from __future__ import annotations

from pathlib import Path
from typing import Iterator

from pypdf import PdfReader

from .contratos import Normalizador


class LeitorPdf:
    def __init__(self, normalizador: Normalizador):
        self.normalizador = normalizador

    def paginas(self, caminho: Path) -> Iterator[tuple[int, str]]:
        for numero, pagina in enumerate(PdfReader(str(caminho)).pages, start=1):
            texto = self.normalizador.normalizar(pagina.extract_text() or "")
            if texto:
                yield numero, texto
