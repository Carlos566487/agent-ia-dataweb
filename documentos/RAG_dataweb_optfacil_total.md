# Base de Conhecimento RAG: Analytics, CRM e Optfácil.com (Manual Consolidado)

## Informações do Documento Original
- **Manual de Origem:** Optfacil.com_Total.pdf (ANALYTICS / CRM / OPTIFACIL.COM)
- **Módulos Abrangidos:** Analytics, CRM DATAWEB e Optfácil
- **Série / Versão:** Pílulas Semanais (VER 01.01 - Outubro de 2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Plataforma Web Mobile (Optfacil.com)
  - Acesso ao Sistema via Mobile e Autenticação
  - Tela Inicial (Seletor de Aplicações)
- Módulo Analytics
  - Vendas (Vendas Totais, Comparativos, Vendedor, Médico, Receitas, Geolocalização, Marcas)
  - Metas (Acumuladas, Histórico 12 Meses, Por Segmento e Por Empresa)
  - Financeiro (Contas a Pagar/Receber, Meios de Pagamento por Vendedor, Bancos, Inadimplência)
  - Perfil do Cliente (Gênero e Faixa Etária por Mês)
  - Compras (Análise Geral, Grifes/Marcas, Consultas e Comparativo Compra x Venda)
- Módulo CRM DATAWEB
  - Conceito e Estratégia de CRM no PDV
  - Clientes (Inadimplentes, A Vencer, Aniversariantes, Favoritos e Pesquisar)
  - Agendas (Abertos, Encerrados e Agenda de Contatos)
  - Impulsionar (Receitas Vencidas, Valor de Compras, Top 10, Grife/Marca e O.S. por Período)
  - Ordens de Serviço no CRM (Atrasadas, Prontas e Próxima Entrega)
  - Estatísticas (Monitoramento de Engajamentos)
  - Configurações / Comunicação (WhatsApp Web, Bot do WhatsApp, Integração Facebook e E-mail)
- Módulo Optfácil (Operacional de Loja)
  - Tela Inicial (O.S. da Semana e Entregas do Dia)
  - Ordens de Serviço (Receituário e O.S. sem Receita / Solar)
  - Cadastros Gerais (Clientes, Médicos, Produtos e Serviços)
  - Módulo Administrador do Optfácil (Regras de Desconto e Promoção 'Lente em Dobro')

---

## 2. Chunks Estruturados para RAG

### [optfacil-total_geral_visao-acesso_01]
**Metadados:**
```json
{
  "id": "optfacil-total_geral_visao-acesso_01",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Optfacil.com / Geral",
  "assunto": "Acesso e Plataforma Mobile",
  "subassunto": "Acesso ao Sistema e Seletor de Aplicações",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar o sistema Optfacil.com via dispositivos móveis e selecionar aplicações",
  "palavras_chave": ["optfacil.com", "acesso mobile", "login", "seletor de aplicação", "analytics", "dataweb", "optfácil"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-3",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Optfacil.com > Acesso ao Sistema via Mobile > Escolha da Aplicação.

A plataforma Optfacil.com foi projetada para operar em navegadores de dispositivos móveis (smartphones e tablets), além de computadores, proporcionando gestão ágil e descentralizada das operações de loja, estoque, caixa, CRM e inteligência analítica.

**Pré-requisitos:** Link exclusivo fornecido pela equipe DATAWEB, usuário e senha válidos e conexão com a internet.

**Passo a passo de acesso:**
1. No navegador do smartphone ou tablet, acesse o link exclusivo disponibilizado pela DATAWEB para a sua loja (ex.: `óticas-diniz.optfacil`).
2. Insira suas credenciais de usuário e senha na tela de autenticação protegida.
3. Na tela "Selecione a aplicação", escolha o módulo desejado entre as opções exibidas:
   - `1-analytics`: painéis de Business Intelligence (BI), relatórios de faturamento, vendas, compras e metas (Habilitado);
   - `2-dataweb`: acesso à interface operacional padrão do ERP web (Habilitado);
   - `dilab`: integração laboratorial (Desabilitado);
   - `3-optfácil`: módulo operacional de frente de loja, emissão de OS, cadastros e CRM (Habilitado).

**Perguntas frequentes relacionadas:**
- Como acessar o Optfacil.com pelo celular ou tablet?
- O que fazer quando a tela "Selecione a aplicação" for exibida no Optfacil?
- Quais módulos estão disponíveis no portal Optfacil.com?

**Imagens associadas:**
- Página 3: Captura de tela de smartphone exibindo a barra de navegação com o endereço `óticas-diniz.optfacil` e a tela "Selecione a aplicação" com os cartões `1-analytics` (Habilitado), `2-dataweb` (Habilitado), `dilab` (Desabilitado) e `3-optfácil` (Habilitado).

---

### [optfacil-total_analytics_vendas-metas_02]
**Metadados:**
```json
{
  "id": "optfacil-total_analytics_vendas-metas_02",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Analytics",
  "assunto": "Inteligência de Vendas e Metas",
  "subassunto": "Painéis de Vendas e Metas",
  "tipo_conteudo": "conceito",
  "titulo": "Indicadores e funcionalidades dos painéis de Vendas e Metas no Analytics",
  "palavras_chave": ["analytics", "vendas", "metas", "bi", "desempenho comercial", "receitas digitadas", "vendas por médico"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4-5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Analytics > Menu Lateral > Vendas e Metas.

O módulo Analytics reúne relatórios de Business Intelligence (BI) para acompanhamento em tempo real do faturamento e produtividade da equipe comercial.

**Relatórios disponíveis no menu Vendas:**
- `Vendas Totais`: monitoramento global do desempenho financeiro de vendas;
- `Comparativo de Anos`: análise comparativa gráfica de vendas entre exercícios consecutivos;
- `Vendas por Vendedor/Mês`: volume e valores faturados individualmente por cada vendedor;
- `Vendas por Médicos/Mês`: acompanhamento da produção atrelada a prescrições médicas;
- `Receitas Digitadas/Mês`: controle quantitativo de receitas oftalmológicas cadastradas no período;
- `Vendas por Estado e Cidade`: análise de geolocalização e praça dos consumidores;
- `Análise por Grupo Econômico`: avaliação segmentada por redes ou grupos empresariais;
- `Análise por Consultor`: métricas de performance detalhadas por consultor de vendas;
- `Vendas por Segmento e Marca`: distribuição de faturamento por marcas e linhas de produtos;
- `Vendas por Marcadores Especiais`: filtragem orientada a tags e marcadores internos da loja;
- `Vendas por Família`: agrupamento de vendas por categorias/famílias de lentes e armações.

**Relatórios disponíveis no menu Metas:**
- `Vendas Acumuladas`: acompanhamento progressivo das metas comerciais da unidade;
- `Histórico dos Últimos 12 Meses`: evolução comparativa de metas nos últimos doze meses;
- `Meta por Segmento`: desdobramento dos objetivos comerciais por categoria de produtos;
- `Meta por Empresa`: definição e acompanhamento de metas atribuídas por loja/filial.

**Perguntas frequentes relacionadas:**
- Onde consultar o comparativo de vendas entre anos no Analytics?
- Como acompanhar o cumprimento de metas por vendedor ou empresa?
- É possível filtrar vendas por médicos prescritores no módulo Analytics?

**Imagens associadas:**
- Página 4: Interface do Analytics destacando o menu lateral `Vendas`, com filtros de período/loja, cartões de totalizadores de venda e gráfico de barras comparativo.
- Página 5: Interface do painel `Metas`, com filtros, indicadores consolidados de metas e gráfico de evolução mensal.

---

### [optfacil-total_analytics_financeiro-perfil-compras_03]
**Metadados:**
```json
{
  "id": "optfacil-total_analytics_financeiro-perfil-compras_03",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Analytics",
  "assunto": "Inteligência Financeira, Compras e Perfil do Cliente",
  "subassunto": "Gestão Financeira, Demografia de Clientes e Compras",
  "tipo_conteudo": "conceito",
  "titulo": "Funcionalidades dos painéis de Financeiro, Perfil do Cliente e Compras no Analytics",
  "palavras_chave": ["analytics financeiro", "perfil do cliente", "análise de compras", "inadimplência", "contas bancárias", "faixa etária"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5-6",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Analytics > Menus Financeiro, Perfil do Cliente e Compras.

Os painéis do Analytics complementam a visão de frente de loja com auditoria financeira, inteligência demográfica e gestão do mix de suprimentos:

**Menu Financeiro:**
- `Contas a Pagar e Receber`: acompanhamento do fluxo de caixa e compromissos financeiros;
- `Forma de Pagamento por Vendedores/Mês`: análise de distribuição dos meios de liquidação (cartões, dinheiro, PIX, carnê) por operador;
- `Contas Bancárias`: monitoramento das contas correntes cadastradas no sistema;
- `Inadimplência`: indicadores globais de atrasos e pendências financeiras de clientes;
- `Inadimplência de Carnês`: monitoramento específico da carteira de crediário próprio em aberto.

**Menu Perfil do Cliente:**
- `Quantidade Vendida por Gênero/Mês`: análise demográfica de compradores dividida por sexo;
- `Quantidade Vendida por Idade/Mês`: vendas agrupadas por faixas etárias para direcionamento de marketing.

**Menu Compras:**
- `Análise Geral`: visão macro de reposição e pedidos efetuados;
- `Lista de Grifes e Marcas`: catálogo de marcas homologadas e fornecidas;
- `Consultas`: ferramentas de busca de compras e entradas por fornecedor;
- `Análise de Compra e Vendas`: confrontação direta entre volume adquirido e volume comercializado no período.

**Perguntas frequentes relacionadas:**
- Onde consultar a inadimplência de carnês no Analytics?
- Como analisar a distribuição de vendas por faixa etária e gênero dos clientes?
- Onde confrontar o volume de compras com as vendas de cada marca?

**Imagens associadas:**
- Página 5 (Inferior): Tela do painel `Financeiro` exibindo a tabela "Contas a pagar e receber dia a dia" com saldo do dia, recebimentos, pagamentos e conciliação bancária.
- Página 6: Telas dos painéis `Perfil do cliente` (filtros e caixas de indicadores demográficos), `Análise geral` de compras e tela de `Consultas` com comparativo entre compras e vendas.

---

### [optfacil-total_crm_visao-clientes-agendas_04]
**Metadados:**
```json
{
  "id": "optfacil-total_crm_visao-clientes-agendas_04",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "CRM",
  "assunto": "Gestão de Relacionamento com o Cliente",
  "subassunto": "Segmentação de Clientes e Agendas de Contato",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerenciar clientes inadimplentes, aniversariantes, favoritos e compromissos no CRM",
  "palavras_chave": ["crm", "inadimplentes", "a vencer", "aniversariantes", "clientes favoritos", "agendas", "lgpd"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "7-8",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menu lateral CRM (ou aplicação CRM) > Clientes e Agendas.

O CRM de Vendas (*Customer Relationship Management*) atua desde o atendimento em loja até o pós-venda, mantendo conformidade total com a LGPD e agilizando consultas a históricos de compras e cobrança.

**Acesso ao CRM:**
No menu lateral esquerdo do Optfácil, clique no item `CRM` para ser redirecionado à plataforma web de relacionamento.

**Submenus da guia Clientes:**
1. `Inadimplentes`: lista consumidores com acordos financeiros pendentes após o recebimento do produto/serviço. Permite pesquisar por Nome/CPF, intervalo de vencimento (`Data vencimento inicial` e `final`), forma de pagamento e empresa, exibindo dados de contato, negativação, valor principal e juros estimados.
2. `A vencer`: consulta clientes que possuem títulos a vencer nos próximos períodos.
3. `Aniversariantes`: lista aniversariantes cadastrados. Permite consultar aniversariantes do dia de hoje, de uma data específica, da semana ou de todo o ano para campanhas promocionais.
4. `Favoritos`: carteira de clientes de alto valor e relevância estratégica, categorizados com base em histórico de compras, volume gasto, frequência ou potencial de recompra.
5. `Pesquisar`: mecanismo de busca cadastral direta de clientes.

**Submenus da guia Agendas:**
- Permite que vendedores e gerentes agendem e acompanhem compromissos, ligações e retornos com clientes através das opções:
  - `Abertos`: compromissos pendentes de realização;
  - `Encerrados`: histórico de atendimentos e contatos concluídos;
  - `Agenda`: visão de calendário e agendamentos futuros filtrados por cliente, usuário responsável e data inicial.

**Perguntas frequentes relacionadas:**
- Onde consultar a lista de clientes inadimplentes para cobrança no CRM?
- Como buscar aniversariantes do mês ou da semana no CRM do Optfacil?
- Como funciona a ferramenta de Agendas para acompanhamento de clientes?

**Imagens associadas:**
- Página 7: Redirecionamento através do clique no ícone `CRM` do menu lateral do Optfácil e exibição do menu lateral do módulo CRM. [REVISAR: a lista gráfica do menu CRM apresenta os itens "Meu BI" e "OptFácil", que não constam na numeração textual de tópicos].
- Página 8: Tela `Clientes - Inadimplentes` com campos de busca por nome/CPF, datas e lista de cobrança. Tela de `Agendamentos` exibindo filtros de cliente, usuário responsável e data inicial.

---

### [optfacil-total_crm_impulsionar-estatisticas_05]
**Metadados:**
```json
{
  "id": "optfacil-total_crm_impulsionar-estatisticas_05",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "CRM",
  "assunto": "Estratégia Comercial e Engajamento",
  "subassunto": "Ferramenta Impulsionar e Estatísticas de Engajamento",
  "tipo_conteudo": "conceito",
  "titulo": "Como utilizar a ferramenta Impulsionar e monitorar engajamentos de clientes no CRM",
  "palavras_chave": ["impulsionar", "receitas vencidas", "top 10 clientes", "grife marca", "ordens de serviço", "estatísticas", "engajamento"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "9-10",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Guias Impulsionar e Estatísticas.

A ferramenta **Impulsionar** disponibiliza relatórios analíticos para identificar tendências de vendas, recuperar receitas e alavancar o crescimento da ótica através de 5 classificações-chave:
1. `Receitas Vencidas`: lista de clientes com receitas oftalmológicas com data de validade prescricional expirada, sinalizando a oportunidade de retorno ao médico e compra de novos óculos;
2. `Valor de Compras por Período`: demonstra o montante financeiro gasto por clientes em intervalos específicos (mês, trimestre ou ano);
3. `Clientes Top 10 (Valor Total)`: ranqueia os 10 maiores clientes em volume monetário acumulado para receberem tratamento VIP e ações de retenção;
4. `Grife/Marca`: segmenta o desempenho comercial por marcas de armações, lentes e acessórios, apoiando estratégias conjuntas com fornecedores;
5. `Ordens de Serviço por Período`: visão quantitativa das ordens criadas, executadas ou em andamento em um período para dimensionar o fluxo operacional e de serviços da loja.

**Guia Estatísticas - Engajamentos:**
- Monitora os pontos de contato e a resposta dos clientes às iniciativas da ótica (visitas presenciais, retorno a campanhas promocionais, interações em canais digitais e consumo de serviços);
- Permite avaliar a eficiência dos agendamentos de cada vendedor (campo `Usuário`), identificando se as abordagens resultaram em engajamento real de vendas.

**Perguntas frequentes relacionadas:**
- O que é o recurso Impulsionar no CRM do Dataweb?
- Como localizar receitas oftalmológicas vencidas para atrair clientes de volta à loja?
- Onde consultar o ranking dos 10 melhores clientes da loja?

**Imagens associadas:**
- Página 9: Tela `Impulsionar` com filtro por `Empresa`, status `LGPD` e campo `Consulta` desdobrando a lista com as 5 opções analíticas.
- Página 10: Tela `Estatísticas - Engajamentos` com filtro por `Tipo`, `Usuário` (ex.: CARLOS EDUARDO), período e mensagem de contagem de engajamento de vendas.

---

### [optfacil-total_crm_os-atendimento_06]
**Metadados:**
```json
{
  "id": "optfacil-total_crm_os-atendimento_06",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "CRM",
  "assunto": "Ordens de Serviço no CRM",
  "subassunto": "Acompanhamento de Prazos de Entrega de O.S.",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acompanhar e gerenciar prazos de Ordens de Serviço pelo CRM",
  "palavras_chave": ["os crm", "ordens de serviço atrasadas", "os prontas", "próxima entrega", "status lgpd", "prazos de entrega"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "10",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Guia O.S.

O módulo de Ordens de Serviço integrado ao CRM organiza o fluxo de atendimento da ótica, garantindo comunicação proativa com os clientes e cumprimento de prazos.

**Categorias de acompanhamento:**
- `Atrasadas`: reúne todas as ordens de serviço que ultrapassaram a data estimada de conclusão sem terem sido finalizadas, exigindo prioridade operacional e contato com laboratórios/fornecedores;
- `Prontas`: lista as ordens totalmente concluídas que estão aguardando retirada ou prontas para despacho ao cliente, possibilitando o disparo imediato de notificações;
- `Próx. entrega`: ordens em fase final de produção cujo prazo de entrega acordado está se aproximando.

**Passo a passo de consulta:**
1. No menu lateral do CRM, clique na guia `O.S`.
2. Selecione a categoria desejada: `Atrasadas`, `Prontas` ou `Próx. entrega`.
3. Selecione a loja no campo `Empresa` e, se necessário, filtre pelo status `LGPD`.
4. Clique no botão `Pesquisar`.
5. A lista exibirá o número da O.S., nome do cliente, permissão LGPD, celular, e-mail e quantidade de dias decorridos.

**Perguntas frequentes relacionadas:**
- Como identificar quais óculos estão com a entrega atrasada no CRM?
- Onde consultar as ordens de serviço que já estão prontas para entrega ao cliente?
- Como filtrar ordens de serviço de acordo com o termo de consentimento LGPD?

**Imagens associadas:**
- Página 10: Tela `Ordens de serviço - Atrasadas` exibindo o filtro de Empresa (DINIZ - SHOPPING TRIMAIS), botão `Pesquisar` e lista com número da OS, cliente, ícones de status LGPD, celular, e-mail e contador de dias em atraso.

---

### [optfacil-total_crm_configs-automacao_07]
**Metadados:**
```json
{
  "id": "optfacil-total_crm_configs-automacao_07",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "CRM",
  "assunto": "Configurações de Comunicação",
  "subassunto": "Canais de Disparo (WhatsApp, Bot, Facebook e E-mail)",
  "tipo_conteudo": "procedimento",
  "titulo": "Como configurar e parametrizar o envio automático de mensagens via WhatsApp e E-mail no CRM",
  "palavras_chave": ["configs", "whatsapp web", "bot do whatsapp", "facebook business", "modelos de mensagem", "servidor smtp"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "11",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Configs > Modelos e Serviços.

A guia **Configs** permite padronizar templates de mensagens e definir as integrações de disparo automático para nutrição, cobrança e avisos de entrega aos clientes.

**1. Modelos (Templates de Mensagem):**
- Permite cadastrar modelos de e-mail e mensagens instantâneas com campos dinâmicos personalizáveis.

**2. Serviços (Canais de Comunicação):**
- **Redirecionamento para WhatsApp Web:**
  - As mensagens geradas pelo CRM abrem no WhatsApp Web com o número de celular do cliente e o texto pré-configurados;
  - Suporta texto simples, emojis e modelos cadastrados.
- **Bot do WhatsApp:**
  - Permite o envio automatizado conectando o número da ótica via leitura de QR Code;
  - *Regra técnica:* Não oferece suporte a múltiplas contas simultaneamente (exige desvincular uma conta para conectar outra). O bot dispara mensagens exclusivamente para contatos já salvos ou que já possuam conversa aberta no aparelho.
- **Integração com o Facebook (WhatsApp Business API):**
  - Integração corporativa oficial que exige conta verificada no Facebook Business;
  - *Regra técnica:* Ao vincular o número ao Facebook, ele passa a ser de uso exclusivo desta integração e **deixa de ser acessível** pelo aplicativo móvel convencional do WhatsApp;
  - *Recursos:* Envio de textos, imagens, emojis, mensagens em grupos e disparos pelo CRM para novos números e contatos não salvos.
- **Configuração de E-mail:**
  - Parametrização dos dados de envio do servidor corporativo: endereço de e-mail, nome do remetente, servidor SMTP, porta e autenticação (usuário e senha).

**Perguntas frequentes relacionadas:**
- Quais são as diferenças entre o Bot do WhatsApp e a Integração com o Facebook no CRM?
- É possível disparar mensagens pelo WhatsApp Web usando modelos pré-definidos?
- O que acontece com o aplicativo do WhatsApp ao vincular o número à integração do Facebook?

**Imagens associadas:**
- Página 11: Tela `Configurações - Modelos` e 4 janelas modais de `Configurações de serviços` ilustrando a configuração do Redirecionamento para WhatsApp Web, Bot do WhatsApp, Integração com o Facebook e Servidor de E-mail.

---

### [optfacil-total_optfacil_os-receituario-solar_08]
**Metadados:**
```json
{
  "id": "optfacil-total_optfacil_os-receituario-solar_08",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Optfácil",
  "assunto": "Ordens de Serviço Operacionais",
  "subassunto": "Abertura e Consulta de O.S. de Receituário e Solar",
  "tipo_conteudo": "procedimento",
  "titulo": "Como consultar e criar ordens de serviço para receituário e solar no Optfácil",
  "palavras_chave": ["optfacil", "ordens de serviço", "receituário", "solar", "os sem receita", "nova os"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "12-13",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menus Início, O.S. e O.S. (sem receita).

A Ordem de Serviço (OS) formaliza o atendimento, registra os produtos selecionados e norteia a produção laboratorial.

**1. Tela Inicial do Optfácil:**
- Ao entrar no módulo, a tela inicial apresenta o quadro `O.S. a serem entregues nesta semana`, com o filtro rápido `Exibir apenas as de hoje`, informando número da OS, valor total, cliente, vendedor, data prevista e situação.

**2. Ordens de Serviço para Receituário:**
- No menu lateral, clique na opção `O.S.` (ícone de prancheta/lápis);
- A tela lista todas as OS de óculos de grau/receituário;
- Para pesquisar, use o campo `digite o nome ou o identificador` ou filtre por ordenação (ex.: `Recentes`);
- Para emitir um novo pedido de receituário, clique no botão azul `+ Nova` no canto superior direito.

**3. Ordens de Serviço para Solar (Sem Receita):**
- No menu lateral, clique na opção `O.S. (sem receita)`;
- Esta tela lista as vendas e serviços de óculos solares ou produtos que dispensam dioptrias/receitas médicas;
- Para abrir uma nova OS de solar, clique no botão superior `+ Nova`.

**Perguntas frequentes relacionadas:**
- Como criar uma nova ordem de serviço para óculos de grau no Optfácil?
- Onde são lançadas as ordens de serviço de óculos solares no sistema?
- Como verificar quais ordens de serviço têm entrega prevista para o dia de hoje?

**Imagens associadas:**
- Página 12: Tela inicial do Optfácil destacando a lista de entregas da semana e tela `Ordens de serviço` (receituário) com seta vermelha apontando para o menu `O.S.` e destaque no botão `+ Nova`.
- Página 13: Tela `O.S. (sem receita)` com seta vermelha apontando para o item do menu lateral e grade demonstrando clientes, datas e status.

---

### [optfacil-total_optfacil_cadastros-gerais_09]
**Metadados:**
```json
{
  "id": "optfacil-total_optfacil_cadastros-gerais_09",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Optfácil",
  "assunto": "Cadastros Básicos",
  "subassunto": "Gestão de Clientes, Médicos, Produtos e Serviços",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar e gerenciar cadastros de clientes, médicos, produtos e serviços no Optfácil",
  "palavras_chave": ["cadastros optfacil", "cadastrar clientes", "médicos", "produtos", "serviços", "lgpd"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "13",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menu lateral Cadastros.

A área de **Cadastros** centraliza e organiza o banco de dados da loja diretamente pela interface móvel, agilizando consultas no momento da venda.

**Estrutura de cadastros disponíveis:**
- `Clientes`: base de clientes com filtros por nome, CPF, tipo de pessoa, status de termo LGPD, empresa e opção `Mostrar apenas clientes ativos`. Botão `+ Nova` para cadastramento rápido;
- `Médicos`: cadastro de profissionais oftalmologistas e optometristas vinculados às prescrições;
- `Produtos`: catálogo de mercadorias da loja (armações, lentes de contato, acessórios, estojos e produtos de limpeza);
- `Serviços`: tabela de serviços prestados pela ótica (ajustes, soldas, consertos e montagens).

**Passo a passo para consulta e inclusão:**
1. No menu lateral esquerdo do Optfácil, clique sobre a pasta `Cadastros` para expandir suas opções.
2. Selecione a entidade desejada: `Clientes`, `Médicos`, `Produtos` ou `Serviços`.
3. Para localizar um registro existente, preencha os campos de busca e clique em `Pesquisar`.
4. Para incluir um novo cadastro, clique no botão azul `+ Nova` (ou `+ Novo`) posicionado no canto superior direito da tela.

**Perguntas frequentes relacionadas:**
- Como cadastrar um novo cliente pelo módulo Optfácil?
- Onde consultar os produtos e serviços cadastrados na loja pelo celular?
- Como verificar se o cliente está com o status LGPD regularizado no Optfácil?

**Imagens associadas:**
- Página 13 (Centro): Menu `Cadastros` expandido com setas vermelhas destacando as opções `Clientes`, `Médicos`, `Produtos` e `Serviços`, além do formulário de pesquisa de clientes com botão `+ Nova`.

---

### [optfacil-total_optfacil_adm-regras-promo_10]
**Metadados:**
```json
{
  "id": "optfacil-total_optfacil_adm-regras-promo_10",
  "manual_origem": "Optfacil.com_Total.pdf",
  "modulo": "Optfácil / Administrador",
  "assunto": "Regras de Negócio e Campanhas Promocionais",
  "subassunto": "Regras de Desconto e Promoção 'Lente em Dobro'",
  "tipo_conteudo": "procedimento",
  "titulo": "Como configurar regras de desconto e consultar a promoção 'Lente em Dobro' no Optfácil",
  "palavras_chave": ["administrador optfacil", "regras de desconto", "famílias em dobro", "promoção lente em dobro", "campanha"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "13-14",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Optfácil > Menu lateral Administrador > Regras de desconto e Famílias em dobro.

O acesso ao menu `Administrador` dentro do Optfácil concede permissão completa (*full*) para criação, edição e consulta de diretrizes comerciais da loja.

**1. Regras de Desconto:**
- No menu lateral do módulo Administrador, clique em `Regras de desconto`;
- A tela exibe o painel "Administrador - Lista de regras de desconto";
- Permite definir percentuais de desconto parametrizados de acordo com a estratégia comercial, garantindo controle sobre as concessões feitas pelos vendedores;
- Ações disponíveis na barra: `Testar regra` e `Nova regra`.

**2. Promoção 'Lente em Dobro' (Famílias em dobro):**
- No menu lateral, clique na opção `Promo em dobro` (na tela exibida como `Famílias em dobro`);
- A tela exibe "Administrador - Familias em dobro";
- No campo `Digite o nome da família:`, digite a linha ou modelo da lente participante e clique em `Pesquisar`;
- Essa funcionalidade lista todos os itens e famílias de lentes elegíveis à oferta, garantindo que o colaborador aplique o benefício de bonificação e dobro em conformidade com as regras vigentes da campanha.

**Perguntas frequentes relacionadas:**
- Onde cadastrar e testar uma regra de desconto no Optfácil?
- Como verificar quais lentes fazem parte da campanha 'Lente em Dobro' no Optfácil?
- Quem tem acesso para criar novas regras de desconto na loja?

**Imagens associadas:**
- Página 13 (Inferior): Seta vermelha indicando o menu `Administrador` na barra de navegação do Optfácil.
- Página 14: Tela `Administrador - Lista de regras de desconto` com os botões `Testar regra` e `Nova regra`. Tela `Administrador - Familias em dobro` com campo de pesquisa por nome da família e botão `Pesquisar`.

---

## 3. Glossário de Termos Específicos do Dataweb
- **Optfacil.com:** Interface web responsiva do ecossistema Dataweb voltada para tablets, celulares e computadores de frente de loja.
- **Analytics:** Módulo de Business Intelligence (BI) focado em gráficos, relatórios gerenciais e cruzamento de indicadores comerciais.
- **CRM (*Customer Relationship Management*):** Módulo voltado ao ciclo de vida do relacionamento com o consumidor, automação de mensagens, pós-venda e retenção.
- **O.S. (Receituário):** Ordem de Serviço destinada a óculos graduados que exigem prescrição oftalmológica e dados de dioptria.
- **O.S. (sem receita / Solar):** Ordem de Serviço simplificada voltada a óculos solares, armações avulsas ou serviços que dispensam receita médica.
- **Receitas Vencidas (CRM Impulsionar):** Relatório que detecta receituários com validade médica prescrita para incentivar o retorno do cliente à loja.
- **Famílias em Dobro:** Configuração cadastral que vincula famílias de produtos e lentes elegíveis à campanha nacional ou local 'Lente em Dobro'.
- **Status LGPD:** Identificador que indica a situação do consentimento de tratamento de dados pessoais assinado pelo cliente.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 2 (Sumário do manual original):** Os números de página no índice apresentam repetições tipográficas gráficas (ex.: páginas indicadas como "44", "55", "666").
- **Página 7 / CRM:** A captura de tela do menu lateral do CRM apresenta as opções `Meu BI` e `OptFácil`, mas a listagem numerada do texto explicativo do manual enumera apenas 7 tópicos (de Início a Configs).
- **Página 14 / Promoção:** O título textual do tópico grafa *"Promoção 'Lente em Dobro'"* / *"Promo em Dobro"*, enquanto o cabeçalho e menu na captura de tela do sistema intitula-se `Administrador - Familias em dobro`.
- **Página 14 / Texto explicativo de Regra de Desconto:** Há truncamento textual no manual impresso (*"controle sobre as condições com oferecidas aos clientes"*, com a palavra "com" avulsa). Corrigido na base de conhecimento para "condições comerciais".