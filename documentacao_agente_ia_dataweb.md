# Agente IA DataWeb (Módulo Caixa) — Documentação Técnica

## 1. Visão Geral do Projeto

O **Agente IA DataWeb (Módulo Caixa)** é um assistente virtual baseado em **RAG** (Retrieval-Augmented Generation), projetado para responder dúvidas operacionais de operadores de loja sobre o sistema DataWeb — com foco no Módulo Caixa e na identidade visual das Óticas Diniz.

O sistema:

- Processa e indexa documentos técnicos (PDFs e Markdowns enriquecidos).
- Armazena representações vetoriais no banco vetorial **ChromaDB**.
- Recupera semanticamente os trechos mais relevantes para a dúvida do usuário.
- Gera respostas com **streaming** via LLM (Gemini ou Claude), seguindo diretrizes narrativas e de *grounding* estrito (sem alucinações).
- Disponibiliza os serviços via **CLI**, **API FastAPI** e uma **interface Web** responsiva com tema Dark/Light.

## 2. Arquitetura e Engenharia de Software

O código em `src/` segue princípios de **Clean Architecture** e design orientado a contratos/interfaces (**SOLID**), facilitando testabilidade e desacoplamento.

### Componentes Principais

| Camada / Componente | Arquivo Principal | Responsabilidade |
|---|---|---|
| Contratos & Interfaces | `src/contratos.py` | Define os contratos via `typing.Protocol` (Normalizador, Fragmentador, FonteDeChunks, GeradorDeResposta, etc.) |
| Entidades de Domínio | `src/dominio.py` | Dataclasses imutáveis `Chunk` (com cálculo de hash SHA-1 idempotente) e `Resultado` |
| Pipeline de Limpeza | `src/normalizador.py` e `src/separador.py` | Normalização fonética/gráfica para PT-BR (ligaduras, hifens quebrados, pontilhados de sumário) e divisão de sentenças resiliente a abreviações brasileiras (sr, dr, pág, nº, etc.) |
| Filtro de Cabeçalhos | `src/leitor_sem_repeticao.py` | Remove cabeçalhos e rodapés repetitivos comuns em manuais PDF, evitando poluição dos vetores |
| Parser Markdown Estruturado | `src/fonte_markdown.py` | Extrai seções enriquecidas com blocos JSON de metadados (`modulo`, `assunto`, `pagina_origem`, etc.) |
| Embeddings & Vetorização | `src/embedding.py` e `src/base_vetorial.py` | Utiliza o modelo `intfloat/multilingual-e5-base` (com prefixos `passage:` e `query:`) e persistência no ChromaDB com métrica de cosseno |
| Agente & Grounding | `src/agente.py` | Prompt com regras estritas: proibição de alucinação, proibição de citar referências internas (`[1]`, `[2]`), tom narrativo e janela de memória conversacional (`Conversa`) |
| Pós-processamento de Saída | `src/formatador.py` | Sanitiza o stream da LLM em tempo real (converte marcações indesejadas, remove linhas divisórias desnecessárias, mantém fluidez) |
| Provedores de LLM | `src/gerador_gemini.py` e `src/gerador_claude.py` | Suporte a Gemini (`gemini-3.6-flash`) e Claude (`claude-opus-5`), com gestão de rate limits (HTTP 429) e retentativas com backoff exponencial |
| API & Servidor | `src/api.py` | Endpoints FastAPI (`/`, `/saude`, `/perguntar`) servindo eventos Server-Sent Events (SSE) |
| Frontend | `web/index.html` | Interface estilizada nos padrões visuais Diniz, com tema claro/escuro, botões rápidos (VENDA, GARANTIA, DEVOLUÇÃO) e exibição expansível dos trechos consultados |
| Ponto de Entrada | `index.py` | CLI com comandos `indexar`, `buscar`, `console` e `servir` |

## 3. Base de Conhecimento Atual

Localizada na pasta `documentos/`:

| Arquivo | Tamanho | Conteúdo |
|---|---|---|
| `MANUAL OPERACIONAL DO SISTEMA DATAWEB – MÓDULO CAIXA.pdf` | 11.7 MB | Manual completo original |
| `RAG_dataweb_modulo_caixa.md` | 65.9 KB | Versão curada em Markdown, dividida em seções operacionais |
| `RAG_dataweb_garantia_devolucao_credito.md` | 23.6 KB | Fluxos de Garantia vs. Devolução (V3), com metadados semânticos completos |

## 4. Diagnóstico do Ambiente

| Item | Status |
|---|---|
| Python | 3.14.4 instalado |
| Pacotes principais (`torch`, `sentence-transformers`, `chromadb`, `fastapi`, `uvicorn`) | Disponíveis |
| Dependências pendentes (`pypdf`, `google-genai`, `anthropic`) | A instalar |
| Base vetorial (`storage/chroma`) | Ainda não gerada |
| Credenciais (`.env`) | A criar, com `GOOGLE_GENERATIVE_AI_API_KEY="sua_chave"` |

## 5. Próximos Passos para Colocar em Funcionamento

1. **Instalar as dependências pendentes:**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Configurar o `.env`** com a chave do Gemini ou Anthropic.
3. **Indexar a base de documentos:**
   ```powershell
   python index.py indexar documentos
   ```
4. **Subir a aplicação web:**
   ```powershell
   python index.py servir --porta 8000
   ```
