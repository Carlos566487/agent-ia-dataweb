# Base de Conhecimento RAG: Cadastro de Campanhas

## Informações do Documento Original
- **Manual de Origem:** CADASTRO DE CAMPANHAS.pdf
- **Módulo Principal:** Caixa
- **Versão / Referência:** Manual Operacional de Caixa

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Caixa
  - Cadastro
    - Campanhas...
      - Inclusão de Nova Campanha
      - Preenchimento do Nome (Descrição) e Gravação

---

## 2. Chunks Estruturados para RAG

### [campanhas_caixa_cadastro_01]
**Metadados:**
```json
{
  "id": "campanhas_caixa_cadastro_01",
  "manual_origem": "CADASTRO DE CAMPANHAS.pdf",
  "modulo": "Caixa",
  "assunto": "Campanhas Promocionais",
  "subassunto": "Cadastro de Campanhas",
  "tipo_conteudo": "procedimento",
  "titulo": "Como cadastrar uma nova campanha no módulo Caixa",
  "palavras_chave": ["campanhas", "cadastro de campanhas", "caixa", "promoção", "dados básicos"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-2",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Caixa > Cadastro > Campanhas...

**Pré-requisitos:** Acesso autorizado ao módulo `Caixa`.

**Passo a passo:**
1. No sistema COMMERCIO, acesse o módulo `Caixa`.
2. No menu superior, clique na aba `Cadastro` e selecione a opção `Campanhas...` [REVISAR: no texto da instrução está escrito "acesse o modulo Caixa -> Cadastros -> Campanhas", mas o menu na tela é intitulado "Cadastro"].
3. Na janela "Cadastro de campanha", clique no botão `Novo` (localizado na barra superior de ferramentas).
4. Na aba `Dados básicos`, localize o campo `Descrição:` e digite o nome desejado para a campanha.
5. Clique no botão `Gravar` [REVISAR: o texto orienta "aperte em Gravar", porém o botão `Gravar` na janela encontra-se desabilitado/esmaecido na captura de tela antes do preenchimento da descrição].

**Perguntas frequentes relacionadas:**
- Onde cadastro campanhas promocionais no Dataweb?
- Qual o caminho no módulo Caixa para criar uma nova campanha?
- Onde defino o nome de uma campanha no sistema?

**Imagens associadas:**
- Página 1: Barra de menus do COMMERCIO Caixa com o menu `Cadastro` expandido, destacando a opção `Campanhas...` entre "Motivos para brindes..." e "Defeitos...".
- Página 2: Janela "Cadastro de campanha" aberta com destaque retangular no botão `Novo` e no campo de preenchimento `Descrição:` da aba `Dados básicos`, exibindo ainda a aba secundária `Produtos` e a grade inferior "Motivos de campanha cadastrados:".

---

## 3. Glossário do Manual
- **Campanhas:** Registro promocional ou motivacional configurado no módulo Caixa para associar regras, identificações ou motivos a operações de venda.
- **Dados básicos:** Aba principal do formulário de cadastro onde se definem a identificação textual da campanha, datas e status ativo/inativo.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 1:** O texto instrui acessar *"modulo Caixa -> Cadastros -> Campanhas"*, mas o nome real do menu no sistema é `Cadastro` (no singular).
- **Página 2:** O manual orienta *"aperte em Gravar"*, mas na imagem fornecida o botão correspondente está na barra superior de ações junto a `Novo`, `Alterar`, `Remover`, `Gravar`, `Cancelar` e `Voltar`, tornando-se clicável após a digitação da descrição.