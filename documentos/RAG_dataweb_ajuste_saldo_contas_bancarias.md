# Base de Conhecimento RAG — Ajuste de Saldo de Contas Bancárias

## 1. Resumo Estrutural do Manual

```
Módulo: Financeiro
└── Integração Bancária
    └── Ajuste de saldos
        ├── Passo 1: Acessar "Ajuste de saldos"
        ├── Passo 2: Informar a conta e o novo saldo
        └── Passo 3: Confirmar a forma de pagamento e baixar o lançamento
```

Manual da Dataweb Tecnologia (capa "Contas Bancárias — ajuste de saldo"), estruturado em 3 passos numerados, cada um com imagem de apoio, seguido de uma observação (OBS) sobre o comportamento do sistema.

---

## 2. Chunks

### ajuste-saldo-contas-bancarias_financeiro_integracao-bancaria_01

**Metadados:**
```json
{
  "id": "ajuste-saldo-contas-bancarias_financeiro_integracao-bancaria_01",
  "manual_origem": "Ajuste_de_Saldo_de_Contas_Bancárias.pdf",
  "modulo": "Financeiro",
  "assunto": "Integração Bancária",
  "subassunto": "Ajuste de saldos",
  "tipo_conteudo": "procedimento",
  "titulo": "Como ajustar o saldo de uma conta bancária no Dataweb",
  "palavras_chave": ["ajuste de saldo", "conta bancária", "integração bancária", "financeiro", "lançamento"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Financeiro | Assunto: Integração Bancária > Ajuste de saldos

Como ajustar o saldo de uma conta bancária no sistema Dataweb:

1. Acesse **Financeiro** -> **Integração Bancária** e clique em **Ajuste de saldos**.
2. Informe a **Conta** e, no campo **Novo saldo**, digite o valor desejado. Clique em **OK** para continuar.
3. O sistema exibirá a tela do lançamento que será gerado, já com o valor da **Diferença** entre o saldo atual e o novo saldo informado.
4. Confira os dados do lançamento e informe a **forma de pagamento**.
5. Clique em **Baixar** para ajustar o saldo imediatamente.

**Observação:** caso você utilize as opções **OK** ou **Receber** (em vez de **Baixar**), o saldo **não será ajustado** até que o lançamento de ajuste seja baixado.

**Perguntas frequentes relacionadas:**
- Como faço para ajustar o saldo de uma conta bancária no Dataweb?
- Onde fica a opção de ajuste de saldo no módulo Financeiro?
- Por que o saldo da minha conta não mudou depois de clicar em OK ou Receber no ajuste de saldo?

**Imagens associadas:**
1. Submenu **Integração bancária**, exibindo as opções: Emissão de bloqueto, Conciliação, Extrato de conta, Controle de saldos, Transferência entre contas, Acerto de taxas e despesas e **Ajuste de saldos** (destacada/selecionada).
2. Tela de ajuste de saldo, com o campo **Conta** preenchido com "ITAU", **Saldo atual**: 1950, **Novo saldo**: 1900, **Diferença**: 50,00, e os botões **OK** e **Cancelar**.
3. Tela de lançamento gerado pelo ajuste, com os campos: **Empresa**: LOJA DW; **Cliente/fornecedor**: LOJA DW; **Conta classificação**: CONTAS A PAGAR (PAGAR); **Número documento**: AJUSTEDESALDO; **Data de emissão**: 17/04/2018; opção **Pagar** selecionada (ao lado de **Receber**); **Valor original**: 50,00; **Desconto**: 0,00; **Juros**: 0,00; **Total a pagar**: 50,00; campo **Observações** preenchido com "Lançamento gerado a partir da ferramenta de AJUSTE DE SALDO DE CONTA."; seção de forma de pagamento com **Forma**: Banco/Boqueto/Previsão, **Valor**: 50,00, **Conta**: ITAU | LOJA DW, checkbox **Emitir bloqueto bancário**; botões **Receber**, **Baixar**, **OK** e **Cancelar** no rodapé.

**Perguntas frequentes relacionadas (observação sobre baixa do lançamento):**
- O ajuste de saldo é aplicado na hora ou preciso fazer mais alguma coisa?
- Qual a diferença entre clicar em "OK", "Receber" e "Baixar" no ajuste de saldo?

---

## 3. Glossário

| Termo | Definição (conforme uso no documento) |
|---|---|
| Ajuste de saldo | Ferramenta do módulo Financeiro (Integração Bancária) que permite corrigir o saldo de uma conta bancária no sistema, gerando automaticamente um lançamento financeiro correspondente à diferença entre o saldo atual e o novo saldo informado. |
| Integração Bancária | Submenu do módulo Financeiro que reúne funções relacionadas a contas bancárias: emissão de bloqueto, conciliação, extrato de conta, controle de saldos, transferência entre contas, acerto de taxas e despesas, e ajuste de saldos. |
| Baixar (lançamento) | Ação que efetiva/conclui um lançamento financeiro — no contexto do ajuste de saldo, é o que efetivamente atualiza o saldo da conta. |
| AJUSTEDESALDO | Valor padrão exibido no campo **Número documento** do lançamento gerado por um ajuste de saldo. |

---

## 4. Pontos Sinalizados para Revisão

Nenhum ponto de revisão identificado neste manual — conteúdo completo e sem ambiguidades.
