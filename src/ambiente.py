from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent


def carregar() -> None:
    load_dotenv(RAIZ / ".env")


def chave(nome: str) -> str:
    return os.environ.get(nome, "").strip()
