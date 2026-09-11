# MANUAL 8: Manual Monitor de Produção

## Resumo estrutural
- Módulo: **Caixa** (Ordem de serviço) / **Estoque** / **Laboratório**
  - Assunto: **Monitor de produção** — acompanhamento do ciclo de vida da Ordem de Serviço (O.S.)
    - Subassunto: Acesso ao Monitor de produção
    - Subassunto: Etapa Loja — Venda concluída e serviço na loja
    - Subassunto: Etapa Loja — Translado loja → estoque (e opções alternativas)
    - Subassunto: Etapa Estoque — Recebimento e opções de movimentação
    - Subassunto: Etapa Laboratório — Recebimento e opções de movimentação
    - Subassunto: Etapa final — Recebimento na loja e entrega ao cliente

## Chunks

### [monitor-producao_caixa_acesso-conceito_01]
**Metadados:**
```json
{
  "id": "monitor-producao_caixa_acesso-conceito_01",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Caixa",
  "assunto": "Monitor de produção",
  "subassunto": "Conceito e acesso",
  "tipo_conteudo": "procedimento",
  "titulo": "O que é e como acessar o Monitor de produção",
  "palavras_chave": ["monitor de produção", "ordem de serviço", "caixa aberto", "acesso"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa — Monitor de produção, conceito e acesso. Através da ferramenta **Monitor de produção** é possível realizar todo o processo das Ordens de serviço na Ótica, desde a entrada da O.S. (Ordem de serviço) na loja até a retirada do óculos pronto pelo cliente.

**Pré-requisito:** para acessar o Monitor de produção é necessário estar com o **Caixa aberto**.

Passo a passo para acessar:
1. Clique na aba **Ordem de serviço** e, em seguida, na aba **Monitor de produção**.
2. Toda O.S. (Ordem de Serviço) aparece automaticamente na tela de monitor de produção, listada uma abaixo da outra.
3. Na tela do Monitor de produção é possível pesquisar pelo **número da Ordem de Serviço** ou pelo **nome do cliente**, e também selecionar a exibição a partir de uma **data pré-definida** pelo usuário.

**Observações:**
- A movimentação da O.S. dentro do Monitor de produção é sempre feita clicando com o **botão direito do mouse** sobre a O.S. e escolhendo a opção desejada no menu de contexto (detalhado nos próximos chunks deste manual).

**Perguntas frequentes relacionadas:**
- O que é o Monitor de produção no Dataweb?
- É necessário algo para acessar o Monitor de produção?
- Como pesquisar uma Ordem de Serviço específica no Monitor de produção?

**Imagens associadas:**
- Tela do módulo **Caixa**, com o menu superior (Acesso, Cadastro, Pesquisas, Relatórios e Gráficos, Caixa, Ordem de serviço, Históricos, Receitas(RX), Ferramentas, Estoque, Menu fiscal, TEF, Configurações, Ajuda) e, no menu lateral esquerdo, as abas **"Ordens de serviço"** e **"Monitor de produção"** destacadas em vermelho; a área central mostra os filtros de situação, tipo de data, período e nome do cliente, além da lista de O.S. em aberto com colunas Nº O.S., Cliente, Dt. Emissão, Dt. Previsão, entre outras.
- Tela do **Monitor de produção**, com os campos **"Número da O.S."**, **"Nome do cliente"** e **"Exibir apenas O.S. com data a partir de"** destacados em vermelho, e a grade abaixo listando as O.S. agrupadas pela etapa **"Etapa inicial"**, com colunas Nº O.S., Empresa, Dt. Emissão, Dias, Dt. Previsão, Dt. previsão Lab. e Nº externo.

---

### [monitor-producao_caixa_venda-concluida-loja_02]
**Metadados:**
```json
{
  "id": "monitor-producao_caixa_venda-concluida-loja_02",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Caixa",
  "assunto": "Monitor de produção",
  "subassunto": "Etapa Loja - Venda concluída",
  "tipo_conteudo": "procedimento",
  "titulo": "Como registrar no Monitor de produção que a venda foi concluída e o serviço está na loja",
  "palavras_chave": ["venda concluída e serviço na loja", "monitor de produção", "botão direito", "observação da O.S."],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa — Monitor de produção, etapa Loja: venda concluída. Para realizar a movimentação das ordens de serviço, deve-se clicar com o **botão direito do mouse** na Ordem de serviço e selecionar a opção desejada no menu de contexto. Assim que o vendedor registra a Ordem de serviço e conclui a venda, é necessário informar no Monitor de produção que a venda foi concluída e o serviço está na loja.

Passo a passo:
1. Clique com o botão direito na O.S. desejada.
2. Selecione a opção **"Venda concluída e serviço na loja"** (dentro da seção "Loja" do menu de contexto).
3. Uma nova janela ("Dados da Ordem de Serviço: [número]") é aberta, onde é possível inserir alguma **Observação** para quem consultar a O.S. visualizar.
4. Clique no botão **"OK"** para confirmar que a venda está na loja.

Ao concluir esse passo, qualquer pessoa que consultar essa ordem de serviço saberá que ela está na loja, aguardando o momento de ir para o Estoque/Laboratório; o ícone/etapa da Ordem de serviço passa a exibir **"Venda concluída e serviço na loja"**.

**Observações:**
- A janela "Dados da Ordem de Serviço" que se abre neste passo é a mesma usada em outras transições de etapa ao longo do fluxo (mencionada novamente nos passos seguintes deste manual), contendo campos como Observação, Número O.S. externo/Envelope, Motivo, Nova Data/Hora de previsão para o cliente, Fornecedor, Caixa/Bandeja, Lentes OD e OE, e a opção de Gerar remessa para industrialização.

**Perguntas frequentes relacionadas:**
- Como informo no sistema que a venda de uma O.S. foi concluída e o produto está na loja?
- Onde fica a opção "Venda concluída e serviço na loja" no Monitor de produção?
- Para que serve o campo Observação ao mudar a etapa de uma O.S.?

**Imagens associadas:**
- Tela do **Monitor de produção** com o menu de contexto do botão direito do mouse aberto sobre uma O.S., mostrando a seção **"Loja"** com a opção **"Venda concluída e serviço na loja"** destacada em vermelho, seguida de outras opções da mesma seção como "Translado loja - estoque", "Translado loja (pós venda) -> estoque", "Ordem de serviço entregue ao cliente", "O.S. devolvida pelo cliente", "Armação enviada pela loja para montagem", "Ordem de serviço recebida do laboratório", "Devolver para o laboratório", e abaixo as seções "Estoque" e "Laboratório" (com itens esmaecidos/indisponíveis nesta etapa).
- Janela **"Dados da Ordem de Serviço: [número]"**, com o campo **Observação** em destaque (texto de exemplo: "POSSIVEL INSERIR QUALQUER INFORMAÇÃO RELEVANTE PARA VENDEDORES/ESTOQUE/LABORATÓRIO"), campos Número O.S. externo/Envelope, Motivo, Nova Data/Hora de previsão para o cliente, Fornecedor, Caixa/Bandeja, Lentes OD e OE, botão "Gerar Ordem de compra", opção "Gerar remessa para industrialização", e botão **"OK"** destacado.

---

### [monitor-producao_caixa_translado-loja-estoque_03]
**Metadados:**
```json
{
  "id": "monitor-producao_caixa_translado-loja-estoque_03",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Caixa",
  "assunto": "Monitor de produção",
  "subassunto": "Etapa Loja - Translado para o estoque",
  "tipo_conteudo": "procedimento",
  "titulo": "Como enviar a Ordem de Serviço da loja para o estoque (Translado loja - estoque)",
  "palavras_chave": ["translado loja estoque", "ordem de serviço entregue ao cliente", "ordem de serviço cancelada", "monitor de produção"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa — Monitor de produção, etapa Loja: envio para o estoque. Quando a Ordem de serviço for enviada para o Estoque, é necessário informar isso no Monitor de produção.

Passo a passo:
1. Clique novamente com o botão direito do mouse na Ordem de Serviço (já na etapa "Venda concluída e serviço na loja").
2. Clique na opção **"Translado loja – estoque"**.
3. Assim como no passo anterior, será aberta a mesma tela de **"Dados da Ordem de Serviço"**, onde é possível inserir alguma observação para quem consultar a O.S. visualizar. Clique em **"OK"** para passar para o passo seguinte.

Repare que, a cada mudança de etapa, apenas as opções possíveis para a **próxima etapa** ficam disponíveis no menu de contexto.

**Fluxos alternativos (quando não há necessidade de enviar a O.S. para o Estoque/Laboratório):**
- **"Ordem de serviço entregue ao cliente"**: usada quando o produto já pode ser entregue diretamente ao cliente sem passar por Estoque/Laboratório.
- **"Ordem de serviço Cancelada"**: usada para cancelar a O.S.

Após o translado, o ícone/etapa da Ordem de serviço passa a exibir **"Translado estoque -> Loja"**, e a partir desse momento o **ESTOQUE** deve informar o recebimento da O.S. (procedimento detalhado no próximo chunk deste manual).

**Observações:**
- As opções do menu de contexto se adaptam à etapa atual da O.S. — nem todas as opções ficam sempre habilitadas, apenas as compatíveis com a próxima movimentação possível.

**Perguntas frequentes relacionadas:**
- Como envio uma Ordem de Serviço da loja para o estoque no Monitor de produção?
- É possível entregar a O.S. ao cliente sem passar pelo estoque ou laboratório?
- Como cancelo uma Ordem de Serviço no Monitor de produção?

**Imagens associadas:**
- Tela do **Monitor de produção** com o menu de contexto do botão direito aberto sobre uma O.S. já na etapa "Venda concluída e serviço na loja", exibindo a seção **"Loja"** com a opção **"Translado loja - estoque"** destacada em vermelho, além de "Translado loja (pós-venda) -> estoque", **"Ordem de serviço entregue ao cliente"**, **"Ordem de serviço cancelada"**, "O.S. devolvida pelo cliente", "Armação enviada pela loja para montagem", "Ordem de serviço recebida do laboratório", "Devolver para o laboratório", seguidas das seções **"Estoque"** (com "Ordem de serviço no estoque", "Devolver Estoque -> Loja", "Aguardando compra de lentes", "O.S. em tratamento externo", "Translado estoque -> laboratório", "Serviço forçar finalização") e **"Laboratório"**.
- Janela **"Dados da Ordem de Serviço: [número]"** (mesma estrutura de tela mostrada no chunk anterior), com o botão **"OK"** destacado.

---

### [monitor-producao_estoque_recebimento-opcoes_04]
**Metadados:**
```json
{
  "id": "monitor-producao_estoque_recebimento-opcoes_04",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Estoque",
  "assunto": "Monitor de produção",
  "subassunto": "Etapa Estoque - Recebimento e movimentação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como o Estoque recebe a Ordem de Serviço e quais são as opções de movimentação disponíveis",
  "palavras_chave": ["ordem de serviço no estoque", "devolver estoque loja", "aguardando compra da lente", "tratamento externo", "translado estoque laboratório", "serviço forçar finalização"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3",
  "revisar": false
}
```

**Conteúdo:**
Módulo Estoque — Monitor de produção, etapa Estoque. Para receber a O.S. no estoque, o operador do estoque deve clicar com o **botão direito do mouse** na Ordem de serviço e selecionar a opção **"Ordem de Serviço no Estoque"**.

Depois de informado que a O.S. chegou no estoque, é necessário informar o que será feito com essa O.S. O sistema habilita **5 opções**:
1. **Devolver estoque -> Loja**: usada caso esteja faltando alguma informação da loja.
2. **Aguardando compra da Lente**: usada quando o estoque ainda vai solicitar a compra das lentes. Quando utilizada, a O.S. permanecerá no estoque. Nesse caso, é possível adicionar as lentes na tela de Dados da Ordem de serviço (campos **Lente OD** e **Lente OE**) e solicitar a geração de ordem de compra através do botão **"Gerar Ordem de compra"**.
3. **O.S. em tratamento externo**: usada quando a O.S. é enviada para algum serviço fora da loja (ex.: montagem). Quando utilizada, a O.S. permanecerá no estoque.
4. **Translado estoque laboratório**: usada quando o estoque envia a O.S. para o laboratório.
5. **Serviço forçar finalização**: usada quando não há nada a fazer na Ordem de serviço, nem no estoque, nem no laboratório. Após selecionar esta opção, somente fica habilitada a opção 1 (**Devolver estoque -> Loja**).

Em todas as opções acima, o sistema abre a tela de **Dados da O.S.** para inserir qualquer informação adicional.

**Regra de saída do Estoque:**
A O.S. sai do Estoque quando o operador seleciona uma das seguintes opções: **"Translado estoque -> laboratório"**, **"Devolver estoque -> Loja"** ou **"Serviço forçar finalização"**.
- Caso opte por enviar para o laboratório, é necessário que o **Laboratório realize o recebimento** da Ordem de serviço.
- Caso a loja **não tenha laboratório próprio**, este passo (recebimento no laboratório) deve ser realizado pelo próprio Estoque ou por quem realiza a movimentação na loja.
- Para receber a O.S. no laboratório, basta clicar com o botão direito do mouse na O.S. e ir na opção **"Ordem de serviço no laboratório"** (detalhado no próximo chunk deste manual).

**Observações:**
- As opções 2 (Aguardando compra da Lente) e 3 (O.S. em tratamento externo) mantêm a O.S. no estoque, ou seja, não a movem para outra etapa até uma ação de saída ser executada.

**Perguntas frequentes relacionadas:**
- Quais opções o estoque tem para movimentar uma O.S. que acabou de chegar?
- Como o estoque solicita a compra de uma lente pendente para uma O.S.?
- O que acontece se a loja não tiver laboratório próprio ao enviar uma O.S. para tratamento?
- Como faço para devolver uma O.S. do estoque para a loja?

**Imagens associadas:**
- Menu de contexto do botão direito do mouse sobre uma O.S. em etapa "Translado loja -> [estoque]", mostrando as seções "Loja" (esmaecida/indisponível) e **"Estoque"** com a opção **"Ordem de Serviço no Estoque"** destacada em vermelho, seguida de "Devolver Estoque -> Loja", "Aguardando compra de lentes", "O.S. em tratamento externo", "Translado estoque -> laboratório", "Serviço forçar finalização", e a seção "Laboratório" abaixo.
- Janela **"Dados da Ordem de Serviço"** com os campos **Lente OD** e **Lente OE** preenchidos (ex.: "LG ACCESS 1.49 RES AR") destacados em vermelho, e o botão **"Gerar Ordem de compra"** ao lado.

---

### [monitor-producao_laboratorio_recebimento-opcoes_05]
**Metadados:**
```json
{
  "id": "monitor-producao_laboratorio_recebimento-opcoes_05",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Laboratório",
  "assunto": "Monitor de produção",
  "subassunto": "Etapa Laboratório - Recebimento e movimentação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como o Laboratório recebe a Ordem de Serviço e quais são as opções de movimentação disponíveis",
  "palavras_chave": ["ordem de serviço no laboratório", "aguardando armação para montagem", "O.S. devolvida para tratamento", "translado laboratório loja", "translado laboratório estoque"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4",
  "revisar": false
}
```

**Conteúdo:**
Módulo Laboratório — Monitor de produção, etapa Laboratório. Para receber a O.S. no laboratório, clique com o botão direito do mouse na O.S. e selecione a opção **"Ordem de serviço no laboratório"**.

Com a Ordem de serviço no laboratório, ao clicar com o botão direito na O.S. o sistema habilita **4 opções**:
1. **Aguardando armação para montagem**: quando selecionada, a O.S. permanece no laboratório.
2. **O.S. devolvida para tratamento**: nesse caso será necessário inserir um **Motivo**, que deve ser cadastrado previamente (campo "Motivo" na tela de Dados da Ordem de Serviço).
3. **Translado laboratório -> loja**: usada quando o laboratório envia direto para a loja. Nesse caso é necessário inserir uma **Observação** do laboratório informando que o serviço foi concluído (ex.: "Serviço concluído").
4. **Translado laboratório – Estoque**: usada quando é necessário devolver ao estoque. Nesse caso é necessário que o estoque realize a entrada novamente da O.S., conforme o procedimento de recebimento no estoque descrito neste manual, e repita os processos seguintes.

Em todas as opções acima, o sistema abre a tela de **Dados da O.S.** para inserir qualquer informação.

**Observações:**
- O campo **Motivo**, exigido na opção "O.S. devolvida para tratamento", deve estar previamente cadastrado no sistema.

**Perguntas frequentes relacionadas:**
- Quais opções o laboratório tem ao receber uma O.S.?
- Como devolvo uma O.S. do laboratório para tratamento?
- O laboratório pode enviar a O.S. direto para a loja, sem passar pelo estoque?
- Como devolvo uma O.S. do laboratório para o estoque?

**Imagens associadas:**
- Menu de contexto do botão direito do mouse com a seção **"Laboratório"** exibindo a opção **"Ordem de serviço no laboratório"** destacada em azul, junto às seções "Loja" e "Estoque" (esmaecidas/indisponíveis nessa etapa), e abaixo, já com a O.S. no laboratório, as opções "Aguardando armação para montagem", "O.S. devolvida para tratamento", "Translado laboratório -> loja", "Translado laboratório -> Estoque".
- Janela **"Dados da Ordem de Serviço"** com o campo **Motivo** destacado em vermelho e em amarelo (indicando campo obrigatório/ativo), definido como "(Nenhuma)" por padrão (a ser selecionado a partir de uma lista pré-cadastrada).
- Janela **"Dados da Ordem de Serviço"** com o campo **Observação** destacado em vermelho e preenchido com o texto de exemplo "Serviço concluído".

---

### [monitor-producao_caixa_recebimento-final-entrega_06]
**Metadados:**
```json
{
  "id": "monitor-producao_caixa_recebimento-final-entrega_06",
  "manual_origem": "Manual Monitor de Produção",
  "modulo": "Caixa",
  "assunto": "Monitor de produção",
  "subassunto": "Etapa final - Recebimento na loja e entrega ao cliente",
  "tipo_conteudo": "procedimento",
  "titulo": "Como registrar o recebimento da O.S. vinda do laboratório e finalizar a entrega ao cliente",
  "palavras_chave": ["ordem de serviço entregue ao cliente", "ordem de serviço recebida do laboratório", "devolver para o laboratório", "monitor de produção"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa — Monitor de produção, etapa final: recebimento na loja e entrega. Quando o operador do laboratório enviar a O.S. para a loja, o vendedor que receber a Ordem de serviço deve realizar o recebimento da O.S. no Monitor de produção.

Ao clicar com o botão direito na Ordem de serviço nesta etapa, o sistema habilita apenas **3 opções**:
1. **Ordem de serviço entregue ao cliente**: informa que a O.S. já foi entregue.
2. **Ordem de serviço recebida do laboratório**: confirma o recebimento da O.S. vinda do laboratório.
3. **Devolver para o Laboratório**: usada caso tenha sido constatado algum problema e o Laboratório precise ser acionado novamente.

Ao selecionar a opção **"Ordem de serviço entregue ao cliente"**, estará finalizada toda a operação da O.S. no sistema.

**Perguntas frequentes relacionadas:**
- Como confirmo no sistema que a O.S. voltou do laboratório para a loja?
- Como finalizo a entrega de uma O.S. ao cliente no Monitor de produção?
- O que fazer se o produto voltar do laboratório com algum problema?

**Imagens associadas:** nenhuma (procedimento descrito apenas em texto no manual, sem captura de tela associada a este passo específico).

---

## Glossário
- **Monitor de produção**: ferramenta do módulo Caixa que permite acompanhar e movimentar o ciclo de vida completo de uma Ordem de Serviço, da entrada na loja até a entrega ao cliente.
- **O.S. (Ordem de Serviço)**: registro de venda/pedido de óculos que percorre as etapas Loja → Estoque → Laboratório → Loja → Cliente.
- **Translado**: movimentação da O.S. entre etapas/setores (ex.: "Translado loja - estoque", "Translado laboratório - Estoque").
- **Serviço forçar finalização**: opção usada no Estoque quando não há mais nada a fazer com a O.S. nem no estoque nem no laboratório, liberando apenas a devolução para a loja.
- **Motivo**: campo obrigatório, previamente cadastrado no sistema, usado ao devolver uma O.S. do laboratório para tratamento.

## Pontos para revisão
- Nenhum ponto sinalizado como `[REVISAR]` neste manual.
