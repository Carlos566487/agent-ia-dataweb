from __future__ import annotations

import re
from typing import Iterator


class FormatadorNarrativo:
    """Pós-processador leve que garante a formatação arejada e estruturada das respostas.

    Opera linha a linha sobre o stream, preservando o streaming com latência mínima.

    Garante:
    - Títulos com emojis e seções destacados e isolados com linhas em branco
    - Cada marcador (•) em sua própria linha individual
    - Espaçamento adequado após frases introdutórias com dois-pontos
    - Preservação de listas numeradas e em tópicos
    - Colapso de linhas vazias excessivas
    """

    HEADING = re.compile(r"^#{1,3}\s+(.+)$")
    DIVISORIA = re.compile(r"^-{3,}\s*$")
    MARCADOR_INTERNO = re.compile(r"(?<=\S)\s+(•\s+)")
    TITULO_NO_MEIO = re.compile(r"([.!?])\s+(\*\*[^\*]{3,50}\*\*)\s+")
    TITULO_ISOLADO = re.compile(r"^\*\*[^\*]{3,50}\*\*:$|^\*\*[^\*]{3,50}\*\*$")

    def formatar(self, stream: Iterator[str]) -> Iterator[str]:
        """Consome o stream do LLM e produz chunks já formatados."""
        buffer = ""
        anterior_vazia = True
        for pedaco in stream:
            buffer += pedaco
            while "\n" in buffer:
                linha, buffer = buffer.split("\n", 1)
                for sublinha in self._processar_linha(linha):
                    atual_vazia = sublinha.strip() == ""
                    if atual_vazia and anterior_vazia:
                        continue
                    anterior_vazia = atual_vazia
                    yield sublinha + "\n"
        if buffer:
            for sublinha in self._processar_linha(buffer):
                if not (sublinha.strip() == "" and anterior_vazia):
                    yield sublinha

    def _processar_linha(self, linha: str) -> list[str]:
        if self.DIVISORIA.match(linha.strip()):
            return []

        # Converte títulos Markdown (### Título) em **Título**
        encontrado_heading = self.HEADING.match(linha.strip())
        if encontrado_heading:
            titulo = encontrado_heading.group(1).strip("* ")
            return ["", f"**{titulo}**", ""]

        # Se um título foi colado no meio de uma frase, separa com quebras duplas
        if self.TITULO_NO_MEIO.search(linha):
            linha = self.TITULO_NO_MEIO.sub(r"\1\n\n\2\n\n", linha)

        # Se houver frase introdutória colada aos marcadores
        linha = re.sub(r":\s+(•\s+)", r":\n\n\1", linha)

        # Se houver múltiplos marcadores na mesma linha, quebra cada um em sua própria linha
        if "•" in linha:
            linha = self.MARCADOR_INTERNO.sub(r"\n\1", linha)

        # Se a linha for um título isolado em negrito, garante linha em branco antes e depois
        linhas_resultantes: list[str] = []
        for l in linha.split("\n"):
            l_limpa = l.strip()
            if self.TITULO_ISOLADO.match(l_limpa):
                linhas_resultantes.extend(["", l_limpa, ""])
            else:
                linhas_resultantes.append(l)

        return linhas_resultantes
