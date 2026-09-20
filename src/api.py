from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .agente import AgenteDataWeb, Conversa
from .dominio import Resultado
from .fabrica import construir, escolher_gerador

PAGINA  = Path(__file__).resolve().parent.parent / "web" / "index.html"
WEB_DIR = Path(__file__).resolve().parent.parent / "web"

SEM_CHAVE = (
    "Não há credencial de nenhum provedor configurada, então não consigo redigir a resposta. "
    "Os trechos do manual encontrados para esta pergunta estão listados abaixo.\n\n"
    "Defina GROK_API_KEY (ou XAI_API_KEY), GOOGLE_GENERATIVE_AI_API_KEY ou ANTHROPIC_API_KEY no arquivo .env e reinicie o servidor."
)


SEM_TEXTO = (
    "O modelo não devolveu texto — normalmente o orçamento de saída foi consumido pelo raciocínio. "
    "Os trechos consultados estão abaixo; tente reformular a pergunta."
)


class Pergunta(BaseModel):
    texto: str
    sessao: str = "padrao"


def criar_app(modelo: str = "intfloat/multilingual-e5-base", armazenamento: str = "storage/chroma") -> FastAPI:
    aplicacao = construir(modelo, armazenamento)
    agente = AgenteDataWeb(aplicacao.pesquisa, escolher_gerador())
    conversas: dict[str, Conversa] = {}
    app = FastAPI(title="Agente DataWeb")
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

    @app.get("/")
    def pagina() -> FileResponse:
        return FileResponse(PAGINA)

    @app.get("/saude")
    def saude() -> dict:
        return {"chunks": aplicacao.indexador.total_indexado(), "modelo": agente.modelo}

    @app.post("/perguntar")
    def perguntar(pergunta: Pergunta) -> StreamingResponse:
        conversa = conversas.setdefault(pergunta.sessao, Conversa())
        resposta = agente.responder(pergunta.texto, conversa)
        texto = resposta.texto if agente.disponivel else iter([SEM_CHAVE])
        return StreamingResponse(_fluxo(resposta.fontes, texto), media_type="text/event-stream")

    return app


def _evento(tipo: str, dados: object) -> str:
    return f"data: {json.dumps({'tipo': tipo, 'dados': dados}, ensure_ascii=False)}\n\n"


def _fluxo(fontes: list[Resultado], texto: Iterator[str]) -> Iterator[str]:
    yield _evento("fontes", [
        {
            "fonte": f.fonte,
            "pagina": f.pagina,
            "score": round(f.score, 3),
            "assunto": f.extra.get("assunto", ""),
            "texto": f.texto,
        }
        for f in fontes
    ])
    vazia = True
    try:
        for pedaco in texto:
            vazia = False
            yield _evento("texto", pedaco)
    except Exception as erro:
        vazia = False
        yield _evento("texto", _mensagem_erro(erro))
    if vazia:
        yield _evento("texto", SEM_TEXTO)
    yield _evento("fim", None)


def _mensagem_erro(erro: Exception) -> str:
    texto = str(erro)
    if "429" in texto or "RESOURCE_EXHAUSTED" in texto or "rate" in texto.lower() or "503" in texto or "UNAVAILABLE" in texto:
        return (
            "⚠️ Limite de requisições ou instabilidade temporária no provedor de IA.\n\n"
            "Aguarde alguns segundos e tente novamente. Se o problema persistir, "
            "verifique o plano e os limites da sua chave de API no arquivo .env."
        )
    if "credits" in texto.lower() or "permission-denied" in texto.lower() or "403" in texto:
        return (
            "⚠️ Sem créditos disponíveis no provedor de IA (xAI / Grok).\n\n"
            "A chave de API do Grok foi configurada com sucesso, mas a sua conta ou time na xAI "
            "ainda não possui créditos recarregados. Recarregue créditos em https://console.x.ai/ "
            "para liberar as respostas do modelo."
        )
    return f"Falha ao gerar a resposta: {type(erro).__name__}: {erro}"


app = criar_app()
