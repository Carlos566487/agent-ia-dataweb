from __future__ import annotations

import re


class SeparadorDeFrases:
    ABREVIACOES = {
        "sr", "sra", "srs", "sras", "dr", "dra", "drs", "prof", "profa", "eng",
        "art", "arts", "inc", "incs", "par", "cap", "fl", "fls", "pág", "págs",
        "av", "r", "rod", "ltda", "cia", "s.a", "me", "epp", "etc", "obs", "ref",
        "cf", "ex", "exmo", "exma", "ilmo", "num", "nº", "no", "vol", "ed", "cnpj",
        "cpf", "cep", "tel", "aprox", "máx", "mín", "jan", "fev", "mar", "abr",
        "jun", "jul", "ago", "set", "out", "nov", "dez",
    }
    LIMITE = re.compile(r"(?<=[.!?…])\s+(?=[A-ZÀ-ÝÇ0-9\"“'(\[§])")
    ULTIMO_TOKEN = re.compile(r"([A-Za-zÀ-ÿº°ºª\.]+)\.$")

    def separar(self, texto: str) -> list[str]:
        frases: list[str] = []
        acumulado = ""
        for parte in self.LIMITE.split(texto):
            acumulado = f"{acumulado} {parte}".strip()
            if acumulado and not self._termina_em_abreviacao(acumulado):
                frases.append(acumulado)
                acumulado = ""
        if acumulado:
            frases.append(acumulado)
        return frases

    def _termina_em_abreviacao(self, texto: str) -> bool:
        encontrado = self.ULTIMO_TOKEN.search(texto)
        if not encontrado:
            return False
        token = encontrado.group(1).rstrip(".").lower()
        return token in self.ABREVIACOES or len(token) == 1
