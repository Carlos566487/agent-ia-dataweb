from __future__ import annotations

from typing import Iterator

from .contratos import Separador


class FragmentadorSemantico:
    def __init__(self, separador: Separador, tamanho: int = 1000, sobreposicao: int = 200):
        self.separador = separador
        self.tamanho = tamanho
        self.sobreposicao = sobreposicao

    def fragmentar(self, texto: str) -> list[str]:
        fragmentos: list[str] = []
        atual: list[str] = []
        for frase in self._frases(texto):
            if atual and self._comprimento(atual) + len(frase) > self.tamanho:
                fragmentos.append(" ".join(atual))
                atual = self._cauda(atual)
            atual.append(frase)
        if atual:
            fragmentos.append(" ".join(atual))
        return fragmentos

    def _frases(self, texto: str) -> Iterator[str]:
        for bloco in texto.split("\n\n"):
            for frase in self.separador.separar(bloco):
                yield from self._dividir_longa(frase)

    def _dividir_longa(self, frase: str) -> Iterator[str]:
        if len(frase) <= self.tamanho:
            yield frase
            return
        pedaco: list[str] = []
        for palavra in frase.split():
            if pedaco and self._comprimento(pedaco) + len(palavra) > self.tamanho:
                yield " ".join(pedaco)
                pedaco = []
            pedaco.append(palavra)
        if pedaco:
            yield " ".join(pedaco)

    def _cauda(self, frases: list[str]) -> list[str]:
        cauda: list[str] = []
        for frase in reversed(frases):
            if self._comprimento(cauda) + len(frase) > self.sobreposicao:
                break
            cauda.insert(0, frase)
        return cauda

    def _comprimento(self, frases: list[str]) -> int:
        return sum(len(f) + 1 for f in frases)
