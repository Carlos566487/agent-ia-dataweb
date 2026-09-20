from __future__ import annotations

from dataclasses import dataclass

from . import ambiente
from .agente import AgenteDataWeb
from .base_vetorial import BaseVetorialChroma
from .contratos import GeradorDeResposta
from .gerador_claude import GeradorClaude
from .gerador_gemini import GeradorGemini
from .gerador_grok import GeradorGrok
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
    provedor = (ambiente.chave("PROVEDOR") or "").lower()

    grok_chave = ambiente.chave("GROK_API_KEY") or ambiente.chave("XAI_API_KEY")
    gemini_chave = ambiente.chave("GOOGLE_GENERATIVE_AI_API_KEY")
    claude_chave = ambiente.chave("ANTHROPIC_API_KEY")

    if provedor == "grok" or (not provedor and grok_chave and not gemini_chave):
        modelo = ambiente.chave("GROK_MODEL") or "grok-2-latest"
        return GeradorGrok(grok_chave, modelo=modelo)
    if provedor == "claude" or (not provedor and claude_chave and not gemini_chave):
        modelo = ambiente.chave("CLAUDE_MODEL") or "claude-opus-5"
        return GeradorClaude(claude_chave, modelo=modelo)
    if provedor == "gemini" or (not provedor and gemini_chave):
        modelo = ambiente.chave("GEMINI_MODEL") or "gemini-3.8-flash"
        return GeradorGemini(gemini_chave, modelo=modelo)
    if grok_chave:
        modelo = ambiente.chave("GROK_MODEL") or "grok-2-latest"
        return GeradorGrok(grok_chave, modelo=modelo)
    if claude_chave:
        modelo = ambiente.chave("CLAUDE_MODEL") or "claude-opus-5"
        return GeradorClaude(claude_chave, modelo=modelo)
    return GeradorGemini(gemini_chave)


def construir_agente(modelo: str, armazenamento: str) -> AgenteDataWeb:
    return AgenteDataWeb(construir(modelo, armazenamento).pesquisa, escolher_gerador())
