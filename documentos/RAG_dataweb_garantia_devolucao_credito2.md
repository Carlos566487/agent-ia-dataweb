# Base de Conhecimento RAG: Devolução de Mercadorias (Gerando Crédito ou Não)

## Informações do Documento Original
- **Manual de Origem:** Devolução (gerando crédito ou não).pdf
- **Módulo Principal:** Caixa / Histórico
- **Versão / Referência:** Dataweb Tecnologia - Procedimento Operacional PDV

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Histórico / Módulo Caixa
  - Histórico de Vendas
    - Pesquisa e Localização da Venda
    - Devolução de Mercadorias
      - Decisão de Geração de Crédito para o Cliente (Sim / Não)
      - Tratamento na Tela Sinais (Crédito)
      - Tratamento por Sangria/Retirada do Caixa (Devolução em Dinheiro)
  - Módulo Caixa
    - Aba Devoluções e Atualização de Registros

---

## 2. Chunks Estruturados para RAG

### [devolucao-mercadorias_caixa-historico_procedimento_01]
**Metadados:**
```json
{
  "id": "devolucao-mercadorias_caixa-historico_procedimento_01",
  "manual_origem": "Devolução (gerando crédito ou não).pdf",
  "modulo": "Caixa / Histórico",
  "assunto": "Devoluções",
  "subassunto": "Devolução de Mercadorias e Geração de Crédito",
  "tipo_conteudo": "procedimento",
  "titulo": "Como fazer a devolução de mercadorias com ou sem geração de crédito",
  "palavras_chave": ["devolução de mercadorias", "gerar crédito", "histórico de vendas", "tela sinais", "retirada do caixa"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-2",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Caixa / Histórico > Histórico > Histórico de Vendas > Devolução de Mercadorias.

**Pré-requisitos:** Venda original localizada no sistema e produtos a serem devolvidos.

**Passo a passo:**
1. Acesse o menu superior `Histórico` e clique em `Histórico de Vendas` para abrir a janela "Pesquisa de venda por cupom fiscal".
2. Informe os filtros (como período, empresa ou cliente) e localize a venda desejada na lista de resultados.
3. Clique com o botão direito do mouse sobre a linha da venda selecionada.
4. No menu de contexto exibido, selecione a opção `Devolução de mercadorias...`.
5. O sistema exibirá uma caixa de diálogo de confirmação com a pergunta: *"Deseja gerar um crédito no valor desta devolução? Dessa forma o cliente poderá utilizar esse valor posteriormente."*
6. Escolha a opção de acordo com o destino financeiro acordado com o cliente:
   - **Selecione `Sim`:** o sistema gerará um saldo de crédito para o cliente, que ficará disponível para consulta e abatimento futuro na tela `Sinais`.
   - **Selecione `Não`:** escolha esta opção caso o cliente deseje receber o reembolso do dinheiro de volta imediatamente; em seguida, realize manualmente uma operação de retirada (sangria) no caixa para efetuar o pagamento ao cliente.
7. Para conferir os lançamentos processados, acesse a aba `Devoluções` dentro do módulo `Caixa`.
8. Caso o registro de devolução recém-executado não apareça imediatamente na lista, clique no botão `Atualizar` [REVISAR: as aspas do texto original terminam sem fechar: `clique em "Atualizar`].

**Perguntas frequentes relacionadas:**
- Como fazer uma devolução de venda no Dataweb?
- Onde fica o crédito do cliente gerado a partir de uma devolução?
- O que fazer se o cliente quiser receber o dinheiro de volta na devolução em vez de crédito?
- Onde consultar as devoluções já realizadas no módulo Caixa?

**Imagens associadas:**
- Imagem 1: Janela "Pesquisa de venda por cupom fiscal" com os critérios de busca à esquerda e o menu de contexto aberto pelo clique direito sobre a venda, destacando a opção `Devolução de mercadorias...` entre "Dados da venda..." e "Exibir produtos da venda".
- Imagem 2: Caixa de diálogo do sistema intitulada "Confirmar", contendo o ícone informativo azul, o texto *"Deseja gerar um crédito no valor desta devolução? Dessa forma o cliente poderá utilizar esse valor posteriormente."* e os botões `Sim` e `Não`.

---

## 3. Glossário do Manual
- **Devolução de mercadorias:** Operação de estorno da venda que retorna o item ao inventário e ajusta o saldo financeiro da transação.
- **Crédito de devolução:** Valor monetário vinculado ao cadastro do cliente resultante de uma devolução, permitindo utilização em compras posteriores.
- **Tela Sinais:** Interface do sistema Dataweb onde constam os adiantamentos e créditos acumulados de clientes para compensação em pagamentos.
- **Retirada do caixa:** Operação manual de saída de numerário físico (sangria) efetuada no módulo Caixa para devolver valores em espécie ao consumidor.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 2:** O texto final apresenta erro tipográfico de pontuação no fechamento de aspas: *"clique em "Atualizar"* (sem fechar as aspas e sem ponto final).