from __future__ import annotations

import logging
import re
import time
from typing import Iterator

from google import genai
from google.genai import types

from .agente import Mensagem

PAPEIS = {"assistente": "model", "usuario": "user"}
ESPERA_PADRAO = 5
ESPERA_REGEX = re.compile(r"retry\s+in\s+([\d.]+)", re.I)

logger = logging.getLogger(__name__)


class GeradorGemini:
    def __init__(self, chave: str, modelo: str = "gemini-3.6-flash", max_tokens: int = 16000,
                 raciocinio: str = "low", tentativas: int = 3):
        self.modelo = modelo
        self.max_tokens = max_tokens
        self.raciocinio = raciocinio
        self.tentativas = tentativas
        self.cliente = genai.Client(api_key=chave) if chave else None

    @property
    def disponivel(self) -> bool:
        return self.cliente is not None

    def gerar(self, instrucao: str, mensagens: list[Mensagem]) -> Iterator[str]:
        contents = [
            types.Content(role=PAPEIS[m.papel], parts=[types.Part.from_text(text=m.texto)])
            for m in mensagens
        ]
        config = types.GenerateContentConfig(
            system_instruction=instrucao,
            max_output_tokens=self.max_tokens,
            thinking_config=types.ThinkingConfig(thinking_level=self.raciocinio),
        )
        fluxo = self._iniciar_com_retentativa(contents, config)
        for pedaco in fluxo:
            if pedaco.text:
                yield pedaco.text

    def _iniciar_com_retentativa(self, contents: list, config: types.GenerateContentConfig):
        """Tenta criar o stream, re-tentando em caso de rate-limit (429)."""
        ultimo_erro: Exception | None = None
        for tentativa in range(self.tentativas):
            try:
                return self.cliente.models.generate_content_stream(
                    model=self.modelo,
                    contents=contents,
                    config=config,
                )
            except Exception as erro:
                if not self._eh_limite(erro) or tentativa >= self.tentativas - 1:
                    raise
                ultimo_erro = erro
                espera = self._calcular_espera(erro, tentativa)
                logger.warning(
                    "Rate limit Gemini (tentativa %d/%d), aguardando %.1fs…",
                    tentativa + 1, self.tentativas, espera,
                )
                time.sleep(espera)
        raise ultimo_erro  # pragma: no cover

    @staticmethod
    def _eh_limite(erro: Exception) -> bool:
        texto = str(erro)
        return "429" in texto or "RESOURCE_EXHAUSTED" in texto

    @staticmethod
    def _calcular_espera(erro: Exception, tentativa: int) -> float:
        """Extrai o delay sugerido pela API ou usa backoff exponencial."""
        encontrado = ESPERA_REGEX.search(str(erro))
        if encontrado:
            return float(encontrado.group(1)) + 1  # +1s margem de segurança
        return min(ESPERA_PADRAO * (2 ** tentativa), 60)
