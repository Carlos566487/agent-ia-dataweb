from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterator

from .contratos import Fragmentador
from .dominio import Chunk, Escalar


class FonteMarkdown:
    SECAO = re.compile(r"^###[ \t]+(.+?)[ \t]*$", re.M)
    FIM_SECAO = re.compile(r"^#{1,2}[ \t]", re.M)
    BLOCO_JSON = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)
    ROTULOS = re.compile(r"\*\*|^-{3,}$", re.M)
    PRIMEIRO_NUMERO = re.compile(r"\d+")

    def __init__(self, fragmentador: Fragmentador, limite: int = 2200):
        self.fragmentador = fragmentador
        self.limite = limite

    def aceita(self, caminho: Path) -> bool:
        return caminho.suffix.lower() in {".md", ".markdown"}

    def chunks(self, caminho: Path) -> Iterator[Chunk]:
        texto = caminho.read_text(encoding="utf-8")
        for posicao, (titulo, corpo) in enumerate(self._secoes(texto)):
            dados = self._metadados(corpo)
            if dados is None:
                continue
            conteudo = self._conteudo(corpo, dados.get("titulo", titulo))
            for parte, fragmento in enumerate(self._dentro_do_limite(conteudo)):
                yield Chunk(
                    text=fragmento,
                    source=caminho.name,
                    page=self._pagina(dados),
                    position=posicao * 100 + parte,
                    extra=self._extra(dados),
                )

    def _secoes(self, texto: str) -> Iterator[tuple[str, str]]:
        partes = self.SECAO.split(texto)
        for titulo, corpo in zip(partes[1::2], partes[2::2]):
            corte = self.FIM_SECAO.search(corpo)
            yield titulo.strip(), corpo[: corte.start()] if corte else corpo

    def _metadados(self, corpo: str) -> dict | None:
        encontrado = self.BLOCO_JSON.search(corpo)
        if not encontrado:
            return None
        try:
            return json.loads(encontrado.group(1))
        except json.JSONDecodeError:
            return None

    def _conteudo(self, corpo: str, titulo: str) -> str:
        sem_json = self.BLOCO_JSON.sub("", corpo).replace("**Metadados:**", "")
        limpo = self.ROTULOS.sub("", sem_json)
        linhas = [l.rstrip() for l in limpo.split("\n")]
        return f"{titulo}\n" + "\n".join(l for l in linhas if l.strip())

    def _dentro_do_limite(self, conteudo: str) -> list[str]:
        if len(conteudo) <= self.limite:
            return [conteudo]
        titulo = conteudo.split("\n", 1)[0]
        partes = self.fragmentador.fragmentar(conteudo)
        return partes[:1] + [f"{titulo}\n{parte}" for parte in partes[1:]]

    def _pagina(self, dados: dict) -> int:
        encontrado = self.PRIMEIRO_NUMERO.search(str(dados.get("pagina_origem", "")))
        return int(encontrado.group()) if encontrado else 0

    def _extra(self, dados: dict) -> dict[str, Escalar]:
        return {chave: self._escalar(valor) for chave, valor in dados.items() if valor not in ("", None)}

    def _escalar(self, valor: object) -> Escalar:
        if isinstance(valor, (list, tuple)):
            return " | ".join(str(v) for v in valor)
        if isinstance(valor, (bool, int, float)):
            return valor
        return str(valor)
