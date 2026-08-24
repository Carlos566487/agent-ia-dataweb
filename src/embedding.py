from __future__ import annotations

from sentence_transformers import SentenceTransformer


class EmbeddingMultilingue:
    def __init__(
        self,
        modelo: str = "intfloat/multilingual-e5-base",
        prefixo_documento: str = "passage: ",
        prefixo_consulta: str = "query: ",
        lote: int = 16,
        dispositivo: str | None = None,
    ):
        self.modelo = SentenceTransformer(modelo, device=dispositivo)
        self.prefixo_documento = prefixo_documento
        self.prefixo_consulta = prefixo_consulta
        self.lote = lote

    def documentos(self, textos: list[str]) -> list[list[float]]:
        return self._codificar([self.prefixo_documento + t for t in textos])

    def consulta(self, texto: str) -> list[float]:
        return self._codificar([self.prefixo_consulta + texto])[0]

    def _codificar(self, textos: list[str]) -> list[list[float]]:
        vetores = self.modelo.encode(
            textos,
            batch_size=self.lote,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return vetores.tolist()
