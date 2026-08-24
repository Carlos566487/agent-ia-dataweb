from __future__ import annotations

import argparse

from src.dominio import Resultado
from src.api import criar_app
from src.fabrica import construir
from src.pesquisa import PesquisaSemantica


def mostrar(resultados: list[Resultado]) -> None:
    for r in resultados:
        assunto = r.extra.get("assunto", "")
        etiqueta = f" | {assunto}" if assunto else ""
        print(f"\n[{r.score:.3f}] {r.fonte} p.{r.pagina}{etiqueta}")
        print(r.texto)


def console(pesquisa: PesquisaSemantica, quantidade: int) -> None:
    print("Digite a pergunta (Ctrl+D para sair).")
    while True:
        try:
            pergunta = input("\npergunta> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if pergunta:
            mostrar(pesquisa.perguntar(pergunta, quantidade))


def main() -> None:
    parser = argparse.ArgumentParser(description="Embedding de PDFs internos em português")
    parser.add_argument("--modelo", default="intfloat/multilingual-e5-base")
    parser.add_argument("--armazenamento", default="storage/chroma")
    comandos = parser.add_subparsers(dest="comando", required=True)

    opcoes = argparse.ArgumentParser(add_help=False)
    opcoes.add_argument("--top", type=int, default=3)

    indexar = comandos.add_parser("indexar")
    indexar.add_argument("pasta")

    buscar = comandos.add_parser("buscar", parents=[opcoes])
    buscar.add_argument("pergunta")

    comandos.add_parser("console", parents=[opcoes])

    servir = comandos.add_parser("servir")
    servir.add_argument("--porta", type=int, default=8000)

    argumentos = parser.parse_args()

    if argumentos.comando == "servir":
        import uvicorn

        uvicorn.run(criar_app(argumentos.modelo, argumentos.armazenamento), host="127.0.0.1", port=argumentos.porta)
        return

    aplicacao = construir(argumentos.modelo, argumentos.armazenamento)

    if argumentos.comando == "indexar":
        for arquivo, quantidade in aplicacao.indexador.indexar_pasta(argumentos.pasta).items():
            print(f"{arquivo}: {quantidade} fragmentos")
        print(f"total na base: {aplicacao.indexador.total_indexado()}")
    elif argumentos.comando == "buscar":
        mostrar(aplicacao.pesquisa.perguntar(argumentos.pergunta, argumentos.top))
    else:
        console(aplicacao.pesquisa, argumentos.top)


if __name__ == "__main__":
    main()
