# Agente IA DataWeb — Módulo Caixa

Este projeto implementa um **assistente virtual corporativo baseado em RAG** (Retrieval-Augmented Generation) para responder a dúvidas operacionais do sistema DataWeb (com foco no Módulo Caixa e processos de Frente de Loja), seguindo o padrão de design visual e identidade das **Óticas Diniz**.

O sistema consome a base de conhecimento local (manuais em PDF e documentos curados em Markdown com metadados semânticos), gera *embeddings* vetoriais de alta precisão e armazena os fragmentos indexados no banco de dados **ChromaDB**. O back-end é desenvolvido em **FastAPI** com streaming em tempo real via **Server-Sent Events (SSE)**, enquanto a interface web oferece respostas escaneáveis, arejadas, com títulos temáticos com emojis, marcadores claros e suporte a temas **Claro** e **Escuro**.

---

## 🚀 Principais Recursos e Alterações Recentes

* **Geração com Gemini 3.8 Flash:** Provedor primário atualizado para `gemini-3.8-flash` — o modelo GA mais recente do Google (set/2026), com janela de 1M tokens de entrada e 65K de saída, entregando respostas rápidas e de alta qualidade. Configurável via variável `GEMINI_MODEL`.
* **Suporte Multi-Provedor (Gemini, Claude, Grok):** Três provedores de IA integrados com seleção automática via variável `PROVEDOR` no `.env`. Basta configurar a chave de API do provedor desejado.
* **Interface Limpa sem Referências RAG:** As fontes da base consultada (trechos do RAG) foram removidas da interface do usuário — o operador vê apenas a resposta direta e profissional, sem referências técnicas internas.
* **Indicador Visual "Processando...":** Novo indicador de processamento com spinner giratório vermelho brilhante (`#FF1A3C`) e texto pulsante "Processando...", proporcionando feedback visual claro durante a geração da resposta.
* **Scripts de Inicialização Rápida:** Arquivos `iniciar.ps1` (PowerShell) e `executar.bat` (duplo clique) para iniciar o servidor com um único comando ou clique.
* **Resiliência e Retentativas:** Tratamento com backoff exponencial automático para erros temporários de limite de taxa (`429 / RESOURCE_EXHAUSTED`) e indisponibilidade de pico (`503 / UNAVAILABLE`).
* **Padrão Visual e Escaneabilidade:**
  * **Títulos de Seção com Emojis:** Identificação visual imediata (ex.: `**💳 Pagamentos**`, `**💰 Venda com Saldo a Receber**`, `**⚠️ Observação**`).
  * **Parágrafos Curtos e Arejados:** Frases diretas (1–2 por parágrafo) com espaçamento vertical duplo, evitando blocos densos de texto.
  * **Marcadores Estruturados:** Itens e métodos listados em linhas individuais no padrão `• **Nome:** Descrição.`.
  * **Negrito Estratégico:** Destaque pontual exclusivamente em nomes de botões, telas, menus, atalhos (`F6`, `Ctrl+R`) e termos chave.
  * **Seção de Observação Padronizada:** Ressalvas ou detalhes não constantes na base são apresentados em um bloco dedicado `**⚠️ Observação**` ao final.
* **Pós-processamento de Streaming (`src/formatador.py`):** Sanitizador leve que reorganiza marcadores colados, títulos sem quebra e cabeçalhos Markdown em tempo real sem degradar a latência do stream.
* **Frontend Aprimorado (`web/index.html`):**
  * Estilo `.balao` atualizado com `white-space: pre-wrap;` e tipografia `strong`, preservando quebras de linha e estrutura em qualquer resolução.
  * Função `formatarMarkdown()` nativa em JS com sanitização HTML contra XSS e conversão de negrito, itálico e códigos inline durante o streaming.
* **Base Vetorial Persistente Indexada:** Ingestão de 307 fragmentos vetoriais a partir de manuais em PDF e 39 markdowns enriquecidos.

---

## 🛠️ Estrutura Técnica

