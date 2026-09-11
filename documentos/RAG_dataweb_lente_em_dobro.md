# MANUAL 7: Manual Básico Lente em Dobro

## Resumo estrutural
- Módulo: **Administrador** / **Caixa (Vendas / Ordem de Serviço)**
  - Assunto: Promoção **Lente em dobro**
    - Subassunto: Conceito da promoção
    - Subassunto: Marcadores — configurar a família de lentes na promoção
    - Subassunto: Como gerar a O.S. de lente em dobro
    - Subassunto: Como finalizar a venda da O.S. de lente em dobro

## Chunks

### [lente-em-dobro_administrador_conceito_01]
**Metadados:**
```json
{
  "id": "lente-em-dobro_administrador_conceito_01",
  "manual_origem": "Manual Básico Lente em Dobro",
  "modulo": "Administrador",
  "assunto": "Promoção Lente em dobro",
  "subassunto": "Conceito",
  "tipo_conteudo": "conceito",
  "titulo": "O que é a promoção Lente em dobro no Dataweb",
  "palavras_chave": ["lente em dobro", "promoção", "conceito", "marcador"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Administrador — Promoção Lente em dobro, conceito. A **lente em dobro** é uma opção de venda onde o cliente compra um par de lentes e ganha outro par. No sistema, essa operação é configurada de uma maneira fácil e simples, através de duas etapas principais: (1) marcar as famílias de lentes elegíveis com um marcador específico e (2) gerar a Ordem de Serviço (O.S.) da lente em dobro a partir da O.S. original do cliente.

**Observações:**
- Os requisitos necessários para realizar a venda de uma lente em dobro estão descritos nos procedimentos seguintes deste manual (configuração do marcador e geração da O.S.).

**Perguntas frequentes relacionadas:**
- O que é a promoção "Lente em dobro" no Dataweb?
- Como funciona a venda de lente em dobro para o cliente?

**Imagens associadas:** nenhuma.

---

### [lente-em-dobro_administrador_marcadores_02]
**Metadados:**
```json
{
  "id": "lente-em-dobro_administrador_marcadores_02",
  "manual_origem": "Manual Básico Lente em Dobro",
  "modulo": "Administrador",
  "assunto": "Promoção Lente em dobro",
  "subassunto": "Marcadores",
  "tipo_conteudo": "procedimento",
  "titulo": "Como configurar o marcador PROMOCAO:LENTE EM DOBRO nas famílias de lentes",
  "palavras_chave": ["marcador", "PROMOCAO:LENTE EM DOBRO", "família de lentes", "módulo Administrador", "associar marcador"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Administrador — Promoção Lente em dobro, configuração de marcadores. Primeiramente, toda família de lentes que esteja enquadrada na promoção lente em dobro deverá conter o **MARCADOR: PROMOCAO:LENTE EM DOBRO**. Este marcador deve ser inserido através da ferramenta **Marcadores** do módulo Administrador.

Passo a passo:
1. Abra o **módulo Administrador** e clique no botão **"Marcadores" → Famílias...**
2. Na tela **"Manutenção de marcadores da família"**, pesquise pela família de lentes desejada usando o botão **Pesquisar (F3)**.
3. No campo **"Marcadores"**, selecione a opção **"PROMOCAO:LENTE EM DOBRO"**.
4. Selecione (marque o checkbox de) as lentes/famílias que receberão o marcador.
5. Clique em **Marcador → Associar marcador**.
6. O sistema exibirá a pergunta: **"Deseja ASSOCIAR a todas famílias selecionadas o marcador PROMOCAO:LENTE EM DOBRO?"**. Confirme clicando em **"Sim"**.

Com o marcador inserido nas lentes passíveis do uso da lente em dobro, o sistema libera a opção de **"gerar O.S. lente em dobro"**.

**Observações:**
- Após a associação, a coluna "Marcadores associados" da grade de famílias passa a exibir "PROMOCAO:LENTE EM DOBRO" para cada família selecionada.
- Sem esse marcador associado à família de lentes, não é possível gerar a O.S. de lente em dobro para aquele item.

**Perguntas frequentes relacionadas:**
- Como marco uma família de lentes para participar da promoção lente em dobro?
- Onde fica a ferramenta de Marcadores no Dataweb?
- O que preciso fazer antes de conseguir gerar uma O.S. de lente em dobro?

**Imagens associadas:**
- Tela inicial do **módulo Administrador**, com o menu superior (Acesso, Cadastro, Pesquisas, Relatórios e Gráficos, Ferramentas, Histórico, Estoque, Importação/Exportação, Configurações, Ajuda) e o botão **"Marcadores"** destacado em vermelho, com o submenu aberto mostrando as opções "Família de todos os tipos...", **"Famílias..."** (destacada), "Produtos de todos os tipos...", "Produtos...", "Serviços...", "Armações...", "Lentes...", "Pessoas" (Clientes..., Fornecedores...).
- Tela **"Manutenção de marcadores da família"**, com o campo **Marcadores** definido como "PROMOCAO:LENTE EM DOBRO", botão **Pesquisar (F3)** destacado à esquerda, grade central listando famílias de lentes (ex.: "LG VARILUX COMFORT 360 NE1.50 ORM TREX/CRE") com checkboxes de seleção, e no topo os botões **Marcar/Desmarcar**, **Marcador** (com submenu "Associar marcador" destacado, "Remover marcador selecionado", "Remover todos os marcadores da classe selecionada") e **Sair**.
- A mesma tela **"Manutenção de marcadores da família"** após a associação, mostrando "Registro 12 de 12" e a coluna **"Marcadores associados"** preenchida com "PROMOCAO:LENTE EM DOBRO" em destaque azul para cada família da lista.

---

### [lente-em-dobro_vendas_gerar-os_03]
**Metadados:**
```json
{
  "id": "lente-em-dobro_vendas_gerar-os_03",
  "manual_origem": "Manual Básico Lente em Dobro",
  "modulo": "Caixa / Vendas",
  "assunto": "Promoção Lente em dobro",
  "subassunto": "Geração da Ordem de Serviço de lente em dobro",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerar a Ordem de Serviço (O.S.) de lente em dobro",
  "palavras_chave": ["gerar OS lente em dobro", "ordem de serviço", "promoção lente em dobro", "permissão acesso total"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa/Vendas — Promoção Lente em dobro, geração da O.S. Com o marcador **PROMOCAO:LENTE EM DOBRO** já associado à família de lentes, é possível gerar a Ordem de Serviço (O.S.) de lente em dobro a partir de uma O.S. original.

**Pré-requisitos:**
- Para habilitar a opção "Promoção lente em dobro", o usuário deve estar com a permissão de **acesso total** na tarefa **"Promoção lente em dobro"**.
- A Ordem de serviço original precisa ter lentes que tenham o marcador **PROMOCAO:LENTE EM DOBRO**.

Passo a passo:
1. Clique com o **botão direito** na Ordem de serviço original, na tela de Ordens de serviço.
2. Selecione a opção **"Promoção lente em dobro"** no menu de contexto (dentro da seção "Gerar", junto com a opção "Gerar venda").
3. O sistema deve gerar a O.S. em dobro **somente com as lentes**. A quantidade será de **2 lentes**, e o preço será o **preço real de cada lente**.

**Observações:**
- Demais produtos (além das lentes) devem ser inseridos na primeira Ordem de Serviço, ou, se preferir, pode ser gerada uma terceira O.S. para o mesmo cliente — a escolha de qual opção usar fica a critério do usuário.

**Perguntas frequentes relacionadas:**
- Como gero a Ordem de Serviço de lente em dobro a partir da O.S. do cliente?
- Que permissão é necessária para usar a opção "Promoção lente em dobro"?
- A O.S. de lente em dobro inclui outros produtos além das lentes?

**Imagens associadas:**
- Tela de **Ordens de serviço** (módulo Caixa), com o menu de contexto do botão direito do mouse aberto sobre uma O.S. da lista, mostrando as opções "Inserir ordem de serviço...", "Editar ordem de serviço...", "Excluir ordem de serviço...", a seção **"Gerar"** com "Gerar venda" e **"Promoção lente em dobro"** destacada em vermelho (rotulada na imagem como "Gerar OS Lente em dobro"), seguida da seção "Operações" com "Entregar", "Cancelar entrega", "Executar O.S." (F7), "Cancelar execução", "Associar venda...", "Desassociar venda...", entre outras.
- Tela **"Óculos"** (cadastro da O.S. gerada), mostrando os campos Nro. OS, Vendedor, Cliente, Convênio empresarial, Laboratório responsável, Médico, Data de emissão, Data/Hora de previsão para o cliente, Desconto (nos itens), Data/Hora de previsão do fornecedor, Total previsto, Observações, Nº Garantia; na grade de **Produtos**, um item de lente (ex.: "LG HOYALUX SUMMIT 1.41.50 RES IN") com **Quantidade = 2** e valor total correspondente ao preço real de cada lente multiplicado por 2.

---

### [lente-em-dobro_vendas_finalizar-venda_04]
**Metadados:**
```json
{
  "id": "lente-em-dobro_vendas_finalizar-venda_04",
  "manual_origem": "Manual Básico Lente em Dobro",
  "modulo": "Caixa / Vendas",
  "assunto": "Promoção Lente em dobro",
  "subassunto": "Finalização da venda e regras adicionais",
  "tipo_conteudo": "procedimento",
  "titulo": "Como finalizar a venda da O.S. de lente em dobro e regras de alteração de lente",
  "palavras_chave": ["gerar venda", "forma de pagamento Brinde", "nota fiscal modelo 55", "natureza de operação Brinde 5910", "alterar lente", "venda finalizada"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
Módulo Caixa/Vendas — Promoção Lente em dobro, finalização da venda. Após a O.S. de lente em dobro ser gerada, o procedimento para concluir a venda é o seguinte:
1. Selecione a O.S. de lente em dobro gerada e clique em **"Gerar venda"**.
2. A venda da O.S. com a lente em dobro deve ser finalizada com a forma de pagamento **"Brinde"**.
3. Ao finalizar, sairá uma **nota fiscal modelo 55** com **natureza de operação Brinde (5910)**. O preço que sairá na nota é ajustado no cadastro da **Natureza de operação**.

**Alterar a lente da segunda O.S. (opcional):**
- É possível alterar a lente da segunda O.S. (a O.S. de lente em dobro) para outra lente, desde que essa outra lente também tenha o marcador **PROMOCAO:LENTE EM DOBRO**.
- Para habilitar essa opção, o usuário deve estar com a permissão de **acesso total** na tarefa **"Promoção lente em dobro: autorização para alterar lentes"**.

**Observações e exceções:**
- Somente é possível realizar a venda da O.S. Lente em dobro se a primeira O.S. que originou a lente em dobro já estiver com a venda **FINALIZADA**.
- A venda realizada a partir da lente em dobro **não aparece na aba Vendas do caixa** — ela aparece apenas no **histórico de vendas**.

**Perguntas frequentes relacionadas:**
- Com qual forma de pagamento devo finalizar a venda da lente em dobro?
- Por que não consigo finalizar a venda da O.S. de lente em dobro?
- Por que a venda da lente em dobro não aparece na aba Vendas do caixa?
- É possível trocar a lente que será dada de brinde na promoção?

**Imagens associadas:** nenhuma.

---

## Glossário
- **Lente em dobro**: promoção de venda em que o cliente compra um par de lentes e recebe outro par de brinde.
- **Marcador PROMOCAO:LENTE EM DOBRO**: marcador associado a famílias de lentes que as torna elegíveis para a promoção lente em dobro.
- **Manutenção de marcadores da família**: tela do módulo Administrador usada para associar marcadores a famílias de produtos.
- **O.S. (Ordem de Serviço)**: registro da venda/pedido de óculos/lentes de um cliente no sistema.
- **Brinde**: forma de pagamento usada para finalizar a venda da O.S. de lente em dobro, associada à nota fiscal modelo 55 com natureza de operação 5910.
- **Natureza de operação**: cadastro que define, entre outras coisas, o preço que sairá impresso na nota fiscal para determinado tipo de operação (ex.: Brinde).

## Pontos para revisão
- Nenhum ponto sinalizado como `[REVISAR]` neste manual.
