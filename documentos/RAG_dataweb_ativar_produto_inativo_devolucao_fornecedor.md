# MANUAL 1: Ativar produto inativo para emitir nota de devolução para fornecedor

## Resumo estrutural
- Módulo: **Pedidos**
  - Assunto: Ativação/desativação de produtos inativos para devolução ao fornecedor
    - Procedimento: Reativar produto inativo via Manutenção em lote de dados cadastrais
    - Procedimento: Desativar produto após concluir a devolução

## Chunks

### [ativar-produto-inativo-devolucao_pedidos_ativacao_01]
**Metadados:**
```json
{
  "id": "ativar-produto-inativo-devolucao_pedidos_ativacao_01",
  "manual_origem": "Ativar produto inativo para emitir nota de devolução para fornecedor",
  "modulo": "Pedidos",
  "assunto": "Ativação de produto inativo",
  "subassunto": "Nota de devolução para fornecedor",
  "tipo_conteudo": "procedimento",
  "titulo": "Como ativar um produto inativo para incluí-lo em uma nota de devolução para o fornecedor",
  "palavras_chave": ["produto inativo", "devolução fornecedor", "ativar selecionados", "manutenção em lote", "lente"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Pedidos — Ativação de produto inativo. Para realizar uma nota de devolução para o fornecedor quando o produto estiver inativo, utiliza-se o módulo **Pedidos** para reativar o item e incluí-lo na nota. O exemplo do manual usa uma **lente**, mas o procedimento de reativação em lote se aplica à busca de produtos em geral.

Passo a passo:
1. Acesse o módulo **Pedidos**.
2. Acesse o menu **Cadastro → Lentes → Manutenção em lote de dados cadastrais**.
3. Na tela **Pesquisa de lentes** que se abre, selecione a opção **(...)** ao lado do campo de descrição/código para facilitar a busca. Essa função permite localizar todos os produtos que contenham as palavras informadas.
4. Com a opção **Contendo** selecionada, digite a **descrição** ou o **código** da lente.
5. Como o produto está inativo, ele **não aparecerá na busca padrão**. Para incluí-lo na busca, marque a opção **Critérios avançados → Ativos e inativos** (esse critério fica na seção "Pesquisar produtos de acordo com sua situação no banco de dados", que também tem as opções "Apenas ativos" e "Apenas inativos").
6. Com as opções marcadas, pressione **F3** no teclado ou clique em **Pesquisar (F3)**.
7. Após localizar a lente desejada, **selecione-a** marcando o quadradinho (checkbox) ao lado do item na lista de resultados, **clique com o botão direito do mouse** e escolha a opção **Ativar selecionados** no menu de contexto.
8. Com o produto reativado, é possível adicioná-lo ao pedido e prosseguir com a **devolução para o fornecedor**.
9. Concluída a devolução, o produto deve ser **inativado novamente**: repita os passos 2 a 6 para localizá-lo e, no menu de contexto (botão direito), selecione a opção **Desativar selecionados**.

**Observações:**
- O critério "Ativos e inativos" é indispensável para que um produto inativo apareça no resultado de busca — sem ele a pesquisa retorna vazia para itens inativos.
- O produto deve ser reinativado ao final do processo; o manual reforça esse passo como parte do fluxo padrão, não como opcional.

**Perguntas frequentes relacionadas:**
- Como faço para emitir uma nota de devolução de um produto que está inativo no sistema?
- Por que um produto inativo não aparece na busca do módulo Pedidos?
- Como reativar temporariamente uma lente para incluí-la em uma devolução ao fornecedor?

**Imagens associadas:**
- Tela **Pesquisa de lentes** com o menu **Critérios avançados** expandido, destacando com seta vermelha a opção **"Ativos e inativos"** marcada (junto de outros critérios como "Pode ou não ser vendido" e "Pode ou não possuir imagem por URL").
- Tela **Pesquisa de lentes** com um item selecionado (checkbox marcado) e o menu de contexto do botão direito do mouse aberto, com a opção **"Ativar selecionados"** destacada em azul (o menu também mostra outras opções como "Manutenção em lote", "Desativar selecionados", "Transações do produto...", "Família — chave da lente (F5)").

---

## Glossário
- **Manutenção em lote de dados cadastrais**: ferramenta que permite selecionar múltiplos produtos e alterar seus dados cadastrais (ex.: status ativo/inativo) de uma só vez.
- **Critérios avançados**: seção de filtros extras da tela de pesquisa, usada, entre outras coisas, para incluir produtos inativos na busca.
- **Ativar selecionados / Desativar selecionados**: comandos do menu de contexto (botão direito do mouse) que alteram o status ativo/inativo dos itens marcados.

## Pontos para revisão
- Nenhum ponto sinalizado como `[REVISAR]` neste manual.
