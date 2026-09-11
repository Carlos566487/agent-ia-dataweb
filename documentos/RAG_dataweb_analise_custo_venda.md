# Base de Conhecimento RAG — Análise de Custo e Venda

## 1. Resumo Estrutural do Manual

```
Módulo: Entradas
└── Análise de Custo e Venda (fluxo completo a partir de NFe do fornecedor)
    ├── Conceito: Ferramenta de Controle de Preços e Markup
    ├── NFe Fornecedor - XML Disponível [sumário p.2]
    ├── Criar ENF [sumário p.2]
    ├── Itens do Sistema [sumário p.3]
    ├── Identificação de Produtos Associados [sumário p.3]
    ├── Entrada de Nota Fiscal [sumário p.4]
    ├── Importar Fatura do XML da NFe Importada [sumário p.4]
    └── ANÁLISE DE CUSTO X VENDA [sumário p.5]
```

Manual "Pílulas Semanais" (VER 24.08, agosto de 24), criado por Carlos Eduardo — Analista de Suporte e Implantação PDV, homologado por Lincoln Akira — Supervisor de TI. Descreve um fluxo único e contínuo (passos numerados de 1º a 13º), do qual cada seção do sumário corresponde a uma etapa. Por ter mais de 500 palavras no total, foi dividido em sub-chunks lógicos correspondentes às seções do sumário original.

---

## 2. Chunks

### analise-custo-venda_entradas_conceito_01

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_conceito_01",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Conceito",
  "tipo_conteudo": "conceito",
  "titulo": "O que é a Ferramenta de Controle de Preços e Markup (Análise de Custo x Venda)",
  "palavras_chave": ["análise de custo e venda", "markup", "controle de preços", "preço de custo", "preço de venda"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda

A ferramenta de controle de preços e Markup permite registrar e exibir, com clareza, os últimos preços de custo e venda de cada item comercializado, oferecendo uma visão histórica e comparativa para a tomada de decisões.

Ao receber uma nova nota fiscal, a ferramenta realiza uma análise comparativa entre os valores nela contidos e os preços históricos previamente registrados. Um mecanismo de alerta automático sinaliza qualquer divergência que ultrapasse um percentual "X" previamente definido — percentual que é personalizável pelo gestor.

A ferramenta também simplifica a formação do preço de venda: através da inserção direta do **Markup** desejado, o sistema calcula automaticamente o preço final de venda, reduzindo o tempo gasto em cálculos manuais e minimizando a margem de erro.

**Perguntas frequentes relacionadas:**
- Para que serve a ferramenta de Análise de Custo e Venda no Dataweb?
- Como o sistema alerta sobre divergência de preços em uma nova nota fiscal?
- É possível calcular o preço de venda automaticamente a partir do Markup?

**Imagens associadas:** nenhuma.

---

### analise-custo-venda_entradas_nfe-fornecedor_02

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_nfe-fornecedor_02",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "NFe Fornecedor - XML Disponível",
  "tipo_conteudo": "procedimento",
  "titulo": "Como localizar o XML disponível na aba NFe do Fornecedor",
  "palavras_chave": ["NFe do fornecedor", "XML disponível", "entradas", "nota fiscal eletrônica"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > NFe Fornecedor - XML Disponível

Este é o primeiro passo do fluxo de Análise de Custo e Venda, que parte de uma NFe (Nota Fiscal Eletrônica) do fornecedor.

1º. No módulo de **<ENTRADAS>** DATAWEB, escolha/clique na aba **<NFe do FORNECEDOR>**.
2º. Escolha um "XML" que esteja com o seguinte status: **<Situação: 3 XML disponível>**.

**Perguntas frequentes relacionadas:**
- Onde encontro os XMLs de NFe disponíveis para entrada no Dataweb?
- O que significa a situação "3 XML disponível" na aba NFe do Fornecedor?

**Imagens associadas:**
Figura 1 - "NFe Fornecedor - XML Disponível": tela do módulo Entradas com a aba **NFe de fornecedor** selecionada, mostrando uma grade com colunas Chave de acesso, NFe Fornecedor, Data emissão, CNPJ Fornecedor, Nome fornecedor e Valor; um filtro indicando "Situação : 3 XML disponível"; uma linha da lista destacada/selecionada.

---

### analise-custo-venda_entradas_criar-enf_03

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_criar-enf_03",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Criar ENF",
  "tipo_conteudo": "procedimento",
  "titulo": "Como criar uma ENF a partir do XML da NFe do fornecedor",
  "palavras_chave": ["criar ENF", "ENF", "NFe do fornecedor", "entradas"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > Criar ENF

Continuação do fluxo iniciado na aba NFe do Fornecedor, após localizar o XML disponível:

3º. Após a escolha do XML disponível, clique no mesmo com o botão direito e escolha a opção **<Criar ENF>**.

**Perguntas frequentes relacionadas:**
- Como crio uma ENF a partir de um XML de NFe do fornecedor?
- Onde fica a opção "Criar ENF" no Dataweb?

**Imagens associadas:**
Figura 2 - "Criar ENF": menu de contexto (botão direito) aberto sobre um XML na lista de NFe do Fornecedor, exibindo as opções Manifestar, Ciência da emissão, Confirmação da operação, Desconhecimento, Importar NFe e **Criar ENF** (destacada/selecionada), além de Copiar chave de acesso, Selecionar todos, Destacar todos, Visualizar Documento e Baixar XML da ENF.

---

### analise-custo-venda_entradas_itens-sistema_04

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_itens-sistema_04",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Itens do Sistema / Identificação de Produtos Associados",
  "tipo_conteudo": "procedimento",
  "titulo": "Como selecionar o item do sistema e tratar produtos associados ao criar a ENF",
  "palavras_chave": ["itens do sistema", "produtos associados", "ENF", "entradas"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3",
  "revisar": true
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > Itens do Sistema / Identificação de Produtos Associados

Continuação do fluxo, após clicar em "Criar ENF":

4º. Após a execução do item anterior, o sistema disponibilizará a tela de **Itens do Sistema**.
5º. Marque o item desejado e clique em **<ok>**.
6º. Após a execução do item anterior, o sistema disponibilizará a tela de aviso de **Identificação de Produtos Associados**.
7º. Escolha/clique na opção **<NÃO>**.

[REVISAR: o manual documenta apenas o fluxo ao clicar em "NÃO" no aviso "Existe pelo menos um produto cadastrado que está associado a diferentes produtos desta ENF. Gostaria de identificar quais são este produtos?". O comportamento do sistema caso o usuário clique em "SIM" não é descrito no documento.]

**Perguntas frequentes relacionadas:**
- O que fazer quando aparece o aviso de produto associado a diferentes produtos da ENF?
- Devo clicar em "Sim" ou "Não" na identificação de produtos associados?

**Imagens associadas:**
- Figura 3 - "Itens do Sistema": grade com colunas Ordem, Descrição NF-e, Referência, EAN, Descrição, ID, Código de barras, ID Exportação, NCM, CEST, %IPI, P. de Compra, P. de Venda, CST, Natureza, Qtd e Ordem, exibindo dois itens do produto "L.59 AR PC-HMC POLIMAX (OPTRA)"; campo "Seleção de produto associado" com busca por descrição na parte inferior.
- Figura 4 - "Identificação de Produtos Associados": mesma grade ao fundo, com uma janela de aviso sobreposta contendo o texto "Existe pelo menos um produto cadastrado que está associado a diferentes produtos desta ENF. Gostaria de identificar quais são este produtos?" e os botões **Sim** e **Não**.

---

### analise-custo-venda_entradas_entrada-nota-fiscal_05

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_entrada-nota-fiscal_05",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Entrada de Nota Fiscal",
  "tipo_conteudo": "procedimento",
  "titulo": "Como validar e encerrar a Entrada de Nota Fiscal",
  "palavras_chave": ["entrada de nota fiscal", "encerrar", "natureza da operação", "entradas"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > Entrada de Nota Fiscal

Continuação do fluxo, após tratar os produtos associados:

8º. Após a execução do item anterior, o sistema disponibilizará a tela de **Entrada de nota fiscal**.
9º. Valide e confirme os dados e a **natureza da operação** e, caso esteja tudo de acordo, clique em **<Encerrar (F7)>**.

**Perguntas frequentes relacionadas:**
- Como encerro uma entrada de nota fiscal no Dataweb?
- O que preciso conferir antes de encerrar a entrada de nota fiscal?

**Imagens associadas:**
Figura 5 - "Entrada de Nota Fiscal": tela com campos **Empresa**, tipo de nota fiscal (Recebida / Não-recebida / Não-emitida), **Tipo de nota** (Convencional / NFe / NFe Serviço), **Nro. da nota**, **Série**, **Emissão**, **Recebimento**, **Cliente/fornecedor**, **Condição de pagamento**, **Natureza da operação** (exemplo exibido: "L.101 — COMPRAS PARA INDUSTRIALIZAÇÃO"), **Transportadora**, percentuais de ICMS/ST/frete/seguro/despesas; grade de itens com colunas Código, ID, CFOP, Descrição, Preço compra atual, Und, Qtd, V.Original, Total (item desconto), V.Unitário, Total (com desconto), ICMS (%), Total ICMS, IPI(%) e Total IPI; botões **Gravar (F9)**, **Aprovar (F6)** e **Encerrar (F7)** (destacado) na barra superior, e **Voltar**.

---

### analise-custo-venda_entradas_importar-fatura-xml_06

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_importar-fatura-xml_06",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Importar Fatura do XML da NFe Importada",
  "tipo_conteudo": "procedimento",
  "titulo": "Como importar a fatura do XML ao encerrar a entrada de nota fiscal",
  "palavras_chave": ["importar fatura", "XML", "NFe importada", "encerrar entrada de nota fiscal"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > Importar Fatura do XML da NFe Importada

Continuação do fluxo, imediatamente após clicar em "Encerrar (F7)" na Entrada de Nota Fiscal:

10º. Após a execução do item anterior, o sistema disponibilizará a tela de encerramento com as opções de lançamento.
11º. Habilite a opção **<Importar fatura do XML da NFe importada>** e clique em **<OK>**.

**Perguntas frequentes relacionadas:**
- Como faço para importar a fatura do XML de uma NFe já importada?
- O que a opção "Importar fatura do XML da NFe importada" faz ao encerrar a nota?

**Imagens associadas:**
Figura 6 - "Importar Fatura do XML da NFe Importada": janela "Encerrar entrada de nota fiscal" com as opções: **Lançar contas a pagar**; **Atualizar preço de custo e compra** (nota: "Se marcado permite que seja realizado o lançamento no contas a pagar"/"Se marcado irá recalcular o preço de custo e custo médio dos produtos. Somente para naturezas de compra"); **Atualizar preço de venda** (nota: "Se marcado irá recalcular o preço de venda dos produtos dessa entrada conforme a fórmula previamente configurada no sistema. Somente para naturezas de compra"); **Importar fatura do XML da NFe importada** (destacada, com nota "Se marcado gerará os lançamentos financeiros conforme constante no XML da NFe importada"); **Manifestação de destinatário**, com campo "Informe o motivo da manifestação: (nenhum)" e observação sobre a permissão necessária ("Manifestação de destinatário de NFe ao encerrar ENF"); botões **Ok** e **Cancelar**.

---

### analise-custo-venda_entradas_analise-custo-x-venda_07

**Metadados:**
```json
{
  "id": "analise-custo-venda_entradas_analise-custo-x-venda_07",
  "manual_origem": "ANALISE_DE_CUSTO_E_VENDA_-_PILULAS_SEMANAIS.pdf",
  "modulo": "Entradas",
  "assunto": "Análise de Custo e Venda",
  "subassunto": "Análise de Custo x Venda",
  "tipo_conteudo": "procedimento",
  "titulo": "Como visualizar a Análise de Custo x Venda ao final da entrada de nota fiscal",
  "palavras_chave": ["análise de custo x venda", "variação de preço", "custo atual", "custo novo"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Análise de Custo e Venda > Análise de Custo x Venda

Etapa final do fluxo, exibida após importar a fatura do XML da NFe importada:

12º. Após a execução do item anterior, o sistema disponibilizará a tela final.
13º. A tela refere-se à **<ANÁLISE DE CUSTO X VENDA>**, onde é possível visualizar as variações de valores de "compra", "diferença", "custo atual" e "custo novo".

**Perguntas frequentes relacionadas:**
- Onde vejo a variação de preço de compra e custo depois de encerrar uma nota fiscal?
- O que significam "custo atual" e "custo novo" na Análise de Custo x Venda?

**Imagens associadas:**
Figura 7 - "ANÁLISE DE CUSTO X VENDA": tela com **Fornecedor** (exemplo: VISCO COMERCIAL IMP.EXT.LTDA), **Nota Fiscal** (exemplo: 1880329/1), campos "Variação normal de preço de compra", "Variação normal de preço de custo" e "Variação normal de preço de venda" (todos em 0,00% no exemplo); checkboxes **Destacar compra**, **Destacar custo**, **Destacar venda**, **Destacar valores abaixo da variação normal**, **Destacar variação normal** e **Destacar valores acima da variação normal**; grade com colunas Ordem, Código barras, Descrição, Compra (atual), Compra (nova), Diferença, Atualizar compra, Custo (atual), Custo (novo), Diferença, Atualizar custo, %Markup, Venda mínimo e Venda; no exemplo exibido, o produto de código 0017547 ("LG LP VISCO L.59 POL AR") mostra Compra atual R$ 8,95 → Compra nova R$ 9,67 (diferença 8,04%) e Custo atual R$ 8,95 → Custo novo R$ 9,6 (diferença 8,04%).

---

## 3. Glossário

| Termo | Definição (conforme uso no documento) |
|---|---|
| NFe do Fornecedor | Aba do módulo Entradas onde ficam disponíveis os XMLs de Notas Fiscais Eletrônicas recebidas de fornecedores. |
| XML disponível (Situação: 3) | Status de um XML de NFe que indica que ele está pronto para ser transformado em ENF. |
| ENF | Entrada de Nota Fiscal — documento gerado a partir do XML da NFe do fornecedor, usado para processar a entrada de mercadorias no sistema. |
| Natureza da operação | Classificação fiscal da entrada (exemplo citado: "L.101 — COMPRAS PARA INDUSTRIALIZAÇÃO"), informada na tela de Entrada de Nota Fiscal. |
| Manifestação de destinatário | Ação relacionada à NFe (ciência, confirmação, desconhecimento etc.), disponível no menu de contexto do XML e também como opção ao encerrar a ENF; requer permissão específica. |
| Markup | Percentual aplicado sobre o custo para formação automática do preço de venda. |
| CFOP, NCM, CEST | Códigos fiscais exibidos nas grades de itens da Entrada de Nota Fiscal (Código Fiscal de Operações e Prestações, Nomenclatura Comum do Mercosul, Código Especificador da Substituição Tributária); o manual não detalha o significado de cada sigla, apenas os exibe como colunas do sistema. |

---

## 4. Pontos Sinalizados para Revisão

- **[REVISAR]** O manual não descreve o que acontece caso o usuário clique em **"SIM"** (em vez de "NÃO") na tela de aviso "Identificação de Produtos Associados" — apenas o fluxo pelo "NÃO" está documentado.
