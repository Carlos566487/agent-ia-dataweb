from __future__ import annotations

from dataclasses import dataclass

from . import ambiente
from .agente import AgenteDataWeb
from .base_vetorial import BaseVetorialChroma
from .contratos import GeradorDeResposta
from .gerador_claude import GeradorClaude
from .gerador_gemini import GeradorGemini
from .embedding import EmbeddingMultilingue
from .fonte_markdown import FonteMarkdown
from .fonte_pdf import FontePdf
from .fragmentador import FragmentadorSemantico
from .indexador import IndexadorDeDocumentos
from .leitor_pdf import LeitorPdf
from .leitor_sem_repeticao import LeitorSemRepeticao
from .normalizador import NormalizadorPortugues
from .pesquisa import PesquisaSemantica
from .separador import SeparadorDeFrases


@dataclass(frozen=True)
class Aplicacao:
    indexador: IndexadorDeDocumentos
    pesquisa: PesquisaSemantica


def construir(modelo: str, armazenamento: str) -> Aplicacao:
    embedding = EmbeddingMultilingue(modelo=modelo)
    base = BaseVetorialChroma(caminho=armazenamento)
    separador = SeparadorDeFrases()
    indexador = IndexadorDeDocumentos(
        fontes=[
            FontePdf(
                leitor=LeitorSemRepeticao(LeitorPdf(NormalizadorPortugues())),
                fragmentador=FragmentadorSemantico(separador),
            ),
            FonteMarkdown(FragmentadorSemantico(separador, tamanho=2000, sobreposicao=300)),
        ],
        embedding=embedding,
        base=base,
    )
    return Aplicacao(indexador=indexador, pesquisa=PesquisaSemantica(embedding, base))


def escolher_gerador() -> GeradorDeResposta:
    ambiente.carregar()
    gemini = ambiente.chave("GOOGLE_GENERATIVE_AI_API_KEY")
    if gemini:
        return GeradorGemini(gemini)
    return GeradorClaude(ambiente.chave("ANTHROPIC_API_KEY"))


def construir_agente(modelo: str, armazenamento: str) -> AgenteDataWeb:
    return AgenteDataWeb(construir(modelo, armazenamento).pesquisa, escolher_gerador())
