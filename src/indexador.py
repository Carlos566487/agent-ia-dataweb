from __future__ import annotations

from pathlib import Path

from .contratos import EmbeddingDeDocumentos, EscritaVetorial, FonteDeChunks


class IndexadorDeDocumentos:
    def __init__(
        self,
        fontes: list[FonteDeChunks],
        embedding: EmbeddingDeDocumentos,
        base: EscritaVetorial,
    ):
        self.fontes = fontes
        self.embedding = embedding
        self.base = base

    def indexar_pasta(self, pasta: str) -> dict[str, int]:
        arquivos = sorted(p for p in Path(pasta).rglob("*") if p.is_file() and self._fonte(p))
        return {arquivo.name: self.indexar_arquivo(arquivo) for arquivo in arquivos}

    def indexar_arquivo(self, caminho: Path) -> int:
        fonte = self._fonte(caminho)
        if fonte is None:
            return 0
        chunks = list(fonte.chunks(caminho))
        self.base.gravar(chunks, self.embedding.documentos([c.text for c in chunks]))
        return len(chunks)

    def total_indexado(self) -> int:
        return self.base.total()

    def _fonte(self, caminho: Path) -> FonteDeChunks | None:
        return next((f for f in self.fontes if f.aceita(caminho)), None)