* **Linguagem & Ambiente:** Python 3.14 (Ambiente Windows).
* **Vector Database:** ChromaDB (armazenamento persistente local na pasta `storage/chroma`).
* **Embeddings:** Modelo multilíngue `intfloat/multilingual-e5-base` via *SentenceTransformers* (com prefixos `passage:` e `query:`).
* **Provedores de LLM:**
  * **Google Gemini:** Modelo padrão `gemini-3.8-flash` (via biblioteca oficial `google-genai`).
  * **Anthropic Claude:** Provedor alternativo com `claude-opus-5` (via `anthropic`).
  * **xAI Grok:** Provedor alternativo com `grok-2-latest` (via `openai` apontando para `api.x.ai`).
* **Web API:** FastAPI + Uvicorn com streaming assíncrono Server-Sent Events (`text/event-stream`).
* **Front-end:** Interface Single Page (`web/index.html`), tokens visuais das Óticas Diniz, atalhos rápidos (`VENDA`, `GARANTIA`, `DEVOLUÇÃO`), alternador de tema Claro/Escuro e indicador de processamento destacado.
* **Estrutura RAG Modular:** Pipeline com normalizador para PT-BR, leitor de PDFs com remoção de cabeçalhos/rodapés repetitivos, divisor de frases inteligente e fragmentador semântico.

---

## 📋 Pré-requisitos e Instalação

### 1. Criar e ativar o Ambiente Virtual (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar Dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 3. Configurar Credenciais de Ambiente

Copie o arquivo de exemplo ou crie o `.env` na raiz do projeto:

```powershell
Copy-Item .env.example .env
```

Edite o arquivo `.env` inserindo sua chave de API e provedor desejado:

```env
# Provedor ativo de IA (grok, gemini ou claude)
PROVEDOR=gemini

# Chave de API para o Google Gemini (provedor padrão)
GOOGLE_GENERATIVE_AI_API_KEY="SUA_CHAVE_AQUI"

# Modelo Gemini (padrão: gemini-3.8-flash)
GEMINI_MODEL=gemini-3.8-flash

# Chave de API para o Grok / xAI (provedor alternativo)
# XAI_API_KEY=
# GROK_MODEL=grok-2-latest

# Chave de API para a Anthropic Claude (provedor alternativo)
# ANTHROPIC_API_KEY=
# CLAUDE_MODEL=claude-opus-5

# Desativa alertas de symlinks do HuggingFace no Windows
HF_HUB_DISABLE_SYMLINKS_WARNING=1
```

---

## 📦 Indexação da Base de Conhecimento

A base de conhecimento fica localizada na pasta `documentos/`. Para indexar os manuais no ChromaDB:

```powershell
python index.py indexar documentos
```

Saída esperada:
* `MANUAL OPERACIONAL DO SISTEMA DATAWEB – MÓDULO CAIXA.pdf`: 98 fragmentos
* `39 arquivos Markdown operacionais (*.md)`: 209 fragmentos (módulos Caixa, Pedidos, Faturamento, Estoque, Financeiro, OptFácil, Infraestrutura/Periféricos, etc.)
* **Total na base:** 307 fragmentos em 40 documentos indexados

*(A indexação só precisa ser refeita quando novos arquivos forem adicionados ou alterados na pasta `documentos/`)*.

---

## 💻 Como Utilizar

### Modo 1: Inicialização Rápida (Recomendado)

#### Opção A — PowerShell (um comando)

```powershell
& "c:\Agentes\agent-ia-dataweb-main\iniciar.ps1"
```

O script verifica se o servidor já está rodando, inicia se necessário e abre o navegador automaticamente.

> **Nota:** Se aparecer um erro de "política de execução", execute uma única vez:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

#### Opção B — Duplo clique

Navegue até a pasta do projeto e dê duplo clique no arquivo **`executar.bat`**. O navegador abrirá automaticamente.

#### Opção C — Comando manual

```powershell
cd c:\Agentes\agent-ia-dataweb-main
python index.py servir --porta 8000
```

* Acesse no navegador: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Recursos disponíveis:
  * Diálogo fluído com respostas token a token em tempo real.
  * Botões rápidos de sugestão na tela inicial.
  * Indicador visual **"Processando..."** em vermelho durante a geração.
  * Respostas limpas sem referências técnicas internas ao RAG.
  * Alternância entre temas Claro e Escuro com persistência local.

