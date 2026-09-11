# Base de Conhecimento RAG: Módulo Optfacil.com - CRM DATAWEB

## Informações do Documento Original
- **Manual de Origem:** Optfacil.com_CRM.pdf
- **Módulo Principal:** CRM DATAWEB
- **Série / Versão:** Pílulas Semanais (VER 01.01 - Outubro de 2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Plataforma Web Mobile (Optfacil.com)
  - Acesso ao Sistema via Mobile e Autenticação
  - Tela Inicial (Seletor de Aplicações)
- Módulo CRM DATAWEB
  - Redirecionamento e Apresentação do Módulo CRM
  - Clientes (Inadimplentes, A Vencer, Aniversariantes, Favoritos e Pesquisar)
  - Agendas (Abertos, Encerrados e Agenda de Contatos)
  - Impulsionar (Receitas Vencidas, Valor de Compras, Top 10, Grife/Marca e O.S. por Período)
  - Ordens de Serviço no CRM (Atrasadas, Prontas e Próxima Entrega)
  - Estatísticas (Engajamentos de Vendas)
  - Configurações de Comunicação / Configs (Modelos, WhatsApp Web, Bot e Integração Facebook)

---

## 2. Chunks Estruturados para RAG

### [optfacil-crm_geral_acesso-visao_01]
**Metadados:**
```json
{
  "id": "optfacil-crm_geral_acesso-visao_01",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Acesso e Visão Geral do CRM",
  "subassunto": "Acesso Mobile e Navegação no Módulo CRM",
  "tipo_conteudo": "procedimento",
  "titulo": "Como acessar o módulo CRM pelo Optfacil.com e visão geral da plataforma",
  "palavras_chave": ["crm", "optfacil.com", "acesso mobile", "gestão de relacionamento", "pós-venda", "lgpd"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-4",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Optfacil.com > Redirecionamento para Módulo CRM.

O módulo CRM do ecossistema Dataweb atua desde o atendimento em balcão até a fidelização no pós-venda. A ferramenta entrega diferenciais estratégicos, reduz tempo de espera, garante conformidade rigorosa com a LGPD e permite rápido acesso a históricos de compras e cobrança.

**Passo a passo para acesso ao CRM:**
1. No dispositivo móvel, acesse o link exclusivo da loja fornecido pela DATAWEB (ex.: `óticas-diniz.optfacil`).
2. Autentique-se com seu usuário e senha.
3. No seletor de aplicações, escolha `3-optfácil`.
4. Dentro do Optfácil, clique no ícone `CRM` no menu lateral esquerdo para abrir o painel do CRM DATAWEB.
5. O menu do CRM organiza as ferramentas de relacionamento em:
   - 1 - `Clientes`
   - 2 - `Agendas`
   - 3 - `Impulsionar`
   - 4 - `O.S`
   - 5 - `Estatísticas`
   - 6 - `Configs` [REVISAR: na captura gráfica do menu aparecem também as guias "Meu BI" e "OptFácil", não numeradas no texto].

**Perguntas frequentes relacionadas:**
- Como acessar o painel do CRM a partir do Optfácil?
- Quais são os principais recursos disponíveis no CRM DATAWEB?
- O CRM do Dataweb está em conformidade com as exigências da LGPD?

**Imagens associadas:**
- Página 3: Tela em smartphone exibindo o seletor de aplicações com o botão `3-optfácil` habilitado.
- Página 4: Menu do Optfácil com seta vermelha sobre o ícone `CRM` e visualização do painel inicial do CRM com menu lateral numerado de 1 a 6.

---

### [optfacil-crm_clientes_gestao-carteira_02]
**Metadados:**
```json
{
  "id": "optfacil-crm_clientes_gestao-carteira_02",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Gestão de Clientes",
  "subassunto": "Inadimplentes, A Vencer, Aniversariantes e Favoritos",
  "tipo_conteudo": "procedimento",
  "titulo": "Como consultar clientes inadimplentes, a vencer, aniversariantes e favoritos no CRM",
  "palavras_chave": ["clientes", "inadimplentes", "a vencer", "aniversariantes", "clientes favoritos", "cobrança"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Clientes.

O menu **Clientes** agrupa a carteira da ótica em categorias estratégicas de relacionamento:
- `Inadimplentes`: consumidores com acordos financeiros em aberto após terem recebido o produto ou serviço. Permite filtrar por Nome/CPF, período de vencimento (`Data vencimento inicial` e `final`), forma de pagamento e empresa, listando lançamentos, contatos, status de negativação, valor principal e juros estimados;
- `A vencer`: relação de clientes com parcelas a vencer para ações preventivas de recebimento;
- `Aniversariantes`: consulta clientes comemorando aniversário no dia de hoje, em data específica, na semana ou no ano, facilitando o disparo de campanhas comemorativas;
- `Favoritos`: clientes mais relevantes e de maior valor para a loja, categorizados por volume financeiro acumulado, frequência de compras ou potencial de novas vendas;
- `Pesquisar`: ferramenta de pesquisa rápida no cadastro geral.

**Perguntas frequentes relacionadas:**
- Como localizar clientes com parcelas em atraso no CRM?
- Onde consultar os clientes que fazem aniversário na semana pelo CRM?
- O que são os clientes Favoritos no CRM do Dataweb?

**Imagens associadas:**
- Página 5 (Superior): Tela `Clientes - Inadimplentes` com campos de busca por Nome/CPF, intervalo de vencimento, forma de pagamento e grade de resultados de cobrança.

---

### [optfacil-crm_agendas_atendimentos_03]
**Metadados:**
```json
{
  "id": "optfacil-crm_agendas_atendimentos_03",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Agendamentos e Contatos",
  "subassunto": "Gestão de Agendas de Clientes",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerenciar compromissos e agendamentos de clientes no CRM",
  "palavras_chave": ["agendas", "agendamentos", "abertos", "encerrados", "contato com cliente", "retorno"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Agendas.

A funcionalidade de **Agendas de Clientes** organiza as interações futuras da equipe comercial, garantindo que nenhum contato ou oportunidade de venda seja perdida.

**Opções da guia Agendas:**
- `Abertos`: lista agendamentos pendentes de execução;
- `Encerrados`: histórico de compromissos já realizados com clientes;
- `Agenda`: visão consolidada de calendário com filtros por Cliente (Nome/CPF/CNPJ/Telefone), Usuário responsável e Data inicial.

**Perguntas frequentes relacionadas:**
- Como visualizar os compromissos agendados com clientes no CRM?
- Onde verificar o histórico de contatos e retornos já encerrados?
- Como filtrar agendamentos por vendedor/usuário responsável?

**Imagens associadas:**
- Página 5 (Inferior): Tela `Agendamentos` exibindo filtros por cliente, usuário, data inicial e colunas: Agendado para, Cliente, Responsável, Tipo e Avaliação.

---

### [optfacil-crm_impulsionar_estrategia_04]
**Metadados:**
```json
{
  "id": "optfacil-crm_impulsionar_estrategia_04",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Estratégia de Vendas",
  "subassunto": "Ferramenta Impulsionar",
  "tipo_conteudo": "conceito",
  "titulo": "Como utilizar os relatórios estratégicos da ferramenta Impulsionar no CRM",
  "palavras_chave": ["impulsionar", "receitas vencidas", "valor de compras", "clientes top 10", "grife marca", "ordens de serviço por período"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "6",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Impulsionar.

A ferramenta **Impulsionar** disponibiliza análises orientadas a alavancar vendas e fidelizar clientes através de 5 relatórios:
1. `Receitas Vencidas`: lista clientes cujas receitas oftalmológicas estão com prazo expirado, indicando o momento ideal para convidá-los a um novo exame e troca de lentes;
2. `Valor de Compras por Período`: detalha o total gasto por clientes em intervalos específicos (mês, trimestre ou ano);
3. `Clientes Top 10 (Valor Total)`: ranqueia os 10 clientes mais valiosos da ótica para estratégias de retenção e atendimento personalizado;
4. `Grife/Marca`: analisa o faturamento distribuído pelas marcas de armações, lentes e acessórios;
5. `Ordens de Serviço por Período`: quantifica a criação e execução de ordens de serviço ao longo do tempo, mensurando o volume operacional da oficina/laboratório.

**Perguntas frequentes relacionadas:**
- O que é o recurso Impulsionar do CRM Dataweb?
- Como buscar clientes com receita oftalmológica vencida?
- Onde encontrar o relatório dos 10 maiores clientes da loja?

**Imagens associadas:**
- Página 6: Tela `Impulsionar` destacando o seletor de empresa e o campo `Consulta` aberto exibindo as 5 categorias de relatórios analíticos.

---

### [optfacil-crm_os_status-prazos_05]
**Metadados:**
```json
{
  "id": "optfacil-crm_os_status-prazos_05",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Ordens de Serviço no CRM",
  "subassunto": "Status e Gestão de Prazos de Entrega",
  "tipo_conteudo": "procedimento",
  "titulo": "Como monitorar ordens de serviço atrasadas, prontas e próximas da entrega no CRM",
  "palavras_chave": ["ordens de serviço crm", "os atrasadas", "os prontas", "próxima entrega", "status lgpd", "prazos de entrega"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "7",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral O.S.

O painel de Ordens de Serviço do CRM otimiza a comunicação e o acompanhamento dos trabalhos solicitados pelos clientes.

**Categorias de acompanhamento:**
- `Atrasadas`: ordens que ultrapassaram o prazo estimado de conclusão e demandam intervenção prioritária;
- `Prontas`: ordens finalizadas aguardando retirada ou entrega, prontas para aviso imediato ao cliente;
- `Próx. entrega`: ordens em processo de finalização com vencimento próximo.

**Passo a passo de consulta:**
1. No menu do CRM, clique em `O.S`.
2. Escolha o grupo desejado (`Atrasadas`, `Prontas` ou `Próx. entrega`).
3. Selecione a loja no campo `Empresa` e, opcionalmente, filtre por `LGPD`.
4. Clique no botão azul `Pesquisar` para listar número da OS, cliente, aceite LGPD, contatos e dias de atraso.

**Perguntas frequentes relacionadas:**
- Onde consultar ordens de serviço com prazo estourado no CRM?
- Como ver quais óculos já estão prontos para entrega aos clientes?
- Como filtrar ordens de serviço por aceite LGPD?

**Imagens associadas:**
- Página 7 (Superior): Tela `Ordens de serviço - Atrasadas` com filtros de Empresa, status LGPD e grade de dados.

---

### [optfacil-crm_estatisticas_engajamento_06]
**Metadados:**
```json
{
  "id": "optfacil-crm_estatisticas_engajamento_06",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Estatísticas de Relacionamento",
  "subassunto": "Monitoramento de Engajamentos",
  "tipo_conteudo": "conceito",
  "titulo": "Como analisar o engajamento de vendas e interações de clientes no CRM",
  "palavras_chave": ["estatísticas", "engajamentos", "interações", "desempenho de vendas", "agendamentos vendedor"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "7",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Estatísticas > Engajamentos.

O painel **Estatísticas - Engajamentos** avalia a efetividade das interações realizadas entre a ótica e os consumidores (visitas à loja, retorno a promoções, canais digitais e serviços). Permite auditar por vendedor (campo `Usuário`) a taxa de conversão dos agendamentos efetuados em compras concretas.

**Perguntas frequentes relacionadas:**
- Como medir se os agendamentos dos vendedores estão gerando vendas?
- O que é o relatório de Engajamentos no CRM Dataweb?

**Imagens associadas:**
- Página 7 (Inferior): Tela `Estatísticas - Engajamentos` com filtros por Tipo, Usuário ("CARLOS EDUARDO") e contador de engajamento de vendas.

---

### [optfacil-crm_configs_comunicacao_07]
**Metadados:**
```json
{
  "id": "optfacil-crm_configs_comunicacao_07",
  "manual_origem": "Optfacil.com_CRM.pdf",
  "modulo": "CRM",
  "assunto": "Configurações de Comunicação",
  "subassunto": "Automação de WhatsApp, Facebook e E-mail",
  "tipo_conteudo": "procedimento",
  "titulo": "Como configurar o disparo de mensagens automáticas por WhatsApp, Facebook e E-mail no CRM",
  "palavras_chave": ["configs", "modelos", "whatsapp web", "bot whatsapp", "facebook business", "smtp e-mail"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "8",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo CRM > Menu lateral Configs > Modelos e Serviços.

A guia **Configs** centraliza a parametrização dos canais de atendimento e réguas de relacionamento automatizadas.

**1. Modelos:**
- Cadastro e personalização de templates de texto para e-mails e mensagens instantâneas.

**2. Canais de Serviços:**
- **Redirecionamento para WhatsApp Web:** As mensagens abrem diretamente no WhatsApp Web com número e texto pré-preenchidos. Suporta emojis e modelos;
- **Bot do WhatsApp:** Envio automatizado conectando o aparelho via QR Code. Não suporta múltiplas contas simultâneas e atende exclusivamente contatos salvos ou conversas pré-existentes;
- **Integração com o Facebook (API Oficial):** Exige conta verificada no Facebook Business. Ao vincular o número, ele torna-se exclusivo da integração e deixa de operar no aplicativo comum do WhatsApp. Permite mensagens para números não salvos, envio de mídias e grupos;
- **Configuração de E-mail:** Definição do servidor de envio (SMTP, porta, nome de exibição, usuário e senha).

**Perguntas frequentes relacionadas:**
- Como funciona o redirecionamento para o WhatsApp Web no CRM?
- O que é necessário para utilizar a integração oficial do WhatsApp com o Facebook?
- O Bot do WhatsApp permite conectar mais de um número ao mesmo tempo?

**Imagens associadas:**
- Página 8: Tela `Configurações - Modelos` e 4 janelas modais de configuração para WhatsApp Web, Bot do WhatsApp, Integração com o Facebook e Servidor de E-mail.

---

## 3. Glossário do Manual
- **CRM DATAWEB:** Módulo de gerenciamento de relacionamento com clientes integrado ao ERP.
- **Bot do WhatsApp:** Módulo de disparo automático via emulação de sessão por QR Code.
- **Integração com Facebook:** Conexão oficial via WhatsApp Cloud/Business API.
- **Receita Vencida:** Prescrição médica com mais de 12 meses (ou prazo médico excedido) registrada no sistema.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 4:** O menu lateral exibido na captura de tela mostra as opções `Meu BI` e `OptFácil`, mas a relação explicativa textual numera somente até o item 6 (`Configs`).