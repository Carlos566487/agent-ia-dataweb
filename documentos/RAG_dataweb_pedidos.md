# Base de Conhecimento RAG: Pedidos (Convencional e Manual)

## Informações do Documento Original
- **Manual de Origem:** Pedidos.pdf
- **Módulo Principal:** Pedidos / Faturamento
- **Subtítulo:** Guia Rápido - Dataweb Tecnologia
- **Desenvolvedor do Sistema:** Dataweb Tecnologia (Inteligência e Gestão Digital)

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Pedidos
  - Visão Geral das Transações de Saída e Consignação
  - Pedido Convencional
    - Cabeçalho e Dados Principais (Vendedor, Cliente/Fornecedor, Natureza de Operação)
    - Informações Complementares, Transporte e Observações
    - Inclusão de Produtos (Adicionar F8 e Adicionar Múltiplos)
    - Documento Fiscal Referenciado (Devolução e CFOP 5.929 / 6.929)
    - Status e Situações do Pedido (Gravar, Aprovar e Encerrar)
    - Encerramento do Pedido e Emissão da Nota Fiscal
    - Ícones de Status da Nota Fiscal e Ações (DANFE, Cancelamento e Rejeição)
  - Pedido Manual
    - Finalidade Tributária (Destaque de ICMS no Simples Nacional / CSOSN 0900)
    - Preenchimento dos Dados Tributários por Item e Totais da Nota

---

## 2. Chunks Estruturados para RAG