### Modo 2: Busca Rápida via Terminal (CLI)

```powershell
python index.py buscar "como abrir o caixa"
```

### Modo 3: Console Interativo no Terminal (CLI)

```powershell
python index.py console
```

---

## 📂 Estrutura de Diretórios

```
agent-ia-dataweb/
├── documentos/                            # Base de conhecimento oficial
│   ├── MANUAL OPERACIONAL...CAIXA.pdf     # Manual operacional original
│   ├── RAG_dataweb_modulo_caixa.md        # Documento curado com metadados do Caixa
│   └── RAG_dataweb_garantia...credito.md  # Documento curado de Garantia/Devolução
├── src/                                   # Código-fonte da aplicação
│   ├── agente.py                          # Lógica do Agente e System Prompt padronizado
│   ├── ambiente.py                        # Carregamento de variáveis do .env
│   ├── api.py                             # API FastAPI e endpoints SSE
│   ├── base_vetorial.py                   # Integração com ChromaDB
│   ├── catalogo.py                        # Catálogo de temas pesquisáveis
│   ├── contratos.py                       # Protocolos e interfaces (SOLID)
│   ├── dominio.py                         # Entidades Chunk e Resultado
│   ├── embedding.py                       # Embeddings multilíngues (SentenceTransformers)
│   ├── fabrica.py                         # Injeção de dependências e fábrica de componentes
│   ├── fonte_markdown.py                  # Extrator de chunks com JSON de metadados
│   ├── fonte_pdf.py                       # Extrator de chunks de arquivos PDF
│   ├── formatador.py                      # Pós-processador visual e corretor de fluxo
│   ├── gerador_claude.py                  # Provedor LLM Anthropic Claude
│   ├── gerador_gemini.py                  # Provedor LLM Google Gemini com retentativas
│   ├── gerador_grok.py                    # Provedor LLM xAI Grok com retentativas
│   ├── indexador.py                       # Orquestrador de indexação de arquivos
│   ├── leitor_pdf.py                      # Leitor de páginas com PyPDF
│   ├── leitor_sem_repeticao.py            # Filtro de cabeçalhos e rodapés repetitivos
│   ├── normalizador.py                    # Normalizador de texto para PT-BR
│   ├── pesquisa.py                        # Busca semântica vetorial
│   └── separador.py                       # Separador de frases resiliente a abreviações
├── storage/                               # Banco vetorial persistente ChromaDB
│   └── chroma/
├── web/                                   # Frontend estático
│   ├── index.html                         # Interface do chat com temas, markdown e indicador
│   └── logo-diniz.png                     # Identidade visual Óticas Diniz
├── .env.example                           # Modelo de configuração de credenciais
├── executar.bat                           # Script de inicialização rápida (duplo clique)
├── iniciar.ps1                            # Script PowerShell de inicialização automática
├── index.py                               # Ponto de entrada CLI e servidor
├── pyproject.toml                         # Metadados do projeto Python
└── requirements.txt                       # Dependências do projeto
```

---

## 🔍 Solução de Problemas Comuns

* **`Warning: HF Hub requests are unauthenticated`:** Log informativo do HuggingFace ao baixar os pesos locais de embeddings. O modelo funciona normalmente sem a chave.
* **`Symlink Warning` no Windows:** Definir `HF_HUB_DISABLE_SYMLINKS_WARNING=1` no arquivo `.env` para silenciar os avisos.
* **Erro 429 ou 503 na API de IA:** O sistema possui retentativas automáticas integradas. Se persistir, verifique a cota da sua chave no painel do Google AI Studio.
* **`Execution Policy` no PowerShell:** Execute `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` para permitir a execução de scripts.
* **Porta 8000 já em uso:** O servidor já está rodando. Basta abrir `http://127.0.0.1:8000` no navegador.
* **Servidor demora para iniciar:** O modelo de embeddings é carregado na primeira execução (~10-20s). Após isso, as respostas são imediatas.
