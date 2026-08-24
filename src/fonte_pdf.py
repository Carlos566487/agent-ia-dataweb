from __future__ import annotations

from pathlib import Path
from typing import Iterator

from .contratos import Fragmentador, LeitorDeDocumento
from .dominio import Chunk


class FontePdf:
    def __init__(self, leitor: LeitorDeDocumento, fragmentador: Fragmentador):
        self.leitor = leitor
        self.fragmentador = fragmentador

    def aceita(self, caminho: Path) -> bool:
        return caminho.suffix.lower() == ".pdf"

    def chunks(self, caminho: Path) -> Iterator[Chunk]:
        for pagina, texto in self.leitor.paginas(caminho):
            for posicao, fragmento in enumerate(self.fragmentador.fragmentar(texto)):
                yield Chunk(text=fragmento, source=caminho.name, page=pagina, position=posicao)
