# MANUAL 6: [Manutenção em lote de dados cadastrais] — Definir lentes para não movimentar estoque

## Resumo estrutural
- Módulo: **Administrador**
  - Assunto: **Cadastro → Lentes → Manutenção em lote de dados cadastrais**
    - Procedimento: Definir que lentes selecionadas não movimentem mais estoque

## Chunks

### [definir-lentes-nao-movimentar-estoque_administrador_manutencao-lote_01]
**Metadados:**
```json
{
  "id": "definir-lentes-nao-movimentar-estoque_administrador_manutencao-lote_01",
  "manual_origem": "[Manutenção em lote de dados cadastrais] - Definir lentes para não movimentar estoque",
  "modulo": "Administrador",
  "assunto": "Manutenção em lote de dados cadastrais",
  "subassunto": "Lentes que não movimentam estoque",
  "tipo_conteudo": "procedimento",
  "titulo": "Como definir que lentes não movimentem mais estoque",
  "palavras_chave": ["lentes", "movimenta estoque", "manutenção em lote", "não movimentar estoque", "informações tributárias"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Administrador — Manutenção em lote de dados cadastrais, lentes sem movimentação de estoque. Para definir que determinadas lentes não movimentem mais estoque, utiliza-se a ferramenta de **manutenção em lote de dados cadastrais**.

Passo a passo:
1. Abra o **Módulo Administrador**.
2. Acesse **Cadastro → Lentes → Manutenção em lote de dados cadastrais...** — isso abre a tela **"Pesquisa de lentes"**.
3. Adicione algum parâmetro para realizar a pesquisa (no exemplo do manual, utiliza-se **"LT"** no campo de descrição). Para selecionar todos os resultados, pode-se usar **Ctrl + A** ou o botão direito do mouse → **Selecionar todos**. Caso deseje alterar apenas itens específicos, selecione somente os itens desejados (marcando os checkboxes correspondentes).
4. Após selecionar os itens, clique com o **botão direito do mouse** e escolha a opção **Manutenção em lote** no menu de contexto.
5. Na janela **"Manutenção do cadastro de lentes (N selecionados)"** que se abre — onde N é a quantidade de itens selecionados —, na seção **"Informações tributárias"**, **desmarque o campo "Movimenta estoque"**.
6. Após a alteração, clique em **"Ok"** para confirmar.

Resultado: os itens selecionados e alterados não irão mais movimentar estoque.

**Observações:**
- A janela de Manutenção do cadastro de lentes também apresenta outros campos na seção Informações tributárias (NCM, Grupo fiscal, Origem da mercadoria, Venda, Insumo, Fornecedor principal, Local de estoque, Índice de refração, Curva base, Diâmetro), mas apenas o campo **"Movimenta estoque"** precisa ser alterado (desmarcado) para este procedimento específico; os demais campos podem ser mantidos como **"Não alterar"**.
- O título da janela confirma quantos itens foram selecionados para a alteração em lote — é recomendável conferir esse número antes de confirmar.

**Perguntas frequentes relacionadas:**
- Como impedir que uma lente movimente o estoque do sistema?
- Onde fica o campo "Movimenta estoque" no cadastro de lentes?
- Como aplicar a alteração de "não movimentar estoque" em várias lentes ao mesmo tempo?

**Imagens associadas:**
- Tela **"Pesquisa de lentes"** com itens selecionados (checkboxes marcados) e o menu de contexto do botão direito do mouse aberto, com a opção **"Manutenção em lote"** destacada em vermelho.
- Janela **"Manutenção do cadastro de lentes (4 selecionados)"** (exemplo com 4 itens), seção **"Informações tributárias"**, com o checkbox **"Movimenta estoque"** destacado e anotações indicando: verificar quantos itens foram selecionados, desmarcar o campo "Movimenta estoque", e clicar em "Ok" após a alteração; também exibe outros campos como NCM, Grupo fiscal, Origem da mercadoria, Venda, Insumo, Fornecedor principal, Local de estoque, Índice de refração, Curva base e Diâmetro (todos configuráveis como "Não alterar" quando não fazem parte da alteração desejada).

---

## Glossário
- **Movimenta estoque**: campo (checkbox) do cadastro de lentes que determina se a venda/uso do item gera movimentação no controle de estoque. Quando desmarcado, o item deixa de afetar o saldo de estoque.
- **Manutenção em lote**: opção do menu de contexto que abre a janela de edição em massa dos dados cadastrais dos itens selecionados.
- **Informações tributárias**: seção da janela de manutenção do cadastro de lentes que reúne campos fiscais e de estoque, incluindo o campo "Movimenta estoque".

## Pontos para revisão
- Nenhum ponto sinalizado como `[REVISAR]` neste manual.
