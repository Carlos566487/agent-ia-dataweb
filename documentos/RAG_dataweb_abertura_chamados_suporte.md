# Base de Conhecimento RAG: Abertura de Chamados - Suporte Help Desk

## Informações do Documento Original
- **Manual de Origem:** ABERTURA DE CHAMADOS - SUPORTE HELP DESK.pdf
- **Módulo Principal:** Suporte / Help Desk
- **Série:** Pílulas Semanais (Versão 01.01 - Novembro/2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Suporte Help Desk
  - Canais de Acesso e SLA
    - Objetivo, Importância da Descrição e Classificação de SLA
    - Formas de Acesso ao Suporte Dataweb
  - Procedimento de Abertura de Chamado
    - Nova Solicitação e Assunto
    - Preenchimento dos Campos Obrigatórios e Complementares
    - Anexos e Envio
    - Confirmação de Abertura e Número de Incidente (ID)

---

## 2. Chunks Estruturados para RAG

### [suporte-helpdesk_geral_canais-sla_01]
**Metadados:**
```json
{
  "id": "suporte-helpdesk_geral_canais-sla_01",
  "manual_origem": "ABERTURA DE CHAMADOS - SUPORTE HELP DESK.pdf",
  "modulo": "Suporte / Geral",
  "assunto": "Suporte Help Desk",
  "subassunto": "Canais de Acesso e SLA",
  "tipo_conteudo": "conceito",
  "titulo": "Canais de atendimento e importância da descrição para o SLA de suporte",
  "palavras_chave": ["suporte help desk", "abertura de chamados", "SLA", "canais de atendimento", "dataweb suporte"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1-2",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Suporte / Geral > Suporte Help Desk > Canais de Acesso e SLA.

A abertura correta e o detalhamento das informações nos chamados são essenciais para o cumprimento e aplicação do SLA (*Service Level Agreement*). A correta classificação da prioridade e dos prazos de atendimento depende da análise prévia feita com base na descrição fornecida pelo usuário: quanto mais detalhada for a descrição do problema, maior será a assertividade na análise, garantindo agilidade no atendimento.

**Canais para abertura de chamados no Suporte Dataweb:**
1. **E-mail:** envio de mensagem para `suporte@dataweb.com.br`;
2. **Site:** formulário web em `www.dataweb.com.br/suporte`;
3. **Sistema Dataweb:** clique no botão `Suporte` presente nas telas do sistema e, em seguida, em `Enviar uma solicitação`.

**Perguntas frequentes relacionadas:**
- Quais são as formas de entrar em contato com o suporte do Dataweb?
- Qual é o e-mail do suporte técnico do Dataweb?
- Como a descrição do chamado influencia no prazo de atendimento (SLA)?

**Imagens associadas:** nenhuma

---

### [suporte-helpdesk_sistema_abrir-chamado_02]
**Metadados:**
```json
{
  "id": "suporte-helpdesk_sistema_abrir-chamado_02",
  "manual_origem": "ABERTURA DE CHAMADOS - SUPORTE HELP DESK.pdf",
  "modulo": "Suporte",
  "assunto": "Abertura de Chamados",
  "subassunto": "Criação e Preenchimento de Nova Solicitação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como abrir um chamado de suporte técnico no sistema Dataweb",
  "palavras_chave": ["abrir chamado", "enviar solicitação", "anydesk", "help desk", "suporte técnico", "incidente"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-6",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Suporte > Enviar uma solicitação.

**Pré-requisitos:** Estar conectado ao sistema Dataweb ou acessar o portal de suporte; ter em mãos o ID do AnyDesk e dados da loja (CNPJ, nome da filial e diretor).

**Passo a passo:**
1. Nas telas do sistema, clique no botão `Suporte` e selecione `Enviar uma solicitação`.
2. No formulário "Enviar uma solicitação", preencha os campos:
   - `Assunto`: descreva o tema principal do chamado (o sistema exibirá artigos sugeridos da base de conhecimento com base no que for digitado).
   - `Descrição`: detalhe a dúvida ou problema de forma clara e completa.
   - `Telefone de Contato (Com DDD)*`: informe o número telefônico com DDD para contato direto da equipe de suporte (campo com preenchimento obrigatório).
   - `Anydesk`: insira o número de acesso remoto do AnyDesk da máquina que passará pelo atendimento (o link para baixar o aplicativo caso não possua é disponibilizado: `https://download.anydesk.com/AnyDesk.exe`).
   - `Empresa`: digite o nome da empresa ou filial solicitante (ex.: "DINIZ FRANCHISING").
   - `CNPJ`: digite o CNPJ da empresa/filial.
   - `Grupo/Diretor`: informe o nome do grupo ou diretor responsável pela unidade.
   - `Usuario`: digite o nome do usuário responsável pela abertura e acompanhamento do chamado [REVISAR: no formulário original o rótulo do campo aparece sem acento, como "Usuario", enquanto o texto do manual grafa "Usuário"].
   - `Selecione o tipo de Dúvida/Problema`: selecione a categoria correspondente à solicitação no menu suspenso.
   - `Anexos`: clique em "Escolha um arquivo ou arraste e solte aqui" para anexar capturas de tela (*prints*) ou arquivos que ajudem na análise da demanda.
3. Clique no botão azul `Enviar` ao final do formulário para concluir a solicitação.
4. O sistema exibirá a tela de confirmação de abertura com o número do incidente gerado (`ID`, ex.: `#225564`), dados do solicitante, data/hora de criação, analista atribuído, status e prioridade atribuída.

**Perguntas frequentes relacionadas:**
- Quais informações são obrigatórias para abrir um chamado no suporte do Dataweb?
- Onde informo o AnyDesk para acesso remoto do suporte?
- Como saber o número do chamado após o envio da solicitação?

**Imagens associadas:**
- Página 2: Campo `Assunto` na tela "Enviar uma solicitação" preenchido com "ABERTURA DE CHAMADO COMO EXEMPLO" e lista de "Artigos sugeridos" carregada.
- Página 3: Detalhe do campo `Descrição` com barra de formatação e texto de exemplo, seguido pelos campos `Telefone de Contato (Com DDD)*`, `Anydesk`, `Empresa` e `CNPJ`.
- Página 4: Exemplo dos campos de telefone, AnyDesk, empresa e CNPJ preenchidos com dados fictícios/máscaras.
- Página 5: Campos `Grupo/Diretor`, `Usuario`, `Selecione o tipo de Dúvida/Problema`, área de `Anexos` e botão `Enviar` em destaque.
- Página 6: Janela de confirmação exibindo os dados consolidados do ticket: Solicitante ("Carlos Diniz DF"), ID (`#225564`), Status ("Resolvido"), Atribuído a ("Sergio Junior"), Prioridade ("Normal") e arquivo anexo.

---

## 3. Glossário do Manual
- **SLA (*Service Level Agreement*):** Acordo de nível de serviço que estipula prazos máximos para a classificação, primeiro atendimento e resolução de chamados técnicos conforme a prioridade da demanda.
- **AnyDesk:** Software de conexão remota utilizado pelos analistas de suporte para acessar a estação de trabalho do usuário e realizar diagnósticos e manutenções no PDV.
- **ID do Chamado:** Código numérico identificador exclusivo gerado pelo sistema Help Desk para controle e rastreamento de um ticket de atendimento.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 5:** O rótulo visível no formulário do sistema exibe a grafia `Usuario` (sem acento circunflexo), enquanto o texto instrucional do manual cita `Usuário`.