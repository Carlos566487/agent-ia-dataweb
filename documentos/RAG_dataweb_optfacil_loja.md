# Base de Conhecimento RAG: Módulo Optfácil (Operacional de Loja)

## Informações do Documento Original
- **Manual de Origem:** Optfacil.com.pdf
- **Módulo Principal:** Optfácil (Frente de Loja / Operacional)
- **Série / Versão:** Pílulas Semanais (VER 01.01 - Outubro de 2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Plataforma Web Mobile (Optfacil.com)
  - Acesso ao Sistema via Mobile e Autenticação
  - Tela Inicial - Escolha da Aplicação (Seletor)
- Módulo Optfácil
  - Tela Inicial (O.S. da Semana e Entregas do Dia)
  - Ordens de Serviço
    - Ordens de Serviço para Receituário (Grau)
    - Ordens de Serviço para Solar (Sem Receita)
  - Cadastros Gerais (Clientes, Médicos, Produtos e Serviços)
  - Módulo Administrador do Optfácil
    - Regras de Desconto
    - Promoção 'Lente em Dobro' (Famílias em Dobro)

---

## 2. Chunks Estruturados para RAG

### [optfacil-loja_geral_acesso-mobile_01]
**Metadados:**
```json
{
  "id": "optfacil-loja_geral_acesso-mobile_01",
  "manual_origem": "Optfacil.com.pdf",
  "modulo": "Optfacil.com / Geral",
  "assunto": "Acesso e Plataforma Mobile",
  "subassunto": "Acesso ao Sistema e Seletor de Aplicações",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar o sistema Optfacil.com via dispositivos móveis e selecionar aplicações",
  "palavras_chave": ["optfacil.com", "acesso mobile", "login", "seletor de aplicação", "optfácil", "dataweb"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-3",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Optfacil.com > Acesso ao Sistema via Mobile > Escolha da Aplicação.

O módulo Optfácil foi desenvolvido para automatizar tarefas operacionais essenciais da ótica, tais como controle de caixa, fechamento de pedidos e gerenciamento de estoque, reduzindo erros humanos e garantindo maior agilidade e rastreabilidade nas operações.

**Pré-requisitos:** Dispositivo móvel (smartphone ou tablet) com navegador web, link de acesso exclusivo fornecido pela DATAWEB, usuário e senha válidos.

**Passo a passo:**
1. No navegador do dispositivo móvel, acesse o link exclusivo disponibilizado para a sua loja (ex.: `óticas-diniz.optfacil`).
2. Digite seu usuário e senha cadastrados para autenticação segura.
3. Na tela "Selecione a aplicação", clique no módulo desejado:
   - `1-analytics`: Business Intelligence e relatórios de desempenho comercial (Habilitado);
   - `2-dataweb`: interface operacional padrão web (Habilitado);
   - `dilab`: integração laboratorial (Desabilitado);
   - `3-optfácil`: módulo operacional de frente de loja, emissão de OS e cadastros (Habilitado).

**Perguntas frequentes relacionadas:**
- Como acessar o Optfácil pelo smartphone ou tablet?
- O que é necessário para fazer login no portal Optfacil.com?
- Quais aplicações podem ser escolhidas na tela inicial do Optfacil.com?

**Imagens associadas:**
- Página 3: Captura de tela em smartphone exibindo o navegador no endereço `óticas-diniz.optfacil` e a tela "Selecione a aplicação" com os cartões `1-analytics`, `2-dataweb`, `dilab` e `3-optfácil`.

---

### [optfacil-loja_os_receituario-solar_02]
**Metadados:**
```json
{
  "id": "optfacil-loja_os_receituario-solar_02",
  "manual_origem": "Optfacil.com.pdf",
  "modulo": "Optfácil",
  "assunto": "Ordens de Serviço Operacionais",
  "subassunto": "Ordens de Serviço para Receituário e Solar",
  "tipo_conteudo": "procedimento",
  "titulo": "Como consultar e cadastrar Ordens de Serviço de receituário e solar no Optfácil",
  "palavras_chave": ["ordens de serviço", "receituário", "solar", "os sem receita", "nova os", "entregas da semana"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4-5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Ordens de Serviço > Receituário e Solar.

A Ordem de Serviço (OS) formaliza o atendimento ao cliente e estrutura as etapas de montagem e entrega.

**1. Painel Inicial:**
- Ao acessar o Optfácil, a tela "Início" exibe o quadro `O.S. a serem entregues nesta semana`, com a opção de filtrar `Exibir apenas as de hoje`, detalhando número da OS, valor total, cliente, vendedor, previsão e status.

**2. Ordens de Serviço para Receituário (Grau):**
- No menu lateral esquerdo, clique em `O.S.`;
- A grade lista as ordens de serviço vinculadas a prescrições médicas;
- Para pesquisar uma OS existente, utilize o campo `digite o nome ou o identificador`;
- Para cadastrar uma nova OS de receituário, clique no botão superior `+ Nova`.

**3. Ordens de Serviço para Solar (Sem Receita):**
- No menu lateral esquerdo, clique em `O.S. (sem receita)`;
- Esta interface destina-se a óculos solares e produtos que não demandam dioptria oftalmológica;
- Para cadastrar uma nova OS de solar, clique no botão superior `+ Novo`.

**Perguntas frequentes relacionadas:**
- Onde criar uma ordem de serviço para óculos de grau no Optfácil?
- Como emitir uma OS para óculos solar sem receita médica?
- Onde consultar as ordens de serviço previstas para entrega no dia?

**Imagens associadas:**
- Página 4: Tela "Início" com painel de entregas da semana e tela "Ordens de serviço" destacando o menu `O.S.` e o botão `+ Nova`.
- Página 5 (Superior): Tela "O.S. (sem receita)" com lista de clientes, datas, valores e botão `+ Novo`.

---

### [optfacil-loja_cadastros_gerais_03]
**Metadados:**
```json
{
  "id": "optfacil-loja_cadastros_gerais_03",
  "manual_origem": "Optfacil.com.pdf",
  "modulo": "Optfácil",
  "assunto": "Cadastros Básicos",
  "subassunto": "Clientes, Médicos, Produtos e Serviços",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar e gerenciar cadastros de clientes, médicos, produtos e serviços no Optfácil",
  "palavras_chave": ["cadastros", "clientes", "médicos", "produtos", "serviços", "lgpd", "optfacil"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menu lateral Cadastros.

A área de **Cadastros** centraliza e organiza o banco de dados fundamental da loja, agilizando consultas e inclusões diretas via tablet ou celular.

**Entidades gerenciadas:**
- `Clientes`: base cadastral de consumidores com campos de busca por nome, CPF, tipo de pessoa, status de termo LGPD, filial (`Empresa`) e opção `Mostrar apenas clientes ativos`;
- `Médicos`: cadastro de oftalmologistas e optometristas vinculados aos receituários;
- `Produtos`: catálogo de armações, lentes de contato, lentes oftálmicas e acessórios;
- `Serviços`: tabela de serviços prestados pela ótica (ajustes, consertos e montagens).

**Passo a passo:**
1. No menu lateral esquerdo, clique no agrupador `Cadastros`.
2. Clique sobre a entidade desejada (`Clientes`, `Médicos`, `Produtos` ou `Serviços`).
3. Para localizar registros, utilize os filtros de pesquisa e clique em `Pesquisar`.
4. Para incluir um novo registro, clique no botão azul `+ Nova` (ou `+ Novo`) no topo da tela.

**Perguntas frequentes relacionadas:**
- Como cadastrar um novo cliente pelo módulo Optfácil?
- Onde consultar médicos e produtos cadastrados na loja pelo celular?
- Como verificar se o cliente aceitou o termo LGPD no cadastro?

**Imagens associadas:**
- Página 5 (Inferior): Menu lateral com a pasta `Cadastros` expandida e setas vermelhas apontando para `Clientes`, `Médicos`, `Produtos` e `Serviços`, além do formulário de pesquisa com o botão `+ Nova`.

---

### [optfacil-loja_adm_regras-desconto-promo_04]
**Metadados:**
```json
{
  "id": "optfacil-loja_adm_regras-desconto-promo_04",
  "manual_origem": "Optfacil.com.pdf",
  "modulo": "Optfácil / Administrador",
  "assunto": "Regras de Negócio e Campanhas",
  "subassunto": "Regras de Desconto e Promoção 'Lente em Dobro'",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerenciar regras de desconto e consultar a promoção 'Lente em Dobro' no Optfácil Administrador",
  "palavras_chave": ["administrador", "regras de desconto", "famílias em dobro", "promoção lente em dobro", "testar regra"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "6",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menu lateral Administrador > Regras de desconto e Famílias em dobro.

O módulo Administrador do Optfácil permite a configuração estratégica de parâmetros comerciais da loja.

**1. Regras de Desconto:**
- No menu lateral do Administrador, clique em `Regras de desconto`;
- A tela abre a "Administrador - Lista de regras de desconto";
- Permite cadastrar e gerenciar percentuais de desconto parametrizados de acordo com a política da loja, com as ações `Testar regra` e `Nova regra`.

**2. Promoção 'Lente em Dobro' (Famílias em dobro):**
- No menu lateral do Administrador, clique em `Promo em dobro` (intitulada no sistema como `Famílias em dobro`);
- A tela exibe "Administrador - Familias em dobro";
- No campo `Digite o nome da família:`, informe a marca ou linha de lente e clique em `Pesquisar` para listar todos os produtos elegíveis à campanha.

**Perguntas frequentes relacionadas:**
- Como cadastrar regras de desconto pelo Optfácil Administrador?
- Onde consultar as lentes participantes da promoção 'Lente em Dobro'?
- É possível testar uma regra de desconto antes de aplicá-la às vendas?

**Imagens associadas:**
- Página 6: Menu lateral do Administrador destacando as opções `Regras de desconto` e `Promo em dobro`, tela "Administrador - Lista de regras de desconto" com botões `Testar regra` e `Nova regra`, e tela "Administrador - Familias em dobro" com campo de pesquisa por família.

---

## 3. Glossário do Manual
- **Optfácil:** Módulo web móvel do sistema Dataweb voltado à automação e agilização do atendimento de balcão e retaguarda de loja.
- **O.S. (Receituário):** Ordem de Serviço vinculada a dados de dioptrias e prescrições médicas oftalmológicas.
- **O.S. (sem receita / Solar):** Ordem de Serviço simplificada voltada para peças solares ou serviços mecânicos.
- **Famílias em Dobro:** Parâmetro promocional que cadastra as famílias de lentes participantes da campanha de bonificação/dobro.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 6:** O título do tópico no texto cita *"Promoção 'Lente em Dobro'"*, enquanto a interface do sistema exibe a nomenclatura `Administrador - Familias em dobro`.
- **Página 6:** O texto explicativo de regras de desconto contém erro de digitação original (*"controle sobre as condições com oferecidas aos clientes"*), tratado como "condições comerciais".