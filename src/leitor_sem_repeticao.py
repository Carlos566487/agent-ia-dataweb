from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Iterator

from .contratos import LeitorDeDocumento


class LeitorSemRepeticao:
    DIGITOS = re.compile(r"\d+")

    def __init__(
        self,
        leitor: LeitorDeDocumento,
        proporcao: float = 0.5,
        minimo_paginas: int = 5,
        minimo_caracteres: int = 8,
    ):
        self.leitor = leitor
        self.proporcao = proporcao
        self.minimo_paginas = minimo_paginas
        self.minimo_caracteres = minimo_caracteres

    def paginas(self, caminho: Path) -> Iterator[tuple[int, str]]:
        paginas = list(self.leitor.paginas(caminho))
        moldes = self._moldes_repetidos(paginas)
        for numero, texto in paginas:
            limpo = self._sem(texto, moldes)
            if limpo:
                yield numero, limpo

    def _moldes_repetidos(self, paginas: list[tuple[int, str]]) -> set[str]:
        if len(paginas) < self.minimo_paginas:
            return set()
        contagem: Counter[str] = Counter()
        for _, texto in paginas:
            contagem.update({self._molde(l) for l in texto.split("\n") if self._elegivel(l)})
        limite = len(paginas) * self.proporcao
        return {molde for molde, vezes in contagem.items() if vezes >= limite}

    def _sem(self, texto: str, moldes: set[str]) -> str:
        linhas = [l for l in texto.split("\n") if not self._elegivel(l) or self._molde(l) not in moldes]
        return "\n".join(linhas).strip()

    def _elegivel(self, linha: str) -> bool:
        return len(linha.strip()) >= self.minimo_caracteres

    def _molde(self, linha: str) -> str:
        return self.DIGITOS.sub("#", linha.strip())
