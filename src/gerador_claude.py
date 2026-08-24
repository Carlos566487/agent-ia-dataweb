from __future__ import annotations

import logging
import time
from typing import Iterator

import anthropic

from .agente import Mensagem

PAPEIS = {"assistente": "assistant", "usuario": "user"}
ESPERA_PADRAO = 5

logger = logging.getLogger(__name__)


class GeradorClaude:
    def __init__(self, chave: str, modelo: str = "claude-opus-5", esforco: str = "medium",
                 max_tokens: int = 16000, tentativas: int = 3):
        self.modelo = modelo
        self.esforco = esforco
        self.max_tokens = max_tokens
        self.tentativas = tentativas
        self.cliente = anthropic.Anthropic(api_key=chave) if chave else None

    @property
    def disponivel(self) -> bool:
        return self.cliente is not None

    def gerar(self, instrucao: str, mensagens: list[Mensagem]) -> Iterator[str]:
        mensagens_api = [{"role": PAPEIS[m.papel], "content": m.texto} for m in mensagens]
        ultimo_erro: Exception | None = None
        for tentativa in range(self.tentativas):
            try:
                with self.cliente.messages.stream(
                    model=self.modelo,
                    max_tokens=self.max_tokens,
                    system=instrucao,
                    output_config={"effort": self.esforco},
                    messages=mensagens_api,
                ) as fluxo:
                    yield from fluxo.text_stream
                return
            except Exception as erro:
                if not self._eh_limite(erro) or tentativa >= self.tentativas - 1:
                    raise
                ultimo_erro = erro
                espera = min(ESPERA_PADRAO * (2 ** tentativa), 60)
                logger.warning(
                    "Rate limit Claude (tentativa %d/%d), aguardando %.1fs…",
                    tentativa + 1, self.tentativas, espera,
                )
                time.sleep(espera)
        raise ultimo_erro  # pragma: no cover

    @staticmethod
    def _eh_limite(erro: Exception) -> bool:
        if hasattr(erro, "status_code") and erro.status_code == 429:
            return True
        texto = str(erro)
        return "429" in texto or "rate" in texto.lower()
