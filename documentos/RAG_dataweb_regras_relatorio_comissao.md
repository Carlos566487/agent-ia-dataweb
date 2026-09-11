# Base de Conhecimento RAG: Regras e Relatórios de Comissão de Vendas

## Informações do Documento Original
- **Manual de Origem:** Regras e Relatório de Comissão.pdf
- **Módulo Principal:** Administrador / Financeiro
- **Versão:** 01.01 (Setembro/2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Administrador
  - Ferramentas
    - Regras
      - Regras de comissão por forma de pagamento
        - Visão Geral da Ferramenta de Gestão de Regras de Comissão
        - Acesso ao Cadastro de Regras de Comissão
        - Configuração de Regras de Comissionamento (Adicionar, Remover e Testar)
- Módulo Financeiro e Módulo Administrador
  - Relatórios e Gráficos
    - Relatórios
      - Comissões
        - Comissões - Comissão de vendedor (Regra de forma de pagamento)
          - Pesquisa e Seleção do Relatório
          - Definição de Critérios de Filtro
          - Visualização e Emissão do Relatório Modelo

---

## 2. Chunks Estruturados para RAG

### [regras-relatorio-comissao_adm_conceito_01]
**Metadados:**
```json
{
  "id": "regras-relatorio-comissao_adm_conceito_01",
  "manual_origem": "Regras e Relatório de Comissão.pdf",
  "modulo": "Administrador / Financeiro",
  "assunto": "Regras e Relatórios de Comissão de Vendas",
  "subassunto": "Conceito e Funcionalidades de Comissionamento",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral da ferramenta de gestão de regras e relatório de comissão",
  "palavras_chave": ["regras de comissão", "relatório de comissão", "formas de pagamento", "bandeiras de cartão", "gestão financeira"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Administrador / Financeiro > Regras e Relatórios de Comissão de Vendas.

O sistema conta com uma ferramenta de gestão de regras de comissão que permite definir regras e parâmetros específicos para cada bandeira de cartão e para diferentes formas de pagamento (como crédito, débito, dinheiro, entre outros), garantindo administração detalhada e personalizada para cada tipo de transação.

O Relatório de Comissão é gerado com base nas regras previamente cadastradas, garantindo precisão e transparência nos dados apresentados. O relatório detalha:
- Os valores comissionados por cada forma de pagamento;
- Informações sobre parcelas em aberto e pagas;
- Saldo a receber e outras métricas importantes para a gestão financeira.

**Perguntas frequentes relacionadas:**
- Para que serve a ferramenta de regras de comissão do Dataweb?
- O relatório de comissão detalha valores por forma de pagamento?
- É possível definir percentuais de comissão diferentes por bandeira de cartão?

**Imagens associadas:** nenhuma

---

### [regras-relatorio-comissao_adm_config-regras_02]
**Metadados:**
```json
{
  "id": "regras-relatorio-comissao_adm_config-regras_02",
  "manual_origem": "Regras e Relatório de Comissão.pdf",
  "modulo": "Administrador",
  "assunto": "Regras de Comissionamento",
  "subassunto": "Cadastro e Manutenção de Regras",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar e configurar regras de comissão por forma de pagamento",
  "palavras_chave": ["cadastro de regras", "comissão por forma de pagamento", "adicionar regra", "testar regras", "remover regras"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Administrador > Ferramentas > Regras > Regras de comissão por forma de pagamento.

**Pré-requisitos:** Permissão de acesso ao módulo Administrador.

**Passo a passo para acessar e gerenciar as regras:**
1. No módulo `Administrador`, acesse o menu superior `Ferramentas`.
2. Posicione o cursor sobre o submenu `Regras`.
3. No submenu aberto, clique em `Regras de comissões por forma de pagamento`.
4. Na tela "Regras de comissionamento", utilize as opções de gerenciamento disponíveis no topo da janela:
   - `Adicionar regra` (1): adiciona uma nova linha à tabela para definição dos parâmetros da regra [REVISAR: texto original possui lacuna operacional: "Ao clicar em adicionar linha é adicionada à tela acima...". O botão da interface gráfica intitula-se "Adicionar regra"].
   - `Diminuir prioridade`: ajusta a ordem de precedência da regra cadastrada.
   - `Remover regras` (2): exclui as regras selecionadas da lista.
   - `Testar regras` (3): permite validar o funcionamento das regras cadastradas perante as transações.
   - `Visualizar impressão`: gera a pré-visualização para impressão das regras ativas.
5. Na nova linha adicionada, preencha e configure as colunas obrigatórias conforme a política comercial:
   - `Empresa`: selecione uma loja específica ou `(TODAS)`.
   - `Vendedor`: selecione um colaborador específico ou `(TODOS)`.
   - `Forma de pagamento`: ex.: `DINHEIRO`, `CARTÃO`, `CARNE`.
   - `Tipo`: tipo de transação associada.
   - `Parcelas`: quantidade de parcelas aplicáveis (ex.: 1, 2, 3, etc.).
   - `Cheque`: parametrização para cheques.
   - `Cartão`: bandeira e modalidade (ex.: `VISA DEBITO`, `ELO DEBITO`, `MASTER DEBIT`, `AMERICAN EXP`).
   - `Financeira`: convênio de financeira ou carnê (ex.: `CARNE PROPRIO`, `CARNE GARANTIDO`, `CARNE DA FINANCE`, `FINANCEIRA DO BA`).
   - `Valor mínimo`: valor mínimo transacionado para validação da regra.
   - `Comissão (%)`: percentual de comissão devido ao vendedor (ex.: 5,00%, 4,00%, 3,50%, etc.).

**Perguntas frequentes relacionadas:**
- Onde configuro a comissão por bandeira de cartão no Dataweb?
- Como excluir ou testar uma regra de comissão cadastrada?
- Qual o caminho para abrir o cadastro de regras de comissão por forma de pagamento?

**Imagens associadas:**
- Página 2 (Superior): Captura do menu superior do COMMERCIO Administrador mostrando `Ferramentas > Regras > Regras de comissões por forma de pagamento`.
- Página 2 (Inferior): Janela "Regras de comissionamento" com os botões numerados `1 - Adicionar regra`, `2 - Remover regras`, `3 - Testar regras` e grade com exemplos práticos de parametrização cadastrados.

---

### [regras-relatorio-comissao_financeiro_relatorio_03]
**Metadados:**
```json
{
  "id": "regras-relatorio-comissao_financeiro_relatorio_03",
  "manual_origem": "Regras e Relatório de Comissão.pdf",
  "modulo": "Financeiro / Administrador",
  "assunto": "Relatórios de Comissões",
  "subassunto": "Comissão de Vendedor (Regra de Forma de Pagamento)",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerar o relatório de comissão de vendedor por regra de forma de pagamento",
  "palavras_chave": ["relatório de comissão", "comissão de vendedor", "filtros de comissão", "visualizar comissão", "forma de pagamento"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3-6",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro ou Administrador > Relatórios e gráficos > Relatórios > Comissões.

**Pré-requisitos:** Regras de comissão configuradas previamente e vendas registradas no sistema.

**Passo a passo:**
1. Acesse o módulo `Financeiro` ou o módulo `Administrador`.
2. No menu superior, clique na opção `Relatórios e gráficos` e, em seguida, selecione `Relatórios`.
3. No campo `Pesquisa relatório:`, digite `COMISSÃO`.
4. Na árvore de `Tipo Relatório`, expanda a categoria `Comissões`.
5. Selecione a opção `Comissões - Comissão de vendedor (Regra de forma de pagamento)` (nota: esta opção utilizada no manual é meramente exemplar).
6. No painel direito, defina os critérios e filtros a serem exibidos no relatório:
   - `Período`: informe a data inicial e a data final (ex.: `01/10/2024` a `01/10/2024`).
   - `Considerar intervalo`: selecione a referência temporal (ex.: `Data de emissão`).
   - `Diferenciar cheque de cheque-pré`: marque esta opção caso pague comissão diferenciada para cheques à vista (se a venda for feita em 10x no cheque e existir um cheque à vista, o relatório irá separar esses valores).
   - Opções adicionais de filtro (marque conforme a necessidade da apuração):
     - `Exibir dados da transação de venda`
     - `Um vendedor por página`
     - `Separar vendas de orçamento do vendedor`
     - `Considerar devoluções`
     - `Sempre considerar a forma de pagamento atual do financeiro (NÃO considera como carnê os lançamentos já pagos)`
     - `Apenas carnês PAGOS conforme data de pagamento/recebimento. Demais formas consideram data acima selecionada.`
     - `Apenas boletos PAGOS conforme data de pagamento/recebimento.`
     - `Considerar múltiplos cartões. Separar POR NSU.`
     - `Desconsiderar a bandeira do cartão de crédito.` [REVISAR: a opção aparece listada em duplicidade na tela do sistema].
     - `Gerar dados para preparar para exportação` / `Apagar registros de exportação`
     - `Tipo`: Formato 1 (Empresa | Venda | Data | Valor), Formato 2 (Empresa | Vendedor | Totais forma pagamento) ou Formato 3 (Grava arquivo).
     - Filtros específicos de cadastro: `Empresa`, `Vendedor`, `Comissão fixa`, `Comissão de vendedor para convênio`, `Comissão sobre sinais recebidos`, `Comissão sobre créditos usados` e `Venda/Orçamento`.
7. Clique no botão `Visualizar` na barra de ferramentas superior para emitir o relatório.

**Estrutura dos dados exibidos no relatório final:**
- Cabeçalho com identificação da loja, período e filtros aplicados.
- Total a pagar de comissão da empresa.
- Identificação do vendedor e indicação de vendas em convênio ou sinais recebidos (se considerados ou não).
- Total a receber de comissão por vendedor.
- Grade analítica discriminando: `Descrição da comissão` (forma de pagamento, bandeira e parcelas), `B. comissão` (base de cálculo), `%` (percentual da regra) e `A receber` (valor monetário da comissão).
- Linhas de consolidação: `Totais do vendedor`, `Totais da empresa` e `Total geral`.

**Perguntas frequentes relacionadas:**
- Como filtrar o relatório de comissão por data de emissão?
- O que significa a opção "Diferenciar cheque de cheque-pré" no relatório de comissões?
- Onde clicar para visualizar o relatório de comissão após configurar os filtros?

**Imagens associadas:**
- Página 3: Menu superior do COMMERCIO Financeiro indicando `Relatórios e gráficos > Relatórios` e tela com busca por "COMISSÃO".
- Página 4: Lista de relatórios expandida em `Comissões` com destaque para `Comissões - Comissão de vendedor (Regra de forma de pagamento)`.
- Página 5: Painel com os parâmetros e critérios de filtro do relatório de comissões.
- Página 6: Destaque no botão `Visualizar` e modelo completo impresso do "RELATÓRIO DE COMISSÕES" com o cálculo detalhado por transação e bandeira.

---

## 3. Glossário do Manual
- **COMMERCIO / DATAWEB:** Sistema integrado de gestão comercial e administrativa (ERP) utilizado pela rede Óticas Diniz.
- **Módulo Administrador:** Módulo do sistema Dataweb focado no controle de cadastros gerais, regras de negócio, usuários e parametrizações operacionais.
- **Módulo Financeiro:** Módulo do sistema Dataweb responsável pela gestão de fluxo de caixa, conciliação bancária, contas a pagar/receber e relatórios de comissões.
- **NSU (Número Sequencial Único):** Código numérico que identifica individualmente cada transação realizada por meio de cartão ou TEF.
- **B. comissão (Base de Comissão):** Valor financeiro sobre o qual é aplicado o percentual contratual da regra de comissão cadastrada.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 2:** No texto explicativo *"Ao clicar em adicionar linha é adicionada à tela acima..."*, há truncamento gramatical / ausência do nome do botão. Na interface gráfica, o botão correspondente intitula-se `Adicionar regra`.
- **Página 5:** A opção de checkbox *"Desconsiderar a bandeira do cartão de crédito."* é apresentada duas vezes consecutivas na tela de critérios de filtro.