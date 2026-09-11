# MANUAL 4: Como cadastrar condições de pagamento

## Resumo estrutural
- Módulo: **Financeiro**
  - Assunto: **Cadastro → Condição de pagamento**
    - Subassunto: Criação de uma nova condição de pagamento
    - Subassunto: Cadastro de parcelas de uma condição de pagamento

## Chunks

### [cadastro-condicoes-pagamento_financeiro_nova-condicao_01]
**Metadados:**
```json
{
  "id": "cadastro-condicoes-pagamento_financeiro_nova-condicao_01",
  "manual_origem": "Como cadastrar condições de pagamento",
  "modulo": "Financeiro",
  "assunto": "Cadastro de condições de pagamento",
  "subassunto": "Criação de nova condição de pagamento",
  "tipo_conteudo": "procedimento",
  "titulo": "Como cadastrar uma nova condição de pagamento",
  "palavras_chave": ["condição de pagamento", "cadastro", "financeiro", "descrição", "valor mínimo", "desconto máximo"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Financeiro — Cadastro de condições de pagamento. O procedimento para cadastrar condições de pagamento é realizado através do **Módulo Financeiro**.

Passo a passo:
1. Abra o **Módulo Financeiro**.
2. Acesse a aba **Cadastro → Condição de pagamento...** — isso abre a tela **"Cadastro de condições de pagamento"**, que possui as abas **Condição de pagamento**, **Parcelas** e **Contas bancárias**.
3. Para cadastrar uma nova condição, clique em **"Novo"**.
4. Adicione as informações solicitadas na aba **Condição de pagamento**:
   - **Descrição**
   - **ID**
   - **Valor mínimo**
   - **Desconto máximo (%)**
   - **Habilitar para saídas** (checkbox)
   - **Habilitar para entradas** (checkbox)
   - **Emitir fatura** (checkbox)
   - **Desconto padrão (%)**
5. Após preencher as informações, clique em **"Gravar"** para salvar a nova condição de pagamento.

**Observações:**
- A grade inferior da tela lista as condições de pagamento já cadastradas, com colunas Descrição, Dt. Alteração, Gera Fatura, Saídas e Entradas.

**Perguntas frequentes relacionadas:**
- Como cadastro uma nova condição de pagamento no Dataweb?
- Quais campos preciso preencher para criar uma condição de pagamento?
- Onde fica a tela de cadastro de condições de pagamento no módulo Financeiro?

**Imagens associadas:**
- Tela **"Cadastro de condições de pagamento"** com o botão **"Novo"** destacado e os campos **Descrição**, **ID**, **Valor mínimo**, **Desconto máximo (%)**, **Habilitar para saídas**, **Habilitar para entradas**, **Emitir fatura** e **Desconto padrão (%)** visíveis, além da grade com condições já cadastradas (ex.: "A VISTA", "BOLETO 1X", "BOLETO 2X").

---

### [cadastro-condicoes-pagamento_financeiro_parcelas_02]
**Metadados:**
```json
{
  "id": "cadastro-condicoes-pagamento_financeiro_parcelas_02",
  "manual_origem": "Como cadastrar condições de pagamento",
  "modulo": "Financeiro",
  "assunto": "Cadastro de condições de pagamento",
  "subassunto": "Cadastro de parcelas",
  "tipo_conteudo": "procedimento",
  "titulo": "Como adicionar parcelas a uma condição de pagamento",
  "palavras_chave": ["parcelas", "condição de pagamento", "forma de pagamento", "percentual", "baixar automaticamente"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Financeiro — Cadastro de condições de pagamento, aba Parcelas. Exemplo de cadastro de uma condição de pagamento com definição de parcelas:
1. Clique em **"Novo"**.
2. Na aba **Parcelas**, para adicionar uma parcela, clique no ícone **"+"** (adicionar). **Dica:** para cadastrar múltiplas parcelas de uma vez, utilize o ícone correspondente ao lado do "+" (indicado no manual, sem nome textual explícito).
3. Na janela **"Adicionando parcela"**, preencha as informações solicitadas:
   - **Forma de pagamento** (ex.: Carnê)
   - **Período** (ex.: 30)
   - **Tipo de período** (ex.: Dia)
   - **Percentual** (ex.: 25)
   - Para que a parcela seja baixada automaticamente, selecione o campo **"Baixar"**.
4. Com essas informações preenchidas, clique em **"Ok"**.
5. Após preencher os campos necessários, clique em **"Gravar"** para salvar a nova condição de pagamento.

**Observações:**
- O campo **"Baixar"** é opcional e específico para baixa automática da parcela; se não marcado, a parcela não é baixada automaticamente.
- A grade da aba Parcelas lista as parcelas já adicionadas com colunas Período, Forma de pagamento, Percentual e Baixar.

**Perguntas frequentes relacionadas:**
- Como adiciono parcelas a uma condição de pagamento no Dataweb?
- O que faz o campo "Baixar" ao cadastrar uma parcela?
- Como cadastrar múltiplas parcelas de uma vez em uma condição de pagamento?

**Imagens associadas:**
- Tela **"Cadastro de condições de pagamento"**, aba **Parcelas** selecionada, com o botão **"+"** destacado e a janela **"Adicionando parcela"** aberta sobre ela, mostrando os campos **Forma de pagamento** (Carnê), checkbox **Baixar**, **Período** (30), **Tipo de período** (Dia) e **Percentual** (25), com botão **"Ok"** destacado.

---

## Glossário
- **Condição de pagamento**: conjunto de regras (parcelas, prazos, descontos) que define como um pagamento será recebido ou realizado.
- **Baixar**: opção que faz uma parcela ser baixada (quitada) automaticamente pelo sistema.
- **Habilitar para saídas / Habilitar para entradas**: definem se a condição de pagamento pode ser usada em transações de saída e/ou de entrada.

## Pontos para revisão
- `[REVISAR: o ícone usado para "cadastrar múltiplas parcelas" (mencionado como dica) não tem nome textual no manual, apenas uma imagem de ícone]`
