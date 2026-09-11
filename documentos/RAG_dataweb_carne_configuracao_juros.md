# MANUAL 2: Carnê — Configuração de Juros

## Resumo estrutural
- Módulo: **Financeiro**
  - Assunto: Configuração do Financeiro
    - Subassunto: Aba **Juros e CPMF** (taxa e tipo de juros)
    - Subassunto: Aba **Carnê** (desconto, tolerância de atraso e multa)

## Chunks

### [carne-config-juros_financeiro_juros-cpmf_01]
**Metadados:**
```json
{
  "id": "carne-config-juros_financeiro_juros-cpmf_01",
  "manual_origem": "Carnê - Configuração de Juros",
  "modulo": "Financeiro",
  "assunto": "Configuração de juros do carnê",
  "subassunto": "Aba Juros e CPMF",
  "tipo_conteudo": "procedimento",
  "titulo": "Como alterar a porcentagem de juro cobrado nas parcelas em atraso",
  "palavras_chave": ["juros", "carnê", "parcela em atraso", "taxa de juros ao dia", "tipo de juros", "Configuração do Financeiro"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Financeiro — Configuração de juros do carnê. O procedimento para alterar a porcentagem do juro cobrado nas parcelas em atraso é realizado através do **Módulo Financeiro**.

Passo a passo:
1. Abra o **Módulo Financeiro**.
2. Acesse a guia **Configurações → Configurações de contas...**
3. Na tela **Configuração do Financeiro**, acesse a aba **Juros e CPMF** (as demais abas disponíveis nessa tela são: Classificações-padrão, Classificações especiais, Juros e CPMF, Carnê, Outros e Contas bancárias):
   - Defina a **taxa de juros ao dia** no campo correspondente.
   - Defina o **tipo de juros**: **Simples** ou **Composto**.
   - Feitas as alterações, clique em **"Gravar"**.

**Observações:**
- A tela é intitulada **"Configuração do Financeiro"** e exige selecionar a **Empresa** no topo antes de gravar as alterações.

**Perguntas frequentes relacionadas:**
- Como altero a taxa de juros cobrada em parcelas de carnê atrasadas?
- Onde configuro se o juro do carnê é simples ou composto?
- Como acesso a tela de configuração de juros no módulo Financeiro?

**Imagens associadas:**
- Tela **Configuração do Financeiro**, aba **Juros e CPMF** selecionada, mostrando o campo **"Taxa de juros ao dia"** (preenchido com o valor 0,16 no exemplo) e a opção **"Tipo de juros"** com botões de opção **Simples** / **Composto** (Simples selecionado no exemplo).

---

### [carne-config-juros_financeiro_aba-carne_02]
**Metadados:**
```json
{
  "id": "carne-config-juros_financeiro_aba-carne_02",
  "manual_origem": "Carnê - Configuração de Juros",
  "modulo": "Financeiro",
  "assunto": "Configuração de juros do carnê",
  "subassunto": "Aba Carnê",
  "tipo_conteudo": "procedimento",
  "titulo": "Funções adicionais de juros e multa na aba Carnê da Configuração do Financeiro",
  "palavras_chave": ["carnê", "percentual de multa", "limite de dias em atraso", "isentar juros", "percentual de desconto", "Configuração do Financeiro"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
Módulo Financeiro — Configuração do Financeiro, aba Carnê. Além da configuração de juros e CPMF, a aba **Carnê** da tela **Configuração do Financeiro** disponibiliza outras funções relacionadas a juros e multa de parcelas de carnê:
- **Percentual de desconto**: percentual de desconto concedido para pagamento de carnê antecipado.
- **Número de dias de antecipação para conceder desconto**: define a partir de quantos dias de antecipação o desconto passa a ser concedido (ex.: se 0, não concede desconto; se 10, concede desconto se pago 10 dias ou mais antes do vencimento).
- **Limite de dias em atraso para isentar a cobrança de juros**: define o limite de dias em atraso para isenção. Exemplos do próprio sistema: se 0, cobra juros desde o 1º dia de atraso; se 5, cobra juros retroativo se pago após 5 ou mais dias do vencimento; se 10, cobra juros retroativo se pago após 10 ou mais dias do vencimento.
- **Percentual de multa**: percentual de multa aplicado para pagamentos de carnê em atraso.

Após realizar as alterações em qualquer uma dessas abas, é necessário clicar em **"Gravar"** para salvar as informações.

**Observações:**
- Esses campos (Percentual de desconto, Número de dias de antecipação, Limite de dias em atraso, Percentual de multa) ficam todos na aba **Carnê**, distinta da aba Juros e CPMF onde ficam a taxa de juros ao dia e o tipo de juros.

**Perguntas frequentes relacionadas:**
- Como configuro um desconto para quem paga o carnê antes do vencimento?
- Como definir um prazo de tolerância antes de começar a cobrar juros de atraso?
- Onde configuro o percentual de multa por atraso no pagamento do carnê?

**Imagens associadas:**
- Tela **Configuração do Financeiro**, aba **Carnê** selecionada, mostrando os campos **"Percentual de desconto"**, **"Número de dias de antecipação para conceder desconto"** (com texto explicativo de exemplos), **"Limite de dias em atraso para isentar a cobrança de juros"** (com texto explicativo de exemplos) e **"Percentual de multa"**.

---

## Glossário
- **CPMF**: sigla mencionada no nome da aba "Juros e CPMF" da tela de Configuração do Financeiro; o manual não define o termo além do nome da aba. `[REVISAR: sigla CPMF não é definida explicitamente no manual]`
- **Configuração do Financeiro**: tela central de parametrização do módulo Financeiro, com abas para classificações, juros, carnê, outros e contas bancárias.
- **Juros simples / Juros composto**: dois tipos de cálculo de juros configuráveis na aba Juros e CPMF.

## Pontos para revisão
- `[REVISAR: o manual não define o significado da sigla "CPMF" usada no nome da aba "Juros e CPMF"]`
