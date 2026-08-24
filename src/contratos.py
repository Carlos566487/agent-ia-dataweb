from __future__ import annotations

from pathlib import Path
from typing import Iterator, Protocol

from .dominio import Chunk, Resultado


class Normalizador(Protocol):
    def normalizar(self, texto: str) -> str: ...


class Separador(Protocol):
    def separar(self, texto: str) -> list[str]: ...


class Fragmentador(Protocol):
    def fragmentar(self, texto: str) -> list[str]: ...


class LeitorDeDocumento(Protocol):
    def paginas(self, caminho: Path) -> Iterator[tuple[int, str]]: ...


class FonteDeChunks(Protocol):
    def aceita(self, caminho: Path) -> bool: ...
    def chunks(self, caminho: Path) -> Iterator[Chunk]: ...


class EmbeddingDeDocumentos(Protocol):
    def documentos(self, textos: list[str]) -> list[list[float]]: ...


class EmbeddingDeConsulta(Protocol):
    def consulta(self, texto: str) -> list[float]: ...


class GeradorDeResposta(Protocol):
    @property
    def modelo(self) -> str: ...
    @property
    def disponivel(self) -> bool: ...
    def gerar(self, instrucao: str, mensagens: list) -> Iterator[str]: ...


class Pesquisador(Protocol):
    def perguntar(self, pergunta: str, quantidade: int = 5) -> list[Resultado]: ...


class EscritaVetorial(Protocol):
    def gravar(self, chunks: list[Chunk], vetores: list[list[float]]) -> None: ...
    def total(self) -> int: ...


class LeituraVetorial(Protocol):
    def buscar(self, vetor: list[float], quantidade: int) -> list[Resultado]: ...
