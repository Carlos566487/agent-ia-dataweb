from __future__ import annotations

import logging
import time
from typing import Iterator

from openai import OpenAI

from .agente import Mensagem

PAPEIS = {"assistente": "assistant", "usuario": "user"}
ESPERA_PADRAO = 5

logger = logging.getLogger(__name__)


class GeradorGrok:
    def __init__(
        self,
        chave: str,
        modelo: str = "grok-2-latest",
        max_tokens: int = 4096,
        tentativas: int = 3,
        base_url: str = "https://api.x.ai/v1",
    ):
        self.modelo = modelo
        self.max_tokens = max_tokens
        self.tentativas = tentativas
        self.cliente = OpenAI(api_key=chave, base_url=base_url) if chave else None

    @property
    def disponivel(self) -> bool:
        return self.cliente is not None

    def gerar(self, instrucao: str, mensagens: list[Mensagem]) -> Iterator[str]:
        if not self.cliente:
            return

        mensagens_api = [{"role": "system", "content": instrucao}]
        for m in mensagens:
            mensagens_api.append({"role": PAPEIS.get(m.papel, "user"), "content": m.texto})

        ultimo_erro: Exception | None = None
        for tentativa in range(self.tentativas):
            try:
                stream = self.cliente.chat.completions.create(
                    model=self.modelo,
                    messages=mensagens_api,
                    max_tokens=self.max_tokens,
                    stream=True,
                )
                for pedaco in stream:
                    if pedaco.choices and pedaco.choices[0].delta and pedaco.choices[0].delta.content:
                        yield pedaco.choices[0].delta.content
                return
            except Exception as erro:
                if not self._eh_limite(erro) or tentativa >= self.tentativas - 1:
                    raise
                ultimo_erro = erro
                espera = min(ESPERA_PADRAO * (2 ** tentativa), 60)
                logger.warning(
                    "Rate limit Grok (tentativa %d/%d), aguardando %.1fs…",
                    tentativa + 1,
                    self.tentativas,
                    espera,
                )
                time.sleep(espera)
        if ultimo_erro:
            raise ultimo_erro

    @staticmethod
    def _eh_limite(erro: Exception) -> bool:
        if hasattr(erro, "status_code") and erro.status_code == 429:
            return True
        texto = str(erro)
        return "429" in texto or "rate" in texto.lower()
