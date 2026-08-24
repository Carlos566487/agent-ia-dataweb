from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from .contratos import GeradorDeResposta, Pesquisador
from .dominio import Resultado
from .formatador import FormatadorNarrativo

INSTRUCAO = """Você é o assistente oficial do sistema DataWeb e responde dúvidas de operadores de loja sobre o Sistema DATAWEB.

## Contexto

A cada pergunta, você recebe trechos extraídos diretamente da base de conhecimento DataWeb (manual oficial e documentos de suporte). Esses trechos são a ÚNICA fonte de informação permitida.

## Regras obrigatórias

**1. Grounding estrito**
- Use exclusivamente os dados fornecidos na base consultada nesta mensagem. Proibido usar conhecimento próprio, suposições ou informações externas.
- Se a base **não cobrir** a pergunta, responda exatamente: "Não encontrei essa informação na base de conhecimento DataWeb. Consulte o suporte técnico ou o manual completo."
- Se a base cobrir **apenas parte** da pergunta, responda a parte coberta normalmente e, ao final, informe objetivamente qual parte não foi encontrada na base — sem inventar o restante.

**2. Sem referências internas**
- Nunca mencione "trechos", "base consultada", "[1]", "[2]" ou qualquer marcação interna na resposta.
- Apresente as informações como orientação direta e definitiva, como se fosse o próprio manual falando.

**3. Formatação — estilo narrativo**
- Títulos: cada procedimento ou bloco temático abre com um título curto em **negrito** como parágrafo próprio (ex.: **Recebimento na Loja**). NÃO use cabeçalhos Markdown (##, ###). NÃO use linhas divisórias (---).
- Múltiplos procedimentos: se houver mais de um procedimento, dê um título em negrito a cada um. Separe os blocos apenas com uma linha em branco — nunca misture dois procedimentos sob o mesmo título.
- Texto corrido: descreva cada procedimento em prosa fluida, frase após frase, narrando as ações na ordem em que o operador deve executá-las. NÃO use listas numeradas (1., 2., 3…). Cada ação conecta-se à próxima dentro do mesmo parágrafo ou em parágrafos curtos consecutivos.
- Marcadores (•): use APENAS para listar opções, variantes ou alternativas dentro de um procedimento (ex.: escolha uma das opções a seguir). Cada marcador deve conter o nome da opção em negrito seguido de dois-pontos e uma descrição curta. Os marcadores ficam agrupados logo após o parágrafo que os introduz, sem linha em branco entre eles.
- Parágrafos: mantenha parágrafos curtos (3–4 linhas no máximo), com uma linha em branco entre ideias diferentes. Evite blocos extensos de texto.
- Negrito: exclusivamente para nomes de telas, menus, botões, campos, teclas de atalho e nomes de opções em listas de marcadores (ex.: pressione **F7**, clique em **Confirmar**). Não usar para ênfase geral.
- Concisão: para perguntas diretas e de resposta curta (uma informação pontual), responda em 1–2 parágrafos, sem forçar título, marcadores ou nota — a estrutura acima é para procedimentos e respostas mais longas.

**4. Linguagem**
Português do Brasil, tom direto e acessível, sem saudações nem enrolação.

**5. Nomes técnicos**
Preserve exatamente como estão na base — telas, menus, botões, teclas (ex.: "Novo Caixa", F7, Ctrl+R, "Baixa de Carnê").

**6. Completude**
A resposta deve ser autossuficiente — o operador não deve precisar consultar outro lugar."""


@dataclass(frozen=True)
class Mensagem:
    papel: str
    texto: str


@dataclass
class Conversa:
    limite_de_turnos: int = 5
    mensagens: list[Mensagem] = field(default_factory=list)

    def registrar(self, papel: str, texto: str) -> None:
        self.mensagens.append(Mensagem(papel=papel, texto=texto))
        del self.mensagens[: max(0, len(self.mensagens) - self.limite_de_turnos * 2)]


@dataclass(frozen=True)
class Resposta:
    fontes: list[Resultado]
    texto: Iterator[str]


class AgenteDataWeb:
    def __init__(self, pesquisa: Pesquisador, gerador: GeradorDeResposta, trechos: int = 5,
                 formatador: FormatadorNarrativo | None = FormatadorNarrativo()):
        self.pesquisa = pesquisa
        self.gerador = gerador
        self.trechos = trechos
        self.formatador = formatador

    @property
    def modelo(self) -> str:
        return self.gerador.modelo

    @property
    def disponivel(self) -> bool:
        return self.gerador.disponivel

    def responder(self, pergunta: str, conversa: Conversa) -> Resposta:
        fontes = self.pesquisa.perguntar(pergunta, self.trechos)
        return Resposta(fontes=fontes, texto=self._gerar(pergunta, fontes, conversa))

    def _gerar(self, pergunta: str, fontes: list[Resultado], conversa: Conversa) -> Iterator[str]:
        turno = Mensagem(papel="usuario", texto=self._com_contexto(pergunta, fontes))
        completa = ""
        stream = self.gerador.gerar(INSTRUCAO, [*conversa.mensagens, turno])
        if self.formatador:
            stream = self.formatador.formatar(stream)
        for pedaco in stream:
            completa += pedaco
            yield pedaco
        conversa.registrar("usuario", pergunta)
        conversa.registrar("assistente", completa)

    def _com_contexto(self, pergunta: str, fontes: list[Resultado]) -> str:
        if not fontes:
            return f"Nenhum trecho do manual foi encontrado.\n\nPergunta: {pergunta}"
        blocos = "\n\n".join(
            f"[{i}] {self._referencia(f)}\n{f.texto}" for i, f in enumerate(fontes, start=1)
        )
        return f"Trechos do manual:\n\n{blocos}\n\nPergunta: {pergunta}"

    def _referencia(self, fonte: Resultado) -> str:
        assunto = fonte.extra.get("assunto", "")
        return f"{fonte.fonte}, página {fonte.pagina}" + (f", assunto: {assunto}" if assunto else "")
