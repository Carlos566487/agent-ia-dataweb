# Base de Conhecimento RAG: Programação de Contas a Pagar

## Informações do Documento Original
- **Manual de Origem:** PROGRAMAÇÃO DE CONTAS.pdf
- **Módulo Principal:** Financeiro
- **Série / Versão:** Pílulas Semanais (VER 26.08 - Agosto de 2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Financeiro Dataweb
  - Introdução e Finalidade Operacional de Lançamentos Recorrentes
  - Acesso à Ferramenta de Programação de Contas a Pagar
  - Geração dos Lançamentos em Lote (Parâmetros e Conferência)

---

## 2. Chunks Estruturados para RAG

### [programacao-contas_financeiro_conceito_01]
**Metadados:**
```json
{
  "id": "programacao-contas_financeiro_conceito_01",
  "manual_origem": "PROGRAMAÇÃO DE CONTAS.pdf",
  "modulo": "Financeiro",
  "assunto": "Contas a Pagar",
  "subassunto": "Conceito e Vantagens da Programação de Contas",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral e vantagens da ferramenta de programação de contas a pagar",
  "palavras_chave": ["programação de contas", "lançamentos recorrentes", "contas a pagar", "automação financeira", "pagamentos em lote"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Contas a Pagar > Programação de Contas.

A ferramenta de programação de contas a pagar permite a geração automatizada de lançamentos financeiros recorrentes com cobertura de 1 a 2 anos em um único processo.

**Aplicações práticas e flexibilidade:**
- Indicada para despesas contínuas com periodicidade mensal, quinzenal, semanal ou intervalos customizados mais longos (como contratos de locação imobiliária, contas de consumo de água, energia elétrica, taxas de condomínio e prestadores de serviço);
- Elimina a necessidade de inclusão manual mês a mês de parcelas previsíveis;
- Disponibiliza grade prévia para auditoria e revisão dos valores e vencimentos antes de efetivar os lançamentos na conta classificação do plano de contas.

**Perguntas frequentes relacionadas:**
- Para que serve a ferramenta de programação de contas no Dataweb?
- É possível programar contas a pagar para períodos de até 2 anos de uma só vez?
- Quais tipos de despesas são recomendadas para cadastro na programação recorrente?

**Imagens associadas:** nenhuma

---

### [programacao-contas_financeiro_procedimento_02]
**Metadados:**
```json
{
  "id": "programacao-contas_financeiro_procedimento_02",
  "manual_origem": "PROGRAMAÇÃO DE CONTAS.pdf",
  "modulo": "Financeiro",
  "assunto": "Contas a Pagar",
  "subassunto": "Parametrização e Geração de Lançamentos em Lote",
  "tipo_conteudo": "procedimento",
  "titulo": "Como programar e gerar lançamentos de contas a pagar em lote no financeiro",
  "palavras_chave": ["programação de contas a pagar", "gerar lançamentos", "conta classificação", "periodicidade", "vencimento", "aplicar"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Ferramentas > Programação de contas a pagar e receber > Programar contas a pagar.

**Pré-requisitos:** Plano de contas configurado, conta classificação definida e fornecedor cadastrado.

**Passo a passo:**
1. No módulo `Financeiro`, clique no menu superior `Ferramentas` (1).
2. Posicione o cursor sobre `Programação de contas a pagar e receber` (2).
3. Selecione a opção `Programar contas a pagar...` (3) [REVISAR: o texto do manual indica "Programação de contas a pagar", mas o menu na tela é rotulado como "Programar contas a pagar..."].
4. Na tela "Programação de contas pagar", configure os campos do bloco `Dados principais`:
   - `1 - Empresa`: selecione a filial em que os títulos serão gerados (permite selecionar uma loja diferente da empresa logada no momento);
   - `2 - Classificação`: selecione a Conta Classificação contábil de destino (ex.: "Aluguel");
   - `3 - Número do Documento`: informe um identificador padrão para auxiliar na busca (campo opcional, ex.: "ALUGUEL");
   - `4 - Dia do Vencimento`: defina o dia fixo do mês para vencimento das parcelas;
   - `5 - Cliente/Fornecedor`: selecione a entidade credora (ex.: imobiliária, concessionária de água, luz ou condomínio);
   - *(Outros campos visíveis)*: `Conta bancária` e `Forma de pagamento` (ex.: "Banco/Bloqueto").
5. No bloco `Programação dos lançamentos`, configure a periodicidade e os valores (6):
   - Intervalo de datas/anos (ex.: de 2023 a 2024);
   - Periodicidade do ciclo;
   - Valor monetário de cada parcela (ex.: R$ 5.000,00).
6. Configure opções avançadas clicando em `Mais opções` (7):
   - Definir uma `Observação do lançamento` padrão para todas as parcelas;
   - Aplicar regras de vencimento: `Lançar como previsão`, `Somente dias úteis` e `Data de emissão igual à data de vencimento`.
7. Clique no botão superior `Gerar lançamentos` (8): o sistema gerará a grade informativa com a lista completa de parcelas calculadas para conferência visual.
8. Após conferir os registros na tabela, clique no botão `Aplicar` (9): todos os lançamentos serão efetivados na conta classificação informada.

**Perguntas frequentes relacionadas:**
- Como cadastrar as parcelas do aluguel do ano inteiro de forma automática no Dataweb?
- Posso programar contas a pagar para uma empresa diferente da loja em que estou conectado?
- O que faz a opção "Somente dias úteis" na programação de contas?

**Imagens associadas:**
- Página 2 (Superior): Menus do COMMERCIO Financeiro com numeração indicativa: `Ferramentas (1) > Programação de contas a pagar e receber (2) > Programar contas a pagar... (3)`.
- Página 2 (Inferior): Janela "Programação de contas pagar" com os campos de 1 a 9 demarcados, demonstrando parametrização de aluguel para "IMOBILIARIA ALUGUEL" no valor de R$ 5.000,00 e grade gerada com 13 parcelas de 2023 a 2024 prontas para aplicação.

---

## 3. Glossário do Manual
- **Programação de Contas:** Ferramenta do Financeiro que cria lançamentos múltiplos e futuros no plano de contas baseados em periodicidade e parâmetros fixos.
- **Conta Classificação:** Conta contábil pertencente ao plano de contas que categoriza a despesa (ex.: Aluguel, Água, Luz).
- **Lançar como Previsão:** Parâmetro que sinaliza o título financeiro como expectativa de despesa, podendo ser confirmado na data de vencimento real.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 2:** O texto instrucional cita *"Programação de contas a pagar"*, enquanto o nome oficial do submenu exibido na captura de tela é `Programar contas a pagar...`.
- **Página 2:** O título da janela aberta no sistema grafa *"Programação de contas pagar"* (sem a preposição "a").