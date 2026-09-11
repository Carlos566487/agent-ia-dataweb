# Base de Conhecimento RAG — Análise de Vendas em Ordem de Compra

## 1. Resumo Estrutural do Manual

```
Módulo: Entradas
└── Ordem de Compra
    └── Análise de Vendas
        ├── Conceito: o que é a Análise de Vendas
        ├── Analise de Vendas (acesso à ferramenta) [sumário p.2]
        └── Definir Parâmetros de Pesquisa [sumário p.3]
```

Manual "Pílulas Semanais" (VER 26.08, agosto de 24), criado por Carlos Eduardo — Analista de Suporte e Implantação PDV, homologado por Lincoln Akira — Supervisor de TI. Sumário original: "Analise de Vendas" (p.2) e "Definir Parâmetros de Pesquisa" (p.3).

---

## 2. Chunks

### analise-vendas-oc_entradas_ordem-compra_01

**Metadados:**
```json
{
  "id": "analise-vendas-oc_entradas_ordem-compra_01",
  "manual_origem": "ANALISE_DE_VENDAS_EM_ORDEM_DE_COMPRA.pdf",
  "modulo": "Entradas",
  "assunto": "Ordem de Compra",
  "subassunto": "Análise de Vendas",
  "tipo_conteudo": "conceito",
  "titulo": "O que é a Análise de Vendas em Ordem de Compra",
  "palavras_chave": ["análise de vendas", "ordem de compra", "estoque mínimo", "estoque máximo", "sugestão de compra"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Ordem de Compra > Análise de Vendas

A Análise de Vendas é uma ferramenta do setor de compras que permite acessar, em poucos cliques, uma visão detalhada do desempenho comercial de um item específico. Ela revela a média de vendas do item e fornece uma visão precisa do estoque atual.

A ferramenta considera os parâmetros de **estoque mínimo** e **estoque máximo**, quando devidamente configurados, e usa esses dados para sugerir automaticamente a quantidade ideal de itens a serem adquiridos, mantendo o estoque equilibrado e alinhado com a demanda.

A análise também calcula o número de dias em que o estoque atual será capaz de sustentar as operações, com base na média de vendas observada — o que ajuda o gestor de compras a antecipar cenários e ajustar as estratégias de aquisição, evitando excesso ou falta de produtos.

**Perguntas frequentes relacionadas:**
- Para que serve a Análise de Vendas no Dataweb?
- Como o sistema calcula a quantidade sugerida de compra?
- O que são estoque mínimo e estoque máximo na Análise de Vendas?

**Imagens associadas:** nenhuma.

---

### analise-vendas-oc_entradas_ordem-compra_02

**Metadados:**
```json
{
  "id": "analise-vendas-oc_entradas_ordem-compra_02",
  "manual_origem": "ANALISE_DE_VENDAS_EM_ORDEM_DE_COMPRA.pdf",
  "modulo": "Entradas",
  "assunto": "Ordem de Compra",
  "subassunto": "Análise de Vendas",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar a Análise de Vendas dentro de uma Ordem de Compra",
  "palavras_chave": ["análise de vendas", "ordem de compra", "adicionar múltiplos", "entradas"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Ordem de Compra > Análise de Vendas

Como acessar a tela de Análise de Vendas a partir de uma Ordem de Compra:

1. No módulo **<ENTRADAS>** da DATAWEB, clique em **<Ordem Compra>**.
2. Clique em **<Adicionar Múltiplos>**.
3. Clique em **<Análise de Vendas>**.

**Perguntas frequentes relacionadas:**
- Como abro a tela de Análise de Vendas na Ordem de Compra?
- Onde fica a opção "Análise de Vendas" dentro do módulo Entradas?

**Imagens associadas:**
Tela "Ordem de compra (67)", módulo Entradas, com o menu **Ordem Compra** destacado na barra lateral direita (passo 1); na área de itens, o botão **Adicionar múltiplos** destacado na parte inferior (passo 2); e, acima dele, um menu de contexto aberto com a opção **Análise de vendas...** destacada (passo 3), junto de outras opções como Pesquisa de lentes, Pesquisa de produtos, Produtos de transações abertas sem estoque, Lentes/Armações/Produtos com saldo abaixo/acima do mínimo/máximo. Setas amarelas numeradas (1, 2, 3) indicam a sequência dos cliques.

---

### analise-vendas-oc_entradas_ordem-compra_03

**Metadados:**
```json
{
  "id": "analise-vendas-oc_entradas_ordem-compra_03",
  "manual_origem": "ANALISE_DE_VENDAS_EM_ORDEM_DE_COMPRA.pdf",
  "modulo": "Entradas",
  "assunto": "Ordem de Compra",
  "subassunto": "Definir Parâmetros de Pesquisa",
  "tipo_conteudo": "procedimento",
  "titulo": "Como definir os parâmetros de pesquisa na tela de Análise de Vendas",
  "palavras_chave": ["parâmetros de pesquisa", "análise de vendas", "métricas de análise", "período de apuração", "fornecedor"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3",
  "revisar": true
}
```

**Conteúdo:**

Módulo: Entradas | Assunto: Ordem de Compra > Análise de Vendas > Definir Parâmetros de Pesquisa

Na tela de análise de vendas (aberta conforme o procedimento anterior), é possível definir parâmetros que determinam o formato de análise dos itens que serão sugeridos para compra:

4. Seleção da **empresa** em que será efetuada a análise (pode ser feito para todas as empresas).
5. **Período de apuração**.
6. **Métricas de análise** — modelos de cálculo que podem ser executados de acordo com o perfil de cada empresa. [REVISAR: o texto do manual afirma "são 5 modelos de cálculo", mas a captura de tela (Figura 3, página 3) exibe 6 opções listadas (Opção 1 a Opção 6). Divergência entre o texto e a imagem do manual original.]
7. Além das demais opções de pesquisa — **Família**, **Classificações** e produto específico —, é possível escolher um **fornecedor** (mais adequado ao formato de Ordem de Compra) para realizar a análise de vendas.
8. Ao clicar em **Pesquisar**, o sistema lista os itens baseados no formato de cálculo de sugestão de compra definido anteriormente, e permite, ao selecionar parte ou todos os itens, adicioná-los à ordem de compra clicando em **"OK"**.

**Observações:**
- As opções de métrica de análise (conforme exibidas na tela), tal como aparecem no manual, são:
  - Opção 1: se vendi 10 e meu saldo em estoque é de 3, a quantidade faltante será 7.
  - Opção 2: não importa quanto vendi; se meu estoque máximo for 10 e o meu saldo em estoque é 8, a quantidade faltante será 2.
  - Opção 3: a média mensal será a quantidade faltante.
  - Opção 4: a quantidade faltante será igual à quantidade vendida.
  - Opção 5: a quantidade faltante será igual à média mensal menos o saldo em estoque.
  - Opção 6: a quantidade faltante será calculada para completar o estoque máximo. Somente produtos abaixo do estoque mínimo serão considerados.

**Perguntas frequentes relacionadas:**
- Como funcionam as métricas de cálculo na Análise de Vendas?
- É possível filtrar a Análise de Vendas por fornecedor?
- Como faço para adicionar os itens sugeridos à Ordem de Compra?

**Imagens associadas:**
Tela "Análise de venda", com barra de ferramentas superior (Gravar, Imprimir, Ok, Cancelar); campo de empresa "LOJA 01 - WAGNER" (marcado como "1") e checkbox "Agrupar todas empresas em único registro por produto"; campos de período de vendas de 01/06/2021 a 30/06/2023 (marcado como "2") e seletor "Selecione o tipo do período" definido como "Data de encerramento"; lista com as 6 opções de métrica de cálculo descritas acima (marcada como "3"); seções expansíveis **Família**, **Classificação de produtos**, **Classificação de lente**, **Produto** e **Fornecedor** (com campo de busca preenchido com "KENERSON IND E COM DE PROD OPTIC", marcado como "4"); botão **Pesquisar (F3)** (marcado como "5"); e uma grade de resultados com colunas Código barras, Produto, Qtd. Vend., Estoque atual, Mínimo, Média mensal e Faltando.

---

## 3. Glossário

| Termo | Definição (conforme uso no documento) |
|---|---|
| Ordem de Compra | Documento/tela do módulo Entradas usado para solicitar a compra de produtos a um fornecedor; pode ser alimentado com sugestões vindas da Análise de Vendas. |
| Análise de Vendas | Ferramenta que analisa a média de vendas e o estoque de um item para sugerir a quantidade ideal de compra. |
| Estoque mínimo / Estoque máximo | Parâmetros configuráveis por produto usados como referência para o cálculo da quantidade sugerida de compra. |
| Métricas de análise | Modelos de cálculo (opções 1 a 6, conforme tela) que definem como a "quantidade faltante" é calculada na Análise de Vendas. |
| Adicionar Múltiplos | Botão da tela de Ordem de Compra que abre opções para incluir vários itens de uma vez, entre elas a Análise de Vendas. |

---

## 4. Pontos Sinalizados para Revisão

- **[REVISAR]** O texto do manual afirma que existem "5 modelos de cálculo" de métricas de análise, mas a captura de tela na página 3 exibe 6 opções (Opção 1 a Opção 6). Não é possível determinar, apenas com o material fornecido, qual das duas informações está correta.
