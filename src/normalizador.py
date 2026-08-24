from __future__ import annotations

import re
import unicodedata


class NormalizadorPortugues:
    LIGATURAS = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"}
    INVISIVEIS = re.compile(r"[​‌‍‎‏﻿\xad]")
    HIFEN_QUEBRADO = re.compile(r"([A-Za-zÀ-ÿ])-\s*\n\s*([a-zà-ÿ])")
    PARAGRAFO = re.compile(r"\n\s*\n")
    QUEBRA = re.compile(r"\s*\n\s*")
    ESPACOS = re.compile(r"[ \t\xa0]{2,}")
    SUMARIO = re.compile(r"^[^\n]*\.{5,}[^\n]*$", re.MULTILINE)

    def normalizar(self, texto: str) -> str:
        texto = unicodedata.normalize("NFC", texto)
        for ligatura, simples in self.LIGATURAS.items():
            texto = texto.replace(ligatura, simples)
        texto = self.INVISIVEIS.sub("", texto)
        texto = self.SUMARIO.sub("", texto)
        texto = self.HIFEN_QUEBRADO.sub(r"\1\2", texto)
        paragrafos = (self.QUEBRA.sub(" ", p).strip() for p in self.PARAGRAFO.split(texto))
        limpos = (self.ESPACOS.sub(" ", p) for p in paragrafos if p.strip())
        return "\n\n".join(limpos)
