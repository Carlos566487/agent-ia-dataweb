# Base de Conhecimento RAG: Relatório de Comissão por Vendedor no Sistema DATAWEB

## Informações do Documento Original
- **Manual de Origem:** RELATÓRIO DE COMISSÃO POR VENDEDOR.pdf
- **Módulo Principal:** Financeiro
- **Versão:** 01.01 (Setembro/2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Financeiro
  - Relatórios e Gráficos
    - Relatórios
      - Comissões
        - Comissões de Vendedor (Regra de forma de pagamento)
          - Visão Geral do Módulo de Comissões
          - Acesso ao Sistema e Seleção do Relatório
          - Definição de Critérios e Filtros
          - Visualização dos Resultados

---

## 2. Chunks Estruturados para RAG

### [comissao-vendedor_financeiro_conceito_01]
**Metadados:**
```json
{
  "id": "comissao-vendedor_financeiro_conceito_01",
  "manual_origem": "RELATÓRIO DE COMISSÃO POR VENDEDOR.pdf",
  "modulo": "Financeiro",
  "assunto": "Comissão por Vendedor",
  "subassunto": "Conceito e Funcionalidade de Cálculo",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral do módulo de comissão por vendedor",
  "palavras_chave": ["comissão de vendedor", "cálculo automático", "bonificação", "metas de vendas", "faixas de desempenho"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Comissão por Vendedor no Sistema DATAWEB.

O módulo de Comissão por Vendedor do sistema DATAWEB foi projetado para gerenciar o cálculo e pagamento de comissões de forma automatizada e eficiente.

**Características operacionais:**
- Permite configurar regras vinculadas a categorias de produtos, metas de vendas ou faixas de desempenho;
- Realiza o cálculo automático das comissões devidas com base nas vendas registradas na base de dados;
- Gera relatórios detalhados com total transparência e precisão para acompanhamento individual e controle financeiro de bonificações.

**Perguntas frequentes relacionadas:**
- Como funciona o cálculo de comissão de vendedor no Dataweb?
- O módulo de comissão por vendedor permite vincular bonificações a metas ou faixas de desempenho?
- O cálculo de comissão é gerado de forma automática pelo sistema?

**Imagens associadas:** nenhuma

---

### [comissao-vendedor_financeiro_gerar-relatorio_02]
**Metadados:**
```json
{
  "id": "comissao-vendedor_financeiro_gerar-relatorio_02",
  "manual_origem": "RELATÓRIO DE COMISSÃO POR VENDEDOR.pdf",
  "modulo": "Financeiro",
  "assunto": "Relatórios de Vendas e Comissões",
  "subassunto": "Emissão de Comissão por Vendedor (Regra de Forma de Pagamento)",
  "tipo_conteudo": "procedimento",
  "titulo": "Como emitir o relatório de comissão por vendedor baseado na forma de pagamento",
  "palavras_chave": ["relatório de comissão", "comissão por vendedor", "forma de pagamento", "critérios de filtro", "visualizar comissão"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-4",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Relatórios e Gráficos > Relatórios > Comissões.

**Pré-requisitos:** Permissão de acesso ao módulo `Financeiro` e regras de comissionamento ativas.

**Passo a passo:**
1. No módulo `Financeiro` do DATAWEB, clique no menu superior `Relatórios e Gráficos` e selecione a opção `Relatórios`.
2. Na árvore de tipos de relatórios à esquerda, clique na aba/pasta `Comissões`.
3. Selecione a opção `Comissões de Vendedor (Regra de forma de pagamento)`.
4. Na janela de critérios (filtros), defina os parâmetros desejados para apuração:
   - `Período`: intervalo de datas da pesquisa (ex.: `23/09/2024` a `23/09/2024`).
   - `Considerar intervalo`: selecione o critério de data (ex.: `Data de emissão`).
   - `Diferenciar cheque de cheque-pré`: marque caso pague comissão diferenciada para cheques à vista (se a venda for parcelada em 10x no cheque e contiver um cheque à vista, o relatório separa os valores).
   - `Exibir dados da transação de venda`: marque para exibir os números de venda, datas e valores unitários das parcelas.
   - `Um vendedor por página`: divide a visualização em uma página separada para cada vendedor.
   - `Separar vendas de orçamento do vendedor`: segrega orçamentos de vendas efetivas.
   - `Considerar devoluções`: deduz valores referentes a devoluções de mercadorias.
   - `Sempre considerar a forma de pagamento atual do financeiro (NÃO considera como carnê os lançamentos já pagos)`.
   - `Apenas carnês PAGOS conforme data de pagamento/recebimento. Demais formas consideram data acima selecionada.`
   - `Apenas boletos PAGOS conforme data de pagamento/recebimento.`
   - `Considerar múltiplos cartões. Separar POR NSU.`
   - `Desconsiderar a bandeira do cartão de crédito.` [REVISAR: a opção aparece listada de forma duplicada no menu de critérios].
   - `Gerar dados para preparar para exportação` / `Apagar registros de exportação`.
   - `Tipo`: Formato 1 (Empresa | Venda | Data | Valor), Formato 2 (Empresa | Vendedor | Totais forma pagamento) ou Formato 3.
   - Parâmetros específicos: `Empresa`, `Vendedor`, `Comissão fixa`, `Comissão de vendedor para convênio`, `Comissão sobre sinais recebidos`, `Comissão sobre créditos usados` e `Venda/Orçamento`.
5. Clique no botão `Visualizar` na barra de ações.
6. O sistema abrirá a visualização do relatório com os seguintes dados:
   - Cabeçalho: Empresa, período, filtros e Total a pagar de comissão da empresa.
   - Bloco do Vendedor: Nome do vendedor, status de vendas em convênio e sinais recebidos, e Total a receber de comissão.
   - Grade discriminada: Transação com número do pedido/venda, data, valor total da venda, forma de pagamento detalhada (ex.: `Cartão - ELO DEBITO`, `Cartão - MAESTRO DEBITO`, `Cartão - MASTERCARD CREDITO`, `Cartão - PIX/TED`, `Cartão - VISA CREDITO`, `Dinheiro`, `Financeira SALDO A RECEBER`), `B. comissão` (base de cálculo), `%` (taxa de comissão) e `A receber` (valor calculado).
   - Linhas de totais: `Totais do vendedor`, `Totais da empresa` e `Total geral`.

**Perguntas frequentes relacionadas:**
- Como visualizar os dados completos de cada transação de venda no relatório de comissão?
- Como calcular comissão considerando apenas carnês e boletos que já foram quitados?
- O que é necessário selecionar para ver o relatório de comissões por vendedor no Financeiro?

**Imagens associadas:**
- Página 2: Barra superior do COMMERCIO Financeiro indicando `Relatórios e Gráficos > Relatórios` e navegação na árvore de `Comissões > Comissões de Vendedor (Regra de forma de pagamento)`.
- Página 3: Janela completa de critérios de filtro (período, checkboxes de transação, devoluções, carnês, múltiplos cartões e exportação).
- Página 4: Demonstração da visualização impressa do "RELATÓRIO DE COMISSÕES" detalhando cada venda, percentuais de 2,00% e 3,00% e totalizadores consolidados.

---

## 3. Glossário do Manual
- **Comissões de Vendedor (Regra de forma de pagamento):** Relatório operacional do módulo Financeiro que apura os vencimentos de comissão do vendedor conforme a regra cadastrada para o meio de quitação da venda.
- **Sinais recebidos:** Valores recebidos como adiantamento na contratação de produtos/serviços que ainda não foram totalmente faturados.
- **B. comissão:** Valor base da venda sobre o qual incide a porcentagem de comissão atribuída.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 1 (Sumário):** No sumário, o título do primeiro tópico foi diagramado com caracteres truncados: *"COMISSÃO POR VENT STICAS"*.
- **Página 3:** A opção *"Desconsiderar a bandeira do cartão de crédito."* é listada duas vezes consecutivas nos critérios de filtro.