### [pedidos_saida_conceito_01]
**Metadados:**
```json
{
  "id": "pedidos_saida_conceito_01",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Transações de Saída",
  "subassunto": "Visão Geral e Diferença entre Pedido Convencional e Manual",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral do módulo de Pedidos e diferenças entre pedido convencional e manual",
  "palavras_chave": ["pedidos", "transações de saída", "natureza de operação", "consignação", "pedido manual", "pedido convencional"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Transações de Saída.

O módulo de Pedidos do sistema Dataweb tem como finalidade operacional realizar transações de saída de mercadorias, permitindo vincular a natureza de operação (CFOP) adequada a cada movimentação e realizar o controle de processos de consignação.

**Diferença entre os tipos de pedido:**
- **Pedido Convencional:** Utilizado para as operações comerciais cotidianas de venda, remessa ou devolução, onde o cálculo dos impostos e totais é realizado de forma automatizada com base nas configurações prévias cadastradas no sistema.
- **Pedido Manual:** Permite que as informações fiscais, alíquotas e totais sejam preenchidos diretamente pelo usuário. É empregado em situações em que a tributação do pedido difere do padrão cadastrado na empresa (por exemplo, quando uma empresa do Simples Nacional precisa realizar o destaque excepcional de ICMS/IPI utilizando a CSOSN 0900).

**Perguntas frequentes relacionadas:**
- Para que serve o módulo de Pedidos no Dataweb?
- Qual a diferença entre emitir um pedido convencional e um pedido manual?
- É possível controlar mercadorias em consignação pelo módulo de Pedidos?

**Imagens associadas:** nenhuma

---

### [pedidos_saida_convencional_02]
**Metadados:**
```json
{
  "id": "pedidos_saida_convencional_02",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Emissão de Pedidos",
  "subassunto": "Emissão de Pedido Convencional",
  "tipo_conteudo": "procedimento",
  "titulo": "Como emitir um pedido convencional e adicionar produtos no Dataweb",
  "palavras_chave": ["pedido convencional", "adicionar produto", "f8", "adicionar múltiplos", "vendedor", "natureza de operação"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Pedido Convencional.

**Pré-requisitos:** Clientes/fornecedores cadastrados, produtos com saldo em estoque e naturezas de operação configuradas.

**Passo a passo:**
1. No canto superior direito da janela do módulo Pedidos, clique no botão `Pedido`.
2. Preencha os campos obrigatórios do cabeçalho:
   - `Vendedor`: selecione o colaborador responsável;
   - `Fornecedor / Cliente`: informe a entidade de destino da saída;
   - `Natureza de Operação`: selecione a operação fiscal correspondente (CFOP).
3. Preencha os campos opcionais (utilize apenas se aplicável à operação):
   - `Transportadora`, `Valor de frete`, `Despesas`, `Tipos de frete`, `Tipos de expedição`, `Documento` e `Desconto geral`.
4. Preencha os campos de texto descritivo:
   - `Observações`: texto exibido exclusivamente na impressão do espelho do pedido;
   - `Observações para NF`: informações fiscais que constarão no campo "Dados Adicionais" da Nota Fiscal.
5. Para incluir mercadorias no pedido:
   - Clique em `Adicionar (F8)`: abre a tela de inserção individual de produto (`Produto:`, `Estoque`, `Quantidade`, `Unidade`, `CFOP`, `Valor unitário`, `Desconto` com opção `% (F2)` e atalho `F6: Alterar forma de desconto`, `Base cálculo ICMS`, `Aliq. ICMS`, `Aliq. IPI`, `Total ICMS`, `Comissão do vendedor`), confirmando em `Ok`;
   - Ou clique em `Adicionar múltiplos`: insere automaticamente no pedido a quantidade total disponível em estoque dos produtos selecionados.

**Perguntas frequentes relacionadas:**
- Onde fica a opção para criar um novo pedido convencional?
- O que faz o botão "Adicionar múltiplos" na inclusão de itens do pedido?
- Qual a diferença entre o campo "Observações" e "Observações para NF"?

**Imagens associadas:**
- Página 2: Janela modal de adição de item contendo os campos `Produto: (Descrição)`, `Estoque`, `Quantidade`, `CFOP: 5.949`, `Valor unitário`, `Desconto`, `% (F2)`, `Base cálculo ICMS`, `Aliq. ICMS`, `Aliq. IPI`, `Total ICMS`, `Vlr. total`, `Comissão do vendedor`, indicação `F6: Alterar forma de desconto` e botões `Ok` e `Cancelar`.

---

### [pedidos_fiscal_referenciado-status_03]
**Metadados:**
```json
{
  "id": "pedidos_fiscal_referenciado-status_03",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Regras Fiscais e Situações",
  "subassunto": "Documento Fiscal Referenciado e Status do Pedido",
  "tipo_conteudo": "procedimento",
  "titulo": "Como referenciar documentos fiscais e entender os status do pedido (Gravar, Aprovar e Encerrar)",
  "palavras_chave": ["documento fiscal referenciado", "chave de acesso", "devolução", "gravar", "aprovar", "encerrar", "orçamento"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Guia Fiscal e Ações de Finalização.

**1. Documento Fiscal Referenciado:**
Caso a CFOP/natureza seja de **Devolução** ou de **Emissão em decorrência de cupom fiscal (5.929 ou 6.929)**, é obrigatório informar o documento fiscal original na guia `Fiscal` do pedido:
- Acesse a guia `Fiscal` (localizada junto às abas `Dados do pedido`, `Informações complementares`, `Endereço de entrega/Comissão` e `Transporte`);
- No quadro `Documento fiscal referenciado`, selecione o tipo de documento através das abas: `Nota fiscal eletrônica`, `Nota fiscal convencional`, `Nota fiscal de produtor` ou `Cupom fiscal`;
- No caso de devolução, informe a nota fiscal de compra original através do campo `Chave de acesso:`;
- No caso de nota decorrente de cupom fiscal, informe os dados do cupom emitido para o cliente [REVISAR: no texto original há erro tipográfico: "emitido para o clietne"].

**2. Opções de Finalização e Status do Pedido:**
- **Gravar:** Define o pedido na situação inicial de **orçamento**. Permite edições posteriores, não movimenta saldo de estoque, não gera títulos no financeiro e não permite emissão de nota fiscal.
- **Aprovar:** Define o pedido na situação **aprovada**. Bloqueia alterações cadastrais, não movimenta o estoque, não gera títulos no financeiro e não permite emissão de nota fiscal.
- **Encerrar:** Conclui a transação na situação **encerrada**. Bloqueia alterações cadastrais, permite geração de lançamentos no Contas a Receber (caso a CFOP preveja), efetua a baixa/movimentação física do estoque e habilita a emissão da Nota Fiscal. *(Dica: se o pedido já estiver pronto e conferido, clique diretamente em "Encerrar")*.

**Perguntas frequentes relacionadas:**
- Quando é obrigatório preencher o Documento Fiscal Referenciado no pedido?
- Qual a diferença entre Gravar, Aprovar e Encerrar um pedido no Dataweb?
- O status Gravar baixa os produtos do estoque?

**Imagens associadas:**
- Página 3: Barra de abas do pedido (`Dados do pedido`, `Informações complementares`, `Endereço de entrega/Comissão`, `Transporte`, `Fiscal`) com destaque na guia `Fiscal` aberta, exibindo o bloco `Documento fiscal referenciado` com abas para NF-e, NF convencional, produtor e cupom fiscal, além do campo `Chave de acesso:`.

---

### [pedidos_fiscal_encerramento-emissao_04]
**Metadados:**
```json
{
  "id": "pedidos_fiscal_encerramento-emissao_04",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Encerramento e Faturamento",
  "subassunto": "Encerramento do Pedido e Emissão de NF",
  "tipo_conteudo": "procedimento",
  "titulo": "Como encerrar um pedido e emitir a nota fiscal no Dataweb",
  "palavras_chave": ["encerrar pedido", "emitir nota fiscal", "contas a receber", "danfe", "pedidos encerrados"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Ação Encerrar > Emissão de Nota Fiscal.

**Passo a passo:**
1. No pedido aberto e conferido, clique no botão `Encerrar` [REVISAR: na página 4 o manual utiliza a sigla "ENF" no texto ("Ao encerrar a ENF..."), referindo-se ao encerramento do pedido/emissão de nota].
2. O sistema abrirá a janela "Pressione Ok para confirmar o encerramento desse pedido":
   - `Data de encerramento`: exibe a data da operação;
   - `Lançar no contas a receber`: opção habilitada ou desabilitada automaticamente conforme a CFOP da natureza (ex.: para operações de "Garantia", exibe a mensagem *"Essa CFOP NÃO lança no financeiro"*);
   - `Emitir nota fiscal`: marque esta caixa de seleção caso deseje transmitir e emitir a NF-e imediatamente. *(Caso desmarcada, dê apenas OK e emita a nota posteriormente pelo menu de contexto)*;
   - `Modo operação`: exibe a modalidade (ex.: `NAO USAR FATURA`).
3. Clique no botão `Ok`.
4. Na tela de confirmação seguinte, confirme o pedido que terá a nota emitida clicando em `OK`.
5. O sistema processará a nota fiscal, enviará à SEFAZ e abrirá a impressão do DANFE.
6. O pedido finalizado passará a constar na aba `Pedidos`, dentro da seção `3. Encerrados`, exibindo `Nº do pedido`, `Cliente`, `Dt. Emissão (F7)`, `Dt. Encerramento` e `Total`.

**Perguntas frequentes relacionadas:**
- Como emitir a nota fiscal no mesmo momento em que o pedido é encerrado?
- Por que a opção "Lançar no contas a receber" aparece desabilitada ao encerrar um pedido?
- Onde consultar os pedidos que já foram encerrados?

**Imagens associadas:**
- Página 4 (Superior): Janela "Pressione Ok para confirmar o encerramento desse pedido" com campos de data, aviso de CFOP, checkbox `Emitir nota fiscal` marcado e botões `Ok` e `Cancelar`.
- Página 4 (Inferior): Grade da aba `Pedidos` listando o grupo `3. Encerrados` com o pedido nº 130000017 emitido para "FORNECEDOR (896)".

---

### [pedidos_fiscal_status-nfe-acoes_05]
**Metadados:**
```json
{
  "id": "pedidos_fiscal_status-nfe-acoes_05",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Gestão Fiscal de Notas",
  "subassunto": "Ícones de Status da NF-e e Ações de Cancelamento e Revalidação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como identificar a situação da nota fiscal pelos ícones e executar ações (DANFE, cancelamento e rejeição)",
  "palavras_chave": ["status nota fiscal", "ícones nfe", "imprimir danfe", "cancelar pedido", "nota rejeitada", "revalidar nota", "inutilizar"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Grade de Pedidos > Coluna de Status Fiscal.

A situação fiscal da transação é identificada por ícones visíveis na primeira coluna da grade de pedidos:

**1. Ícone de Nota Autorizada (Documento com símbolo verde):**
- Indica que a NF-e foi transmitida, autorizada pela SEFAZ e está vinculada ao pedido.
- **Reimprimir DANFE:** Clique com o botão direito do mouse sobre o pedido e selecione `Imprimir DANFE`.
- **Cancelar Nota:** Clique com o botão direito sobre o pedido e selecione `Cancelar encerramento do pedido`. **Regra obrigatória:** A nota fiscal só pode ser cancelada dentro do prazo regulamentar de **24 horas** após a emissão.

**2. Ícone de Nota Rejeitada (Símbolo de alerta vermelho):**
- Indica que houve erro na tentativa de transmissão para a SEFAZ; o número ficou retido na transação sem autorização.
- **Tentar nova transmissão:** Clique com o botão direito sobre o pedido e selecione `Emitir/Revalidar nota fiscal`.
- **Remover para posterior inutilização:** Clique com o botão direito sobre o pedido e acesse a opção `Mais - Forçar remover nota fiscal`.

**3. Sem Ícone (Coluna em branco / Opção vazia):**
- Indica que o pedido não possui nota fiscal emitida associada.
- **Emitir NF de pedido já encerrado:** Caso o pedido esteja encerrado, clique com o botão direito do mouse sobre a linha e selecione a opção `Emitir nota fiscal`.

**Perguntas frequentes relacionadas:**
- Qual o prazo limite para cancelar uma nota fiscal emitida no módulo de Pedidos?
- O que fazer quando a nota fiscal ficar com ícone de erro/rejeitada?
- Como reimprimir o DANFE de uma nota fiscal autorizada?

**Imagens associadas:**
- Página 5: Exibição dos 3 ícones da primeira coluna da grade (autorizada, rejeitada e sem nota vinculada).

---

### [pedidos_fiscal_pedido-manual_06]
**Metadados:**
```json
{
  "id": "pedidos_fiscal_pedido-manual_06",
  "manual_origem": "Pedidos.pdf",
  "modulo": "Pedidos",
  "assunto": "Emissão de Pedidos",
  "subassunto": "Emissão de Pedido Manual e Tributação Diferenciada",
  "tipo_conteudo": "procedimento",
  "titulo": "Como fazer um pedido manual para destacar impostos (ICMS/IPI) no Simples Nacional",
  "palavras_chave": ["pedido manual", "destaque icms simples nacional", "csosn 0900", "ipi", "dados da nota", "tributação manual"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "6",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Pedidos > Pedido Manual.

**Finalidade:** O pedido manual permite que as alíquotas, bases e valores tributários sejam preenchidos diretamente pelo operador. É utilizado quando a tributação exigida na operação difere das regras tributárias padrão da empresa.

**Cenário de uso prático:**
Empresas enquadradas no Simples Nacional normalmente emitem notas sem destaque de ICMS e IPI utilizando CSOSN 0101 ou 0102. Caso seja exigido o destaque dos impostos pelo destinatário, a operação exige o uso da **CSOSN 0900**. No pedido manual, é possível inserir a CSOSN 0900 e declarar os valores para que sejam impressos na NF.

**Passo a passo:**
1. Acesse o módulo de pedidos e selecione a opção de emissão de pedido manual.
2. Na inclusão de cada item, preencha os dados fiscais e tributários individuais:
   - `Produto:` e `Quantidade`;
   - `Valor original`, `% Desc.`, `Valor unitário` e `Valor total`;
   - `Base cálculo ICMS`, `Aliq. ICMS`, `Total ICMS`, `Red. ICMS` e `CST` (informar `090` / CSOSN `0900`);
   - `Aliq. IPI` e `Total IPI`;
   - `Base cálculo ICMS ST`, `Aliq. ICMS ST`, `Total ICMS ST`, `Red. ICMS ST` e `MVA`;
   - Clique em `Ok`.
3. Ao finalizar a inserção de todos os itens, **é obrigatório** acessar a guia `Dados da Nota` e informar os valores totais consolidados da nota fiscal.
4. Após preencher todos os dados, clique em `Gravar` (para orçamento) ou em `Encerrar` (para faturamento e emissão).

**Perguntas frequentes relacionadas:**
- Quando devo emitir um pedido manual no Dataweb?
- Como destacar ICMS na nota fiscal sendo optante do Simples Nacional?
- Qual CSOSN permite destacar ICMS em uma emissão manual?

**Imagens associadas:**
- Página 6: Janela modal de inclusão de item no pedido manual com campos abertos para digitação: `Base cálculo ICMS: 119,00`, `Aliq. ICMS: 18`, `Total ICMS: 21,42`, `CST: 0 090`, `Aliq. IPI: 4`, `Total IPI: 4,76`, campos de ICMS ST e botões `Ok` e `Cancelar`.

---

## 3. Glossário do Manual
- **CFOP (Código Fiscal de Operações e Prestações):** Código regulamentado pela legislação tributária que define a natureza fiscal de circulação da mercadoria (venda, remessa, devolução, garantia, etc.).
- **CSOSN (Código de Situação da Operação no Simples Nacional):** Código fiscal aplicado a optantes do Simples Nacional (ex.: 0101, 0102, 0900).
- **CSOSN 0900:** Enquadramento do Simples Nacional ("Outros") que autoriza o preenchimento manual de destaque de ICMS e IPI.
- **Documento Fiscal Referenciado:** Chave de acesso ou número de documento original vinculado a notas de devolução ou notas complementares de cupom fiscal (CFOP 5.929 / 6.929).
- **DANFE:** Documento Auxiliar da Nota Fiscal Eletrônica.
- **ENF:** Sigla utilizada operacionalmente para Emissão de Nota Fiscal / Encerramento Fiscal.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 3:** O texto instrucional contém erro tipográfico no original: *"informe o cupom fiscal emitido para o clietne"*, devendo ser lido como "cliente".
- **Página 4:** O texto cita *"Ao encerrar a ENF, a janela ao lado é exibida..."*, misturando a nomenclatura de pedido com ENF (Emissão de Nota Fiscal).