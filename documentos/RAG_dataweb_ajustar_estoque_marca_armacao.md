# MANUAL 3: Como ajustar o estoque por Marca armação

## Resumo estrutural
- Módulo: **Administrador**
  - Assunto: **Estoque → Inventário (Nova)**
    - Procedimento: Ajuste de saldo de estoque filtrado por Marca de armação

## Chunks

### [ajuste-estoque-marca-armacao_administrador_inventario_01]
**Metadados:**
```json
{
  "id": "ajuste-estoque-marca-armacao_administrador_inventario_01",
  "manual_origem": "Como ajustar o estoque por Marca armação",
  "modulo": "Administrador",
  "assunto": "Estoque",
  "subassunto": "Inventário (Nova) - ajuste por Marca armação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como ajustar o estoque de uma Marca de armação usando a ferramenta de Inventário (Nova)",
  "palavras_chave": ["ajuste de estoque", "inventário", "marca armação", "saldo", "tipo de produto armação"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Administrador — Estoque, ajuste por Marca armação. Para ajustar o estoque de uma Marca armação, deve-se utilizar a ferramenta de **Inventário (Nova)**, disponibilizada no **Módulo Administrador**.

Passo a passo:
1. Acesse o **Módulo Administrador**.
2. Clique em **Estoque → Inventário (Nova)...** — isso abre a tela **"Ajuste de inventário"**.
3. Utilize o campo **"Tipo de produto"** e selecione o tipo **ARMAÇÃO**.
4. Clique em **"Pesquisar (F3)"**.
5. Aguarde a consulta ser concluída.
6. Ao concluir a pesquisa, o sistema apresentará o estoque de armação cadastrado no sistema (lista com colunas como Código de barras, Descrição, Valor de venda, Saldo atual, Saldo novo, Mínimo atual).
7. Utilize o botão de definição de filtro de coluna (ícone ao lado do cabeçalho da grade) e adicione o filtro/coluna **"Armação: Marca armação"** na lista de campos disponíveis (que inclui também opções como "Lente: Fabricante", "Armação: Tipo armação", "Armação: Modelo armação", entre outras).
8. No exemplo do manual, pesquisa-se a marca **FILA**: seleciona-se apenas **"Fila"** na lista de valores da coluna adicionada.
9. Selecione todas ou apenas as armações cujo saldo se deseja alterar. Para selecionar todos os itens, selecione alguns lançamentos e pressione **Ctrl + A**.
10. Clique no botão **"Mais opções"**. Isso abre uma janela com quatro seções: **Saldo**, **Saldo mínimo**, **Saldo máximo** e **O que alterar**.
11. Na seção **Saldo**, marque a opção **"Alterar o saldo para a quantidade"** e informe, no campo ao lado, a quantidade desejada. (As seções "Saldo mínimo" e "Saldo máximo" seguem o mesmo padrão de opções — "Não alterar", "Alterar para a quantidade" ou "Alterar levando em consideração a média mensal de vendas no período" — mas não são o foco deste exemplo. A seção **"O que alterar"** tem as opções **"Somente os selecionados"** e **"Todos os exibidos"**.)
12. Clique em **"Ok"** e aguarde o sistema realizar a alteração.
13. O sistema apresentará a tela com os valores atualizados. Para salvar, clique em **"Gravar ajustes"**.
14. Para fins de registro, informe o seu **usuário** e clique em **"Ok"**.
15. Aguarde as alterações serem salvas.
16. Ajuste de saldo concluído.

**Observações:**
- A tela principal do procedimento é intitulada **"Ajuste de inventário"**.
- A janela aberta pelo botão "Mais opções" tem o título **"Mais opções"** e permite alterar não apenas o saldo atual, mas também saldo mínimo e saldo máximo, além de escolher se a alteração se aplica só aos itens selecionados ou a todos os exibidos na grade.

**Perguntas frequentes relacionadas:**
- Como faço para ajustar o saldo de estoque de uma marca específica de armação?
- Onde encontro a ferramenta de Inventário (Nova) no Dataweb?
- Como aplicar um ajuste de saldo apenas para os itens selecionados na grade de inventário?

**Imagens associadas:**
- Tela **Ajuste de inventário** com o campo **"Tipo de produto"** definido como Armação e a grade de resultados mostrando colunas como Código de barras, Descrição, Valor de venda, Saldo atual/novo e a coluna adicionada **"Armação: Marca armação"**; a lista lateral de campos disponíveis para filtro/coluna também é exibida, com "Armação: Marca armação" marcado.
- Janela **"Mais opções"** com as seções **Saldo** (opção "Alterar o saldo para a quantidade" marcada, valor de exemplo "5"), **Saldo mínimo**, **Saldo máximo** e **"O que alterar"** (com opções "Somente os selecionados" / "Todos os exibidos"), e botão **"Ok"** destacado.

---

## Glossário
- **Inventário (Nova)**: ferramenta do módulo Administrador, em Estoque, usada para consultar e ajustar em lote o saldo de estoque de produtos, com filtros por tipo de produto e outras características (como marca de armação).
- **Ajuste de inventário**: nome da tela onde a pesquisa e o ajuste de saldo são realizados.
- **Mais opções**: janela acionada a partir da tela de Ajuste de inventário, que concentra as opções de alteração de Saldo, Saldo mínimo e Saldo máximo.

## Pontos para revisão
- Nenhum ponto sinalizado como `[REVISAR]` neste manual.
