# Base de Conhecimento RAG: Tipos de Carnê

## Informações do Documento Original
- **Manual de Origem:** TIPOS DE CARNÊ.pdf
- **Módulo Principal:** Financeiro
- **Série / Versão:** Pílulas Semanais (VER 01.01 - Setembro de 2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Financeiro
  - Gestão e Vantagens da Criação de Tipos de Carnê
  - Acesso ao Cadastro de Tipos de Carnê
  - Configuração do Carnê (Parâmetros Comerciais, Baixa, Juros e Multa)

---

## 2. Chunks Estruturados para RAG

### [tipos-carne_financeiro_conceito_01]
**Metadados:**
```json
{
  "id": "tipos-carne_financeiro_conceito_01",
  "manual_origem": "TIPOS DE CARNÊ.pdf",
  "modulo": "Financeiro",
  "assunto": "Formas de Pagamento",
  "subassunto": "Gestão e Utilidade dos Tipos de Carnê",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral e finalidade da gestão de Tipos de Carnê no Dataweb",
  "palavras_chave": ["tipos de carnê", "crediário próprio", "comissionamento", "juros e multa", "contas bancárias", "financeiro"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Formas de Pagamento > Tipos de Carnê.

A funcionalidade de criação e personalização de **Tipos de Carnê** permite aos gestores e diretores administrar de forma totalmente independente cada modalidade de crediário próprio ou terceirizado aceito na rede de lojas.

**Vantagens e flexibilidade da parametrização:**
- **Regras de comissionamento distintas:** aplicação de alíquotas de comissão customizadas para vendedores conforme a modalidade do carnê transacionado;
- **Políticas de juros e multas individuais:** definição de incidência própria de taxas financeiras por atraso para cada modelo de contrato;
- **Contas bancárias exclusivas:** associação do recebimento a contas bancárias específicas da empresa;
- **Segregação de riscos:** separação clara no PDV entre carnês próprios garantidos, financiados por instituições parceiras ou sem garantia.

**Perguntas frequentes relacionadas:**
- Por que cadastrar tipos de carnê diferentes no Dataweb?
- É possível definir taxas de juros e regras de comissão distintas para cada carnê?
- Como a criação de tipos de carnê auxilia na gestão da diretoria?

**Imagens associadas:** nenhuma

---

### [tipos-carne_financeiro_cadastro_02]
**Metadados:**
```json
{
  "id": "tipos-carne_financeiro_cadastro_02",
  "manual_origem": "TIPOS DE CARNÊ.pdf",
  "modulo": "Financeiro",
  "assunto": "Cadastros Financeiros",
  "subassunto": "Inclusão e Configuração de Tipo de Carnê",
  "tipo_conteudo": "procedimento",
  "titulo": "Como cadastrar e configurar um novo tipo de carnê no módulo Financeiro",
  "palavras_chave": ["cadastrar carnê", "tipo de carnê", "comissionamento", "valor máximo", "baixa automática", "confissão de dívida"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1-2",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Cadastro > Tipo de carnê...

**Pré-requisitos:** Permissão de acesso administrativo ao módulo `Financeiro`.

**Passo a passo:**
1. No módulo `Financeiro` do sistema COMMERCIO, acesse o menu superior `Cadastro`.
2. Clique na opção `Tipo de carnê...`.
3. Na janela "Financeiras/Tipos de carnê", clique no botão `Novo` da barra superior de ferramentas.
4. Na aba `Carnê`, configure os campos de parametrização:
   - `1 - Nome:` digite a identificação oficial do modelo de carnê (ex.: `CARNE PROPRIO`, `CARNE GARANTIDO`, `CARNE DA FINANCEIRA "Y"`);
   - `2 - Tipo Comissionamento:` selecione o critério temporal de incidência da comissão do vendedor entre `Data de Emissão` ou `Data de Pagamento`;
   - `3 - Valor máximo:` informe o limite teto monetário permitido para vendas nesta modalidade (se não houver teto, deixe em branco ou zero);
   - `4 - Ativo:` marque a caixa de seleção para habilitar o uso do carnê na frente de caixa;
   - `5 - Regras operacionais e financeiras`: marque as opções pertinentes:
     - `Baixa automática`: realiza a liquidação imediata da parcela no sistema no momento da transação;
     - `Imprimir confissão`: habilita a emissão automática do termo de confissão de dívida para assinatura do cliente;
     - `Calcular juros`: ativa a aplicação de taxa de juros sobre parcelas recebidas em atraso;
     - `Calcular multa`: ativa a incidência de multa por atraso no vencimento.
5. Clique no botão `Gravar` (6) para salvar o cadastro.
6. O novo carnê estará disponível para operação no módulo Caixa e habilitado para receber regras específicas na gestão de comissionamento de vendas.

**Perguntas frequentes relacionadas:**
- Onde cadastrar uma nova modalidade de carnê no Dataweb?
- O que muda ao selecionar "Data de Emissão" ou "Data de Pagamento" no comissionamento do carnê?
- Como ativar a impressão da confissão de dívida no carnê?

**Imagens associadas:**
- Página 1: Menu superior do COMMERCIO Financeiro expandindo `Cadastro` com seta vermelha em `Tipo de carnê...`.
- Página 2: Janela "Financeiras/Tipos de carnê" destacando os campos de 1 a 6 (Nome, Tipo Comissionamento, Valor máximo, Ativo, checkboxes de regras e botão Gravar) e tabela inferior de "Itens cadastrados" com modelos já homologados no sistema.

---

## 3. Glossário do Manual
- **Tipo de Carnê:** Entidade cadastral que parametriza as regras contratuais, fiscais e financeiras de uma modalidade de crediário no PDV.
- **Tipo Comissionamento (Data de Emissão):** A comissão do colaborador é computada e liberada no momento em que a venda é realizada e faturada.
- **Tipo Comissionamento (Data de Pagamento):** A comissão é apurada somente conforme as parcelas do carnê forem efetivamente pagas pelo cliente.
- **Imprimir Confissão:** Impressão de instrumento jurídico em que o consumidor declara formalmente a dívida assumida perante a ótica.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 1 (Sumário):** No sumário da página 1, o item está grafado sem o caractere separador usual: *"MÓDULO FINANCEIRO  CADASTRO CARNÊ"*.
- **Página 2:** O título da tela na interface do sistema é `Financeiras/Tipos de carnê`, embora nos menus e no texto do manual seja referenciada como "Tipo de carnê" ou "Configuração do CARNÊ".