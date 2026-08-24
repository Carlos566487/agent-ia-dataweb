from __future__ import annotations

import chromadb

from .dominio import Chunk, Resultado


class BaseVetorialChroma:
    def __init__(self, caminho: str = "storage/chroma", colecao: str = "documentos_internos"):
        cliente = chromadb.PersistentClient(path=caminho)
        self.colecao = cliente.get_or_create_collection(colecao, metadata={"hnsw:space": "cosine"})

    def gravar(self, chunks: list[Chunk], vetores: list[list[float]]) -> None:
        if not chunks:
            return
        self.colecao.upsert(
            ids=[c.id for c in chunks],
            documents=[c.text for c in chunks],
            metadatas=[c.metadata for c in chunks],
            embeddings=vetores,
        )

    def buscar(self, vetor: list[float], quantidade: int) -> list[Resultado]:
        resposta = self.colecao.query(query_embeddings=[vetor], n_results=quantidade)
        return [
            Resultado(
                texto=texto,
                fonte=meta["source"],
                pagina=meta["page"],
                score=1 - distancia,
                extra={k: v for k, v in meta.items() if k not in ("source", "page", "position")},
            )
            for texto, meta, distancia in zip(
                resposta["documents"][0], resposta["metadatas"][0], resposta["distances"][0]
            )
        ]

    def total(self) -> int:
        return self.colecao.count()
