from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Mapping

Escalar = str | int | float | bool


@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    page: int
    position: int
    extra: Mapping[str, Escalar] = field(default_factory=dict)

    @property
    def id(self) -> str:
        chave = f"{self.source}|{self.page}|{self.position}|{self.text}"
        return hashlib.sha1(chave.encode("utf-8")).hexdigest()

    @property
    def metadata(self) -> dict[str, Escalar]:
        return {"source": self.source, "page": self.page, "position": self.position, **self.extra}


@dataclass(frozen=True)
class Resultado:
    texto: str
    fonte: str
    pagina: int
    score: float
    extra: Mapping[str, Escalar] = field(default_factory=dict)
