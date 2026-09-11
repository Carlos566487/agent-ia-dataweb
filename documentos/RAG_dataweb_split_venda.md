# Base de Conhecimento RAG — Emissão de NFSe a partir de uma O.S de Retenção (Split)

> Documento de origem: **SPLIT_DE_VENDA_V2.docx** — "Emissão de NFSe a partir de uma O.S que contém o valor de retenção (split)".

---

## 1. Resumo estrutural do manual (árvore de tópicos reconstituída)

```
Emissão de NFSe a partir de uma O.S que contém o valor de retenção (split)
├── Introdução
├── Como funciona
│   └── Geração automática da O.S de split (24h após a venda no e-commerce)
├── Exemplo — Diferença entre "Observações" e "Obs. interna (adicionada pelo sistema)"
├── Exemplo — Preenchimento da condição de pagamento e encerramento da O.S
│   ├── Parte 1: Preenchendo a condição de pagamento
│   └── Parte 2: Encerrando a O.S e gerando o lançamento no financeiro
└── Emissão da Nota Fiscal
    ├── Opção 1 — Emissão individual (via menu de contexto da O.S)
    └── Opção 2 — Emissão em massa (Ferramentas > Emissão de NF (nova))
```

---

## 2. Lista de chunks

### dataweb-split-venda_faturamento_geracao-os_01
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_geracao-os_01",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "modulo": "Faturamento e Notas Fiscais",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Geração automática da O.S de retenção",
  "tipo_conteudo": "conceito",
  "titulo": "Como funciona a geração automática da O.S de retenção (split) a partir de uma venda no e-commerce",
  "palavras_chave": ["split", "retenção", "O.S", "e-commerce", "DINIZ E-COMMERCE", "observações", "obs. interna"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Geração automática da O.S de retenção.

Este manual explica como funciona a emissão de NFSe a partir de uma Ordem de Serviço (O.S) que contém o valor de retenção (split).

**Como funciona:**
1. Após 24 horas, a contar a partir da venda realizada no e-commerce, o sistema gera uma O.S na empresa **DINIZ E-COMMERCE**.
2. A O.S sempre virá com a situação **"aberta"**.
3. A O.S vai conter um **serviço** (e não um produto); o valor desse serviço será o valor de retenção (split).
4. O **cliente** da O.S será a empresa (franqueado) responsável pela venda no e-commerce.
5. A **empresa** da O.S sempre será a DINIZ E-COMMERCE.
6. Nos campos **Observações** e **Obs. interna (adicionada pelo sistema)** serão adicionadas informações importantes, como: nº da venda, nº da O.S do caixa, valor da venda, empresa que gerou a venda e a chave da NFe da venda.

**Perguntas frequentes relacionadas:**
- Como é gerada a O.S de retenção (split) de uma venda do e-commerce?
- Em qual empresa a O.S de split é sempre lançada?
- Quais informações aparecem nos campos Observações e Obs. interna da O.S de split?

**Imagens associadas:**
- Tela "COMMERCIO – Ordem de serviço (DINIZ E-COMMERCE)", aba Ordens de serviço, mostrando o agrupamento "Situação: 0. Abertas (Dilab Online) (2:Imediato)" com uma O.S de nº 6, cliente "SP CASTRO OPTICA LTDA", destacada em vermelho.
- Tela "Ordem de serviço de venda (6)" com os campos Empresa (DINIZ E-COMMERCE), Cliente/fornecedor (SP CASTRO OPTICA LTDA), os campos Observações e Obs. interna (adicionada pelo sistema) preenchidos com os dados da venda, e a seção Serviços contendo um item "SERVIÇO TESTE" no valor de R$ 107,80 (sem produtos lançados).

---

### dataweb-split-venda_faturamento_campos-observacoes_02
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_campos-observacoes_02",
  "modulo": "Faturamento e Notas Fiscais",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Campos Observações e Obs. interna",
  "tipo_conteudo": "conceito",
  "titulo": "Diferença entre os campos Observações e Obs. interna (adicionada pelo sistema) na O.S de split",
  "palavras_chave": ["observações", "obs. interna", "O.S gerada a partir da internet", "split"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Campos Observações e Obs. interna.

**Importante:** os campos **Observações** e **Obs. interna (adicionada pelo sistema)** possuem praticamente as mesmas informações. A diferença é que o campo **Obs. interna (adicionada pelo sistema)** possui uma informação a mais no início: "O.S gerada a partir da internet".

**Perguntas frequentes relacionadas:**
- Qual a diferença entre o campo Observações e o campo Obs. interna da O.S?
- Por que a Obs. interna começa com o texto "O.S gerada a partir da internet"?

**Imagens associadas:**
- Tabela comparando o texto do campo "Observações" com o da "Observação interna (descrição)": ambos trazem os dados da venda (número da venda, valor, empresa, número da O.S do caixa e chave da NFe), mas a Observação interna inicia com o texto adicional "O.S gerada a partir da internet." (destacado/sublinhado em vermelho na imagem).

---

### dataweb-split-venda_faturamento_condicao-pagamento_03
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_condicao-pagamento_03",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "modulo": "Faturamento e Notas Fiscais",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Encerramento da O.S — Parte 1: Condição de pagamento",
  "tipo_conteudo": "procedimento",
  "titulo": "Como preencher a condição de pagamento antes de encerrar a O.S de split",
  "palavras_chave": ["condição de pagamento", "encerrar ordem de serviço", "lançar no contas a receber", "checkbox"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Encerramento da O.S — Parte 1: Condição de pagamento.

**Pré-requisito:** a O.S de retenção (split) deve já ter sido gerada automaticamente pelo sistema.

**Passo a passo:**
1. **Obs.:** é importante preencher a condição de pagamento para que, quando o usuário for encerrar a O.S, o sistema deixe o checkbox **"Lançar no contas a receber"** disponível para edição.
2. Sem uma condição de pagamento definida, ao tentar encerrar a O.S o checkbox "Lançar no contas a receber" fica desabilitado e o sistema exibe a mensagem "CONDIÇÃO DE PAGAMENTO não definida na transação. NÃO tem valor a faturar."
3. Após inserir uma condição de pagamento, o checkbox **"Lançar no contas a receber"** já vem marcado por padrão.

**Perguntas frequentes relacionadas:**
- Por que o checkbox "Lançar no contas a receber" aparece desabilitado ao encerrar a O.S?
- É necessário preencher a condição de pagamento antes de encerrar a O.S de split?

**Imagens associadas:**
- Tela "Encerrar ordem de serviço", com o texto "Pressione Ok para confirmar o encerramento dessa ordem de serviço", campo Data de encerramento preenchido, o checkbox "Lançar no contas a receber" desabilitado (em cinza, destacado em vermelho) e, abaixo, a mensagem "CONDIÇÃO DE PAGAMENTO não definida na transação. NÃO tem valor a faturar."
- Tela "Encerrar ordem de serviço" com o checkbox "Lançar no contas a receber" marcado e destacado em vermelho, um checkbox adicional "Emitir nota fiscal" desmarcado, e o texto "Modo operação: NAO USAR FATURA" em verde.

---

### dataweb-split-venda_faturamento_lancamento-financeiro_04
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_lancamento-financeiro_04",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "modulo": "Faturamento e Notas Fiscais",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Encerramento da O.S — Parte 2: Lançamento no financeiro",
  "tipo_conteudo": "procedimento",
  "titulo": "Como encerrar a O.S de split e confirmar o lançamento no financeiro",
  "palavras_chave": ["encerrar ordem de serviço", "pagamento", "a receber", "dinheiro", "baixado", "financeiro"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Encerramento da O.S — Parte 2: Lançamento no financeiro.

**Pré-requisito:** condição de pagamento já preenchida na O.S (ver procedimento "Parte 1: Condição de pagamento") e checkbox "Lançar no contas a receber" marcado.

**Passo a passo:**
1. Após clicar em "Ok" na tela de encerramento da O.S, o sistema abre a tela de pagamentos — basta clicar em "Ok" novamente.
2. **Obs.:** caso o usuário queira, pode marcar o checkbox **"Emitir nota fiscal"**; ao marcá-lo, será feito o mesmo procedimento descrito na Opção 1 de emissão de nota fiscal (emissão individual).
3. Após isso, a O.S passa a exibir o ícone de cifrão ($), indicando que o lançamento foi realizado no financeiro com sucesso.
4. **Obs.:** o lançamento gerado sempre será do tipo **"a receber"**, a forma de pagamento em **"dinheiro"** e virá **baixado**.

**Perguntas frequentes relacionadas:**
- Como confirmar que o lançamento financeiro da O.S de split foi gerado com sucesso?
- Qual tipo de lançamento e forma de pagamento são usados no lançamento gerado automaticamente pela O.S de split?
- O que acontece se eu marcar o checkbox "Emitir nota fiscal" ao encerrar a O.S?

**Imagens associadas:**
- Duas telas lado a lado: à esquerda, "Encerrar ordem de serviço" com o checkbox "Lançar no contas a receber" marcado e o botão "Ok" destacado em vermelho; à direita, a tela "Pagamento", com Empresa (DINIZ E-COMMERCE), Cliente/Fornecedor (SP CASTRO OPTICA LTDA), Condição de pagamento "A VISTA", valor "Em dinheiro" de R$ 107,80 e o botão "Ok" destacado em vermelho.
- Tela de listagem de O.S com o agrupamento "Situação: 3. Encerradas", exibindo o ícone verde de cifrão ($) ao lado da O.S nº 6 (SP CASTRO OPTICA LTDA), destacado em vermelho.
- Tela "Lançamento (Normal)", aba Dados, mostrando Empresa (DINIZ E-COMMERCE), Cliente/Fornecedor (SP CASTRO OPTICA LTDA), a opção **"Receber"** selecionada e destacada em vermelho, Valor original de R$ 107,80, e a Forma de pagamento **"Dinheiro"** destacada em vermelho, com o valor já constando como pago (R$ 107,80).

---

### dataweb-split-venda_faturamento_emissao-nf-individual_05
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_emissao-nf-individual_05",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "modulo": "Faturamento e Notas Fiscais",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Emissão de Nota Fiscal — Opção 1 (individual)",
  "tipo_conteudo": "procedimento",
  "titulo": "Como emitir a nota fiscal de uma O.S de split individualmente (Opção 1)",
  "palavras_chave": ["imprimir nota fiscal", "emissão individual", "menu de contexto", "coluna NF"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Emissão de Nota Fiscal — Opção 1 (individual).

Para emitir a NF de uma O.S de split, existem duas opções. Este chunk descreve a **Opção 1**.

**Pré-requisito:** O.S de split já encerrada (com lançamento no financeiro confirmado).

**Passo a passo — Opção 1:**
1. Clique com o botão direito sobre a O.S e escolha a opção **"Imprimir nota fiscal"**.
2. Vai abrir uma tela; nesse caso, basta confirmar se o checkbox está marcado e, em seguida, clicar em **"Ok"**.
3. Após gerar a nota, a coluna **NF** da listagem de O.S será preenchida com o número da nota emitida.

**Observações:**
- Essa opção emite **uma NF por vez**; caso o usuário deseje uma "ação em massa", deve utilizar a Opção 2 (emissão em massa).

**Perguntas frequentes relacionadas:**
- Como emitir a nota fiscal de uma única O.S de split?
- Onde fica a opção "Imprimir nota fiscal" na tela de Ordens de Serviço?
- Como sei se a nota fiscal da O.S já foi emitida?

**Imagens associadas:**
- Menu de contexto exibido ao clicar com o botão direito sobre uma O.S na situação "Encerradas", com a opção **"Imprimir nota fiscal"** destacada em vermelho dentro do grupo "Imprimir" (que também contém "Imprimir Etiqueta de NF" e "Imprimir O.S (F3)").
- Tela "Imprimir notas fiscais" listando a O.S do cliente SP CASTRO OPTICA LTDA com o checkbox de seleção marcado (indicado por uma seta vermelha), o campo "Data de emissão das notas fiscais" e o botão "Ok" destacado em vermelho.
- Tela de listagem de O.S mostrando a coluna "Nº NF" já preenchida com o valor 12 para a O.S nº 6, destacada em vermelho.

---

### dataweb-split-venda_faturamento_emissao-nf-massa_06
**Metadados:**
```json
{
  "id": "dataweb-split-venda_faturamento_emissao-nf-massa_06",
  "manual_origem": "SPLIT_DE_VENDA_V2",
  "modulo": "Faturamento e Notas Fiscais",
  "assunto": "Split de Venda (E-commerce)",
  "subassunto": "Emissão de Nota Fiscal — Opção 2 (em massa)",
  "tipo_conteudo": "procedimento",
  "titulo": "Como emitir notas fiscais em massa a partir da Ordem de Serviço (Opção 2)",
  "palavras_chave": ["Ferramentas", "Emissão de NF (nova)", "emissão em massa", "notas pendentes", "notas a emitir", "CFOP"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "[REVISAR: documento de origem (.docx) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Faturamento e Notas Fiscais > Split de Venda (E-commerce) > Emissão de Nota Fiscal — Opção 2 (em massa).

Este chunk descreve a **Opção 2** de emissão de nota fiscal, usada quando o usuário deseja realizar uma "ação em massa" (emitir várias NFs de uma vez).

**Passo a passo — Opção 2:**
1. No **Ordem de serviço**, vá em **Ferramentas > Emissão de NF (nova)**.
2. Será aberta a tela "Emissão de notas fiscais", com as abas Empresa, Expedição, Natureza de operação e Opções à esquerda, e as abas "Notas a emitir", "Notas pendentes" e "Notas Emitidas" à direita.
3. Realize o filtro utilizando os critérios que desejar e, em seguida, clique em **"Pesquisar"** (ou F3). No exemplo do manual, foi filtrado por NF emitidas a partir do dia 01/07/2024.
4. Selecione os clientes através do checkbox.
5. Defina a data de emissão das notas fiscais.
6. Clique em **"Emitir"**.
7. Após realizar a emissão da NF (mesmo que ela seja rejeitada), as NF selecionadas ficarão na cor verde.

**Observações:**
- **Importante:** nessa segunda opção, é gerada uma NF por transação. Por exemplo, se o cliente possuir três transações, serão emitidas três NFs, uma para cada transação.

**Perguntas frequentes relacionadas:**
- Como emitir notas fiscais em massa para várias O.S de uma vez?
- Onde fica a opção "Emissão de NF (nova)" no menu Ferramentas?
- Se um cliente tiver várias transações, quantas notas fiscais são geradas?

**Imagens associadas:**
- Menu "Ferramentas" aberto na tela de Ordens de Serviço, com o item **"Emissão de NF (Nova)..."** destacado em vermelho, junto de outras opções do menu (Almoxarifado, Gerar fatura, Expedição de O.S, Gerenciador de remessas, Seleção de O.S, Registro de serviço externo, Exceção para faturamento, Exceção para emissão de N.F., Manutenção de ordens de serviço, Agendamento de contatos, Atendimento externo, Manutenção de nota fiscal, Inutilização de nota fiscal).
- Tela "Emissão de notas fiscais" com a aba "Notas pendentes" selecionada, mostrando "Empresa: DINIZ E-COMMERCE" sem registros na lista, e o aviso "Notas fiscais pendentes de 90 dias atrás até hoje".
- Tela "Emissão de notas fiscais" com o filtro "Intervalo de datas: 01/07/2024" preenchido e a lista de Ordens de serviço agrupada por cliente (A M BORGES OPTICA LTDA e CONSUMIDOR), mostrando as respectivas transações, datas e valores totais.
- Mesma tela, com os checkboxes dos clientes "A M BORGES OPTICA LTDA" e "CONSUMIDOR" marcados, o campo "Data de emissão das notas fiscais" preenchido com 23/10/2024, e o botão "Emitir" destacado em vermelho; a imagem traz numeração (1, 2, 3) indicando a ordem das ações: marcar checkbox, definir data, clicar em Emitir.
- Tela "Emissão de notas fiscais" mostrando o cliente "A B BORGES OPTICA" com a linha da transação já em verde, indicando que a NF foi emitida.
- Tabela "Ordens de serviço" mostrando o cliente "A M BORGES OPTICA..." com três transações (números 4, 5 e 12), cada uma com seu próprio valor, destacadas em vermelho — ilustrando que cada transação gera uma NF separada.

---

## 3. Glossário de termos específicos do Dataweb

| Termo/Sigla | Definição (conforme usado no documento) |
| --- | --- |
| **O.S** | Ordem de Serviço — registro gerado automaticamente pelo sistema a partir de uma venda no e-commerce, usado para lançar a retenção (split). |
| **Split (retenção)** | Valor retido referente à venda realizada no e-commerce, lançado como serviço dentro da O.S gerada automaticamente. |
| **DINIZ E-COMMERCE** | Empresa que sempre figura como "Empresa" na O.S de split gerada automaticamente pelo sistema. |
| **Observações** | Campo da O.S preenchido automaticamente pelo sistema com dados da venda (nº da venda, nº da O.S do caixa, valor, empresa geradora e chave da NFe). |
| **Obs. interna (adicionada pelo sistema)** | Campo semelhante ao "Observações", mas que inicia com o texto adicional "O.S gerada a partir da internet". |
| **Lançar no contas a receber** | Checkbox da tela de encerramento da O.S que fica disponível para edição somente após o preenchimento da condição de pagamento. |
| **Modo operação: NAO USAR FATURA** | Indicação exibida na tela de encerramento da O.S informando o modo de operação em uso. |
| **Imprimir nota fiscal (Opção 1)** | Opção do menu de contexto da O.S usada para emitir a nota fiscal individualmente, uma por vez. |
| **Ferramentas > Emissão de NF (nova) (Opção 2)** | Caminho de menu usado para emitir notas fiscais em massa, uma por transação. |

---

## 4. Lista de pontos sinalizados para revisão [REVISAR]

- **[REVISAR: numeração de página]** — O documento de origem (`SPLIT_DE_VENDA_V2.docx`) não contém numeração de páginas explícita; o campo `pagina_origem` de todos os chunks foi marcado como pendente de revisão.
- **[REVISAR: termo "Dilab Online" não explicado]** — A situação da O.S aparece como "0. Abertas (Dilab Online) (2:Imediato)" na primeira imagem do manual, mas o termo "Dilab Online" não é definido em nenhum trecho do texto original. Não foi incluído no glossário por falta de definição no documento, para evitar invenção de conteúdo.
- **[REVISAR: coluna "CFOP/Ence..." truncada]** — Nas telas de emissão de NF em massa, a coluna da grade aparece truncada como "CFOP/Ence..." (provavelmente "CFOP/Encerramento"), mas o texto completo não é visível nem confirmado no manual original.
- **[REVISAR: perfil de usuário não especificado]** — O manual não define explicitamente qual perfil de colaborador (ex.: franqueado, administrador, suporte) deve executar os procedimentos de encerramento de O.S e emissão de NF; o campo `perfil_usuario` foi preenchido como "todos" por padrão, mas pode ser necessário restringir esse valor conforme a política interna da Dataweb.
