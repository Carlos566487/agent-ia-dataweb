# Agente IA DataWeb — Módulo Caixa

Este projeto implementa um **assistente virtual corporativo baseado em RAG** (Retrieval-Augmented Generation) para responder a dúvidas operacionais do sistema DataWeb (com foco no Módulo Caixa e processos de Frente de Loja), seguindo o padrão de design visual e identidade das **Óticas Diniz**.

O sistema consome a base de conhecimento local (manuais em PDF e documentos curados em Markdown com metadados semânticos), gera *embeddings* vetoriais de alta precisão e armazena os fragmentos indexados no banco de dados **ChromaDB**. O back-end é desenvolvido em **FastAPI** com streaming em tempo real via **Server-Sent Events (SSE)**, enquanto a interface web oferece respostas escaneáveis, arejadas, com títulos temáticos com emojis, marcadores claros e suporte a temas **Claro** e **Escuro**.

---

## 🚀 Principais Recursos e Alterações Recentes

* **Geração com Gemini 3.5 Flash Lite:** Provedor primário atualizado para `gemini-3.5-flash-lite`, entregando respostas instantâneas com altíssima disponibilidade e suporte a configuração dinâmica via variável `GEMINI_MODEL`.
* **Resiliência e Retentativas:** Tratamento com backoff exponencial automático para erros temporários de limite de taxa (`429 / RESOURCE_EXHAUSTED`) e indisponibilidade de pico (`503 / UNAVAILABLE`).
* **Novo Padrão Visual e Escaneabilidade:**
  * **Títulos de Seção com Emojis:** Identificação visual imediata (ex.: `**💳 Pagamentos**`, `**💰 Venda com Saldo a Receber**`, `**⚠️ Observação**`).
  * **Parágrafos Curtos e Arejados:** Frases diretas (1–2 por parágrafo) com espaçamento vertical duplo, evitando blocos densos de texto.
  * **Marcadores Estruturados:** Itens e métodos listados em linhas individuais no padrão `• **Nome:** Descrição.`.
  * **Negrito Estratégico:** Destaque pontual exclusivamente em nomes de botões, telas, menus, atalhos (`F6`, `Ctrl+R`) e termos chave.
  * **Seção de Observação Padronizada:** Ressalvas ou detalhes não constantes na base são apresentados em um bloco dedicado `**⚠️ Observação**` ao final.
* **Pós-processamento de Streaming (`src/formatador.py`):** Sanitizador leve que reorganiza marcadores colados, títulos sem quebra e cabeçalhos Markdown em tempo real sem degradar a latência do stream.
* **Frontend Aprimorado (`web/index.html`):**
  * Estilo `.balao` atualizado com `white-space: pre-wrap;` e tipografia `strong`, preservando quebras de linha e estrutura em qualquer resolução.
  * Função `formatarMarkdown()` nativa em JS com sanitização HTML contra XSS e conversão de negrito, itálico e códigos inline durante o streaming.
* **Base Vetorial Persistente Indexada:** Ingestão de 146 fragmentos vetoriais a partir de manuais em PDF e markdowns enriquecidos.

---

## 🛠️ Estrutura Técnica

* **Linguagem & Ambiente:** Python 3.14 (Ambiente Windows).
* **Vector Database:** ChromaDB (armazenamento persistente local na pasta `storage/chroma`).
* **Embeddings:** Modelo multilíngue `intfloat/multilingual-e5-base` via *SentenceTransformers* (com prefixos `passage:` e `query:`).
* **Provedores de LLM:**
  * **Google Gemini:** Modelo padrão `gemini-3.5-flash-lite` (via biblioteca oficial `google-genai`).
  * **Anthropic Claude:** Provedor alternativo com `claude-opus-5` (via `anthropic`).
* **Web API:** FastAPI + Uvicorn com streaming assíncrono Server-Sent Events (`text/event-stream`).
* **Front-end:** Interface Single Page (`web/index.html`), tokens visuais das Óticas Diniz, atalhos rápidos (`VENDA`, `GARANTIA`, `DEVOLUÇÃO`) e alternador de tema Claro/Escuro.
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

Edite o arquivo `.env` inserindo sua chave de API:

```env
# Chave de API para o Google Gemini (provedor padrão)
GOOGLE_GENERATIVE_AI_API_KEY="SUA_CHAVE_AQUI"

# Modelo Gemini opcional (padrão: gemini-3.5-flash-lite)
# GEMINI_MODEL="gemini-3.5-flash-lite"

# Chave de API para a Anthropic Claude (provedor alternativo)
ANTHROPIC_API_KEY=

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

### Modo 1: Interface Web (Recomendado)

Inicie o servidor HTTP com Uvicorn:

```powershell
python index.py servir --porta 8000
```

* Acesse no navegador: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Recursos disponíveis:
  * Diálogo fluído com respostas token a token em tempo real.
  * Botões rápidos de sugestão na tela inicial.
  * Seção expansível **Base consultada** exibindo as fontes, páginas e notas de relevância de cada trecho utilizado.
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
│   ├── contratos.py                       # Protocolos e interfaces (SOLID)
│   ├── dominio.py                         # Entidades Chunk e Resultado
│   ├── embedding.py                       # Embeddings multilíngues (SentenceTransformers)
│   ├── fabrica.py                         # Injeção de dependências e fábrica de componentes
│   ├── fonte_markdown.py                  # Extrator de chunks com JSON de metadados
│   ├── fonte_pdf.py                       # Extrator de chunks de arquivos PDF
│   ├── formatador.py                      # Pós-processador visual e corretor de fluxo
│   ├── gerador_claude.py                  # Provedor LLM Anthropic Claude
│   ├── gerador_gemini.py                  # Provedor LLM Google Gemini com retentativas
│   ├── indexador.py                       # Orquestrador de indexação de arquivos
│   ├── leitor_pdf.py                      # Leitor de páginas com PyPDF
│   ├── leitor_sem_repeticao.py            # Filtro de cabeçalhos e rodapés repetitivos
│   ├── normalizador.py                    # Normalizador de texto para PT-BR
│   ├── pesquisa.py                        # Busca semântica vetorial
│   └── separador.py                       # Separador de frases resiliente a abreviações
├── storage/                               # Banco vetorial persistente ChromaDB
│   └── chroma/
├── web/                                   # Frontend estático
│   ├── index.html                         # Interface do chat com suporte a temas e markdown
│   └── logo-diniz.png                     # Identidade visual Óticas Diniz
├── .env.example                           # Modelo de configuração de credenciais
├── index.py                               # Ponto de entrada CLI e servidor
├── pyproject.toml                         # Metadados do projeto Python
└── requirements.txt                       # Dependências do projeto
```

---

## 🔍 Solução de Problemas Comuns

* **`Warning: HF Hub requests are unauthenticated`:** Log informativo do HuggingFace ao baixar os pesos locais de embeddings. O modelo funciona normalmente sem a chave.
* **`Symlink Warning` no Windows:** Definir `HF_HUB_DISABLE_SYMLINKS_WARNING=1` no arquivo `.env` para silenciar os avisos.
* **Erro 429 ou 503 na API de IA:** O sistema possui retentativas automáticas integradas. Se persistir, verifique a cota da sua chave no painel do Google AI Studio.

