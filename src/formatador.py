from __future__ import annotations

import re
from typing import Iterator


class FormatadorNarrativo:
    """Pós-processador leve que captura escapes de formatação do LLM.

    Opera linha a linha sobre o stream, preservando o streaming com
    latência mínima (buffer apenas até a próxima quebra de linha).

    Transformações aplicadas:
    - ``## Heading`` / ``### Heading`` → ``**Heading**``
    - ``---`` (linha divisória)            → removida
    - ``1. Texto``  (lista numerada)       → ``Texto`` (prefixo removido)
    - Linhas em branco consecutivas        → colapsadas em uma só
    """

    HEADING = re.compile(r"^#{1,3}\s+(.+)$")
    DIVISORIA = re.compile(r"^-{3,}\s*$")
    NUMERACAO = re.compile(r"^\d+\.\s+")

    def formatar(self, stream: Iterator[str]) -> Iterator[str]:
        """Consome o stream do LLM e produz chunks já formatados."""
        buffer = ""
        anterior_vazia = False
        for pedaco in stream:
            buffer += pedaco
            while "\n" in buffer:
                linha, buffer = buffer.split("\n", 1)
                transformada = self._transformar_linha(linha)
                atual_vazia = transformada.strip() == ""
                if atual_vazia and anterior_vazia:
                    continue
                anterior_vazia = atual_vazia
                yield transformada + "\n"
        if buffer:
            transformada = self._transformar_linha(buffer)
            if not (transformada.strip() == "" and anterior_vazia):
                yield transformada

    def _transformar_linha(self, linha: str) -> str:
        if self.DIVISORIA.match(linha.strip()):
            return ""
        encontrado = self.HEADING.match(linha)
        if encontrado:
            titulo = encontrado.group(1).strip("* ")
            return f"**{titulo}**"
        linha = self.NUMERACAO.sub("", linha)
        return linha
