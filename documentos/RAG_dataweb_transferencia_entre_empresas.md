# Base de Conhecimento RAG — Transferência entre Empresas

## 1. Resumo Estrutural do Manual

```
Módulo: Pedido
└── Gerar Pedido de Transferência entre Empresas
    ├── Conceito: alocação de itens de uma entrada entre empresas do grupo
    ├── Figura 1 - Gerar Pedido de Transferência entre Empresas [sumário p.2]
    ├── Figura 2 - Quantidades e Empresas Disponíveis para Transferência [sumário p.2]
    └── Figura 3 - Transação de Saída Loja Origem [sumário p.3]
```

Manual "Pílulas Semanais" (VER 24.08, agosto de 24), criado por Carlos Eduardo — Analista de Suporte e Implantação PDV, homologado por Lincoln Akira — Supervisor de TI.

---

## 2. Chunks

### transferencia-entre-empresas_pedido_conceito_01

**Metadados:**
```json
{
  "id": "transferencia-entre-empresas_pedido_conceito_01",
  "manual_origem": "TRANSFERENCIA_ENTRE_EMPRESAS_-_PILULAS_SEMANAIS_V1.pdf",
  "modulo": "Pedido",
  "assunto": "Transferência entre Empresas",
  "subassunto": "Conceito",
  "tipo_conteudo": "conceito",
  "titulo": "O que é a Transferência entre Empresas no Dataweb",
  "palavras_chave": ["transferência entre empresas", "loja origem", "loja destino", "gestão de estoque"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Pedido | Assunto: Transferência entre Empresas

A funcionalidade de Transferência entre Empresas permite que o diretor ou gestor de aquisições aloque estrategicamente os itens provenientes de uma entrada de nota fiscal entre as diversas empresas que compõem o conglomerado, definindo a quantidade exata de cada item destinada a cada unidade de negócio.

Ao término dessa alocação, o sistema gera automaticamente os pedidos de transferência necessários, especificando a transição dos produtos da loja **"origem"** para as respectivas lojas **"destino"**. Ao concluir o processo dos pedidos de transferência, uma entrada é automaticamente registrada no estoque de cada loja "destino".

**Perguntas frequentes relacionadas:**
- Para que serve a Transferência entre Empresas no Dataweb?
- Como o sistema distribui itens de uma nota fiscal entre lojas diferentes?
- O estoque da loja destino é atualizado automaticamente após a transferência?

**Imagens associadas:** nenhuma.

---

### transferencia-entre-empresas_pedido_gerar-pedido_02

**Metadados:**
```json
{
  "id": "transferencia-entre-empresas_pedido_gerar-pedido_02",
  "manual_origem": "TRANSFERENCIA_ENTRE_EMPRESAS_-_PILULAS_SEMANAIS_V1.pdf",
  "modulo": "Pedido",
  "assunto": "Transferência entre Empresas",
  "subassunto": "Gerar Pedido de Transferência entre Empresas",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerar um pedido de transferência de produtos entre empresas no Dataweb",
  "palavras_chave": ["gerar pedido de transferência", "transferência entre empresas", "loja origem", "loja destino", "módulo pedido"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-3",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Pedido | Assunto: Transferência entre Empresas > Gerar Pedido de Transferência entre Empresas

Como gerar um pedido de transferência de produtos entre empresas a partir de uma nota encerrada:

1. Clique com o botão direito em cima da nota encerrada em que deseja realizar as transferências, vá até o menu **"Mais"** e depois em **"Gerar Pedido de Transferência entre empresas"**.
2. Na tela apresentada, serão mostradas as quantidades disponíveis (presentes naquela nota de entrada) e as empresas para as quais poderão ser transferidas essas peças. Informe as quantidades desejadas para cada loja de destino.
3. Ao clicar em **"Gerar"**, o sistema gera uma transação de saída da loja "origem" para cada uma das lojas "destino". Ao encerrar esses pedidos, serão geradas as transações de entrada (módulo Entradas) nas lojas "destino"; ao serem encerradas, essas transações adicionarão as quantidades de produtos constantes naquela entrada.

**Observação:** para receber esses produtos em seu estoque, cada uma das lojas "destino" deve acessar o **módulo Entradas** e **encerrar a transação de transferência**.

**Perguntas frequentes relacionadas:**
- Como faço para transferir produtos de uma nota fiscal entre lojas diferentes?
- Depois de gerar o pedido de transferência, o que a loja destino precisa fazer para receber os produtos?
- Onde encontro a opção "Gerar Pedido de Transferência entre empresas"?

**Imagens associadas:**
- Figura 1 - "Gerar Pedido de Transferência entre Empresas": lista de notas de entrada encerradas, com uma linha selecionada (marcada como "1"); menu de contexto (botão direito) aberto com opções como Imprimir Conferência, Importação, Solicitação de pagamento, Alterar dados, **Mais** (marcado como "2", expandido) contendo Etiquetas, Recarregar XML da NFe, Análise de preço de Custo e Venda, Manutenção de referência do fornecedor, Consignação > Remover acertos, e **Gerar > Gerar pedido de transferência entre empresas...** (marcado como "3", destacado).
- Figura 2 - "Quantidades e Empresas Disponíveis para Transferência": tela "Transferência de produtos entre empresas a partir da ENF: 6315633", com grade de colunas Código de barras, Produto, Quantidade, Qtd. Transferida e Qtd disponível, seguida de colunas para as lojas de destino ("LOJA 02 - CIRO", "LOJA 03 - LEONARDO", "LOJA 04 - CASSIANO") com campos de quantidade preenchidos (ex.: "1UND") em algumas linhas/colunas; botões **Excel**, **Imprimir**, **Gerar** (destacado) e **Cancelar**.
- Figura 3 - "Transação de Saída Loja Origem": tela "COMMERCIO - Pedido (LOJA 01 - WAGNER)", módulo Pedido, exibindo uma lista de pedidos agrupados em "1. Orçamentos", com três pedidos gerados para LOJA 04 - CASSIANO, LOJA 02 - CIRO e LOJA 03 - LEONARDO, cada um com Nº do pedido, Cliente, Dt.Emissão, Dt.Encerramento e Total.

---

## 3. Glossário

| Termo | Definição (conforme uso no documento) |
|---|---|
| Loja Origem | Loja/empresa a partir da qual os produtos de uma nota de entrada são transferidos para outras lojas do grupo. |
| Loja Destino | Loja/empresa que recebe os produtos transferidos e deve encerrar a transação de transferência no módulo Entradas para atualizar seu estoque. |
| Pedido de Transferência entre Empresas | Documento gerado pelo sistema, a partir de uma nota de entrada encerrada, que formaliza a transferência de produtos de uma loja origem para uma ou mais lojas destino. |
| ENF | Entrada de Nota Fiscal — identificada no exemplo do manual pelo número "6315633", usada como base para a transferência de produtos entre empresas. |

---

## 4. Pontos Sinalizados para Revisão

Nenhum ponto de revisão identificado neste manual — conteúdo completo e sem ambiguidades.
