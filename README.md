# Agente IA DataWeb — Módulo Caixa

Este projeto implementa um **assistente virtual baseado em RAG** (Retrieval-Augmented Generation) para responder a dúvidas operacionais do sistema DataWeb (especificamente o Módulo Caixa), seguindo o padrão de design visual **Diniz**.

O sistema consome os arquivos locais de conhecimento (PDF e Markdown), gera *embeddings* semânticos e armazena os fragmentos indexados utilizando o banco de dados ChromaDB. O back-end é estruturado usando FastAPI, enquanto a interface web foi elaborada com foco na identidade da marca, apresentando respostas de forma limpa, direta, em passos e compatível com temas Claro e Escuro.

---

## Estrutura Técnica

*   **Linguagem & Ambiente**: Python 3.14 (Ambiente Virtual do Windows).
*   **Vector Database**: ChromaDB (armazenamento persistente na pasta `storage/chroma`).
*   **Embeddings**: Modelo multilíngue de alta precisão `intfloat/multilingual-e5-base` fornecido pelo *HuggingFace*.
*   **Geração (LLM)**: O provedor primário configurado é o Gemini (Google) no modelo `gemini-3.6-flash`.
*   **Web API**: FastAPI + Uvicorn com streaming de respostas e eventos para a UI (Server-Sent Events).
*   **Front-end**: Arquivo HTML estático servido pela API (`web/index.html`), mantendo os tokens visuais de estilo Diniz com integração dinâmica do `JS`.
*   **Estrutura RAG Modular**: A indexação é inteligente e divide as classes em: Leitores Sem Repetição, Fontes PDF/Markdown, Fragmentador Semântico e Normalizadores do Idioma PT-BR.

---

## Requisitos de Sistema

*   **Sistema Operacional:** Windows
*   **Python:** 3.14
*   Dependências de sistema essenciais listadas no `requirements.txt` (incluindo PyTorch, sentence-transformers e FastAPI).

---

## Como Configurar o Ambiente e Rodar

### 1. Criando e ativando o Ambiente Virtual (Windows PowerShell)

Caso ainda não tenha ativado ou criado, execute na raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalação das Dependências

Com o ambiente ativado, atualize o pip e instale:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

> **Atenção:** A instalação dos pacotes de IA local (como `torch` e `chromadb`) pode demorar alguns minutos dependendo da sua rede.

### 3. Configuração de Credenciais

No arquivo `.env` localizado na raiz do projeto, garanta que a chave da API do Google Gemini está preenchida corretamente:

```env
GOOGLE_GENERATIVE_AI_API_KEY="SUA_CHAVE_AQUI"
```

### 4. Indexação Inicial (Necessário apenas uma vez ou ao adicionar novos arquivos)

O sistema exige que a base de dados do ChromaDB possua o mapeamento indexado. Execute o script abaixo, apontando para a pasta onde ficam os PDFs e arquivos Markdown (pasta `documentos/`):

```powershell
python index.py indexar documentos
```

Isso fará o parse semântico dos arquivos e salvará localmente as bases vetorizadas.

---

## Utilizando a Aplicação

O projeto possui comandos CLI para teste de terminal e para levantar o servidor WEB.

### Modo Interface Web (Recomendado)

Levante o servidor HTTP no Uvicorn com a seguinte linha de comando:

```powershell
python index.py servir --porta 8000
```
*   Acesse no seu navegador: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
*   A aplicação disponibiliza três botões rápidos ("VENDA", "GARANTIA" e "DEVOLUÇÃO") além de uma caixa de diálogo fluída e responsiva.
*   **Dark Mode**: Botão funcional no canto superior direito para alternar a interface entre temas Claro e Escuro.

### Modo Busca e Modo Interativo no Console (CLI)

Se você precisa consultar ou debugar pelo terminal, basta executar:

*   **Busca em lote único (CLI):**
    ```powershell
    python index.py buscar "como abrir o caixa"
    ```
*   **Sessão interativa (CLI):**
    ```powershell
    python index.py console
    ```

---

## Observações Extras e Troubleshooting

*   **`Warning: HF Hub requests are unauthenticated`:** Ao subir a aplicação ou re-indexar, o HuggingFace pode apresentar este log. Isso é meramente um _warning_ do terminal por não possuir a chave de token da própria base `huggingface` para download do modelo embeddings local. O modelo funciona sem essa chave em velocidade nominal padrão.
*   **Problemas de Symlinks:** No Windows, o HuggingFace pode disparar _warnings_ do tipo `cache-system uses symlinks...`. Adicionar `HF_HUB_DISABLE_SYMLINKS_WARNING=1` no seu `.env` o deixará limpo de avisos.
