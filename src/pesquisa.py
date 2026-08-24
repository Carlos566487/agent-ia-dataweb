from __future__ import annotations

from .contratos import EmbeddingDeConsulta, LeituraVetorial
from .dominio import Resultado


class PesquisaSemantica:
    def __init__(self, embedding: EmbeddingDeConsulta, base: LeituraVetorial):
        self.embedding = embedding
        self.base = base

    def perguntar(self, pergunta: str, quantidade: int = 5) -> list[Resultado]:
        return self.base.buscar(self.embedding.consulta(pergunta), quantidade)
