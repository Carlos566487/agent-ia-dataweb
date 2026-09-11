# Base de Conhecimento RAG: DRE e Fluxo de Caixa

## Informações do Documento Original
- **Manual de Origem:** DRE e Fluxo de Caixa (DRE.pdf / DRE_DATAWEB.pdf)
- **Módulo Principal:** Financeiro
- **Assunto:** DRE (Demonstrativo de Resultado do Exercício), Fluxo de Caixa e Gestão de Lançamentos
- **Observação de Origem:** Os arquivos de origem enviados (DRE.pdf e DRE_DATAWEB.pdf) são idênticos em conteúdo operacional, telas e diagramação. Processamento unificado para evitar duplicidade de chunks na base vetorial.

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Financeiro
  - DRE (Demonstrativo de Resultado do Exercício) e Fluxo de Caixa
    - Acesso ao DRE
    - Parâmetros de Geração (Filtros, Contas Bancárias e Período)
    - Estrutura e Apuração do Resultado do DRE
  - Lançamentos Financeiros (Plano de Contas e Contas a Pagar/Receber)
    - Inclusão de Lançamento Manual (Normal)
    - Pesquisa de Lançamentos no Plano de Contas
    - Alteração de Lançamento em Aberto (Alterar Parcela)
    - Baixa e Quitação de Lançamento (Baixar Parcela)

---

## 2. Chunks Estruturados para RAG

### [dre-fluxo-caixa_financeiro_acesso_01]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_acesso_01",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "DRE",
  "subassunto": "Acesso ao DRE",
  "tipo_conteudo": "procedimento",
  "titulo": "Onde encontrar e como acessar o DRE no Dataweb",
  "palavras_chave": ["DRE", "fluxo de caixa", "módulo financeiro", "acesso"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > DRE e Fluxo de Caixa > Acesso.

A ferramenta de DRE (Demonstrativo de Resultado do Exercício) e Fluxo de Caixa está localizada centralmente no módulo Financeiro do sistema Dataweb.

**Passo a passo:**
1. Abra o módulo `Financeiro`.
2. Na barra de botões de atalho superior (localizada logo abaixo do menu de texto e contendo opções como Plano, Emissão NF, Faturamento, Faturas, Conciliação, DRE, Relatórios, Bonificação e Ferramentas), clique no botão `DRE`.

**Perguntas frequentes relacionadas:**
- Onde encontro o DRE no Dataweb?
- Em qual módulo fica o relatório de Fluxo de Caixa?
- Qual botão devo clicar para abrir a tela de geração do DRE?

**Imagens associadas:**
- Página 2: Tela inicial do Módulo Financeiro (empresa OTICA), exibindo o menu textual superior e a barra de botões de atalho com retângulo vermelho destacando o botão `DRE`, além das abas inferiores ("Hoje", "Carta de cobrança", "Caixas", "Resumo financeiro", "Log do financeiro").

---

### [dre-fluxo-caixa_financeiro_filtros-periodo_02]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_filtros-periodo_02",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "DRE",
  "subassunto": "Parâmetros de geração - Filtros e Período",
  "tipo_conteudo": "procedimento",
  "titulo": "Como configurar os filtros e o período para gerar o relatório DRE",
  "palavras_chave": ["DRE", "parâmetros para geração do DRE", "período", "tipo de pesquisa", "data dos lançamentos", "transferências", "créditos", "contas bancárias", "empresas"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-3",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > DRE > Parâmetros de geração.

Ao clicar em DRE, o sistema abre a tela "Parâmetros para geração do DRE". Configure os critérios para extração do relatório conforme as diretrizes:

1. **Período / Ano (abas superiores):** Defina o intervalo de apuração utilizando a aba `Período` (informando os campos `Início` e `Fim`) ou selecione a aba `Ano`.
2. **Tipo de pesquisa:**
   - `Por período`: consolida os dados no intervalo definido. Se mais de uma empresa for selecionada, o sistema agrupa os totais.
   - `Por empresa`: separa e individualiza os valores por empresa/filial dentro do período selecionado.
3. **Data dos lançamentos e Data das transações:** Define a data-base que alimentará o relatório. De modo geral, utiliza-se a data de pagamento para os lançamentos e a data de encerramento para as transações de venda. Para que um lançamento seja computado, sua data de baixa deve estar contida dentro do período selecionado.
4. **Tipo de lançamentos:** Permite filtrar se o DRE computará apenas lançamentos oriundos de transações ou manuais. Recomenda-se selecionar a opção `Todos` para precisão do resultado financeiro.
5. **Exibir por:** Determina o agrupamento das colunas temporais (ex.: `Mês`).
6. **Transferências e Créditos:**
   - `Transferências`: define se lançamentos entre contas correntes internas entram no cálculo (ex.: opção "Não considerar").
   - `Créditos`: define a consideração ou não de lançamentos de créditos.
7. **Conta bancária:** Lista de contas financeiras da loja (ex.: BRADESCO, CAIXA EMPRESA). Marque a caixa de seleção de cada conta para incluir suas respectivas movimentações. Recomenda-se marcar sempre todas as contas da empresa para apuração contábil correta.
8. **Empresas:** Seleção das filiais/lojas participantes da consolidação (ex.: OTICA).
9. **Opções complementares:** Caixas de seleção `Mostrar fórmulas no DRE` e `Filtrar vendas com Nota/Cupom Fiscal`.
10. **Ações da tela:**
    - `Configurar`: exibe os parâmetros de fórmulas e configurações vigentes de cálculo.
    - `Imprimir`: envia a visualização para impressão física ou PDF.
    - `Gerar`: processa os filtros e exibe a grade do DRE na tela.

**Perguntas frequentes relacionadas:**
- Como filtro o DRE por um período específico?
- Qual a diferença entre pesquisar "Por período" e "Por empresa" no DRE?
- O que significa o campo "Data dos lançamentos" no DRE?
- Como faço para considerar apenas lançamentos manuais (ou apenas transações) no DRE?
- Onde marco quais contas bancárias entram no cálculo do DRE?

**Imagens associadas:**
- Páginas 2-3: Janela "Parâmetros para geração do DRE" com a aba `Período` ativa (01/04/2019 a 30/04/2019), `Data dos lançamentos` definida como "Pagamento", `Data das transações` como "Encerramento", `Tipo de lançamentos` como "Todos", `Exibir por` como "Mês", `Tipo de pesquisa` como "Por período", `Transferências` e `Créditos` como "Não considerar", contas "BRADESCO" e "CAIXA EMPRESA" selecionadas, empresa "OTICA" marcada e botões `Gerar`, `Configurar` e `Imprimir` no canto direito.

---

### [dre-fluxo-caixa_financeiro_resultado_03]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_resultado_03",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "DRE",
  "subassunto": "Resultado do relatório",
  "tipo_conteudo": "conceito",
  "titulo": "Como é estruturado o resultado do relatório DRE",
  "palavras_chave": ["DRE", "resultado", "receita operacional bruta", "receita líquida", "lucro bruto", "resultado operacional líquido"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "3",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > DRE > Resultado do relatório.

Após o clique no botão `Gerar`, o sistema exibe o Demonstrativo de Resultado em formato de grade estruturada, contendo as colunas `Descrição`, `%`, `Total` e colunas dinâmicas por intervalo (ex.: `abr/2019`).

**Estrutura hierárquica das contas apuradas:**
- **1. Receita Operacional Bruta**
  - 1.1. Acréscimos sobre vendas
  - 1.2. Deduções sobre vendas (1.2.1. Descontos | 1.2.2. Devoluções)
  - 1.3. Receita Líquida `{1}+{1.1}-{1.2}`
- **2. Receita operacional líquida `{1.3}`**
  - 2.1. CMV (Custo da Mercadoria Vendida)
  - 2.2. Lucro bruto `{2}-{2.1}`
- **3. Lucro bruto `{2.2}`**
  - 3.1. Despesas com ocupação
  - 3.2. Despesas com comunicação e informática
  - 3.3. Despesas com pessoal
  - 3.4. Despesas com publicidade
  - 3.5. Despesas financeiras operacionais
  - 3.6. Despesas financeiras não operacionais
  - 3.7. Despesas com operação (expediente)
  - 3.8. Fornecedores de serviços
  - 3.9. Manutenção e conservação
  - 3.10. Investimentos
  - 3.11. Despesas e retiradas sócios
  - 3.12. Despesas e taxas bancárias
  - 3.13. Impostos / taxas / contribuições
- **4. Resultado operacional líquido `{3}-{3.1}`**

**Observações operacionais:**
- Quando a opção `Mostrar fórmulas no DRE` está ativada, cada linha exibe os identificadores de composição matemática entre chaves `{ }`.
- Para sair da consulta, clique no botão `Fechar` posicionado no canto inferior direito da tela de resultados.

**Perguntas frequentes relacionadas:**
- Como o Dataweb calcula a Receita Líquida no DRE?
- O que compõe o "Resultado operacional líquido" no relatório DRE?
- É possível ver a fórmula matemática de cálculo de cada linha do DRE?

**Imagens associadas:**
- Página 3: Grade de "Resultados" do DRE exibindo cabeçalho de período `abr/2019` com valores de Receita Operacional Bruta (R$ 34.501,90), Receita Líquida (R$ 38.739,82), CMV (R$ 6.218,72), Lucro Bruto (R$ 32.521,10), despesas categorizadas de 3.1 a 3.13 e o Resultado Operacional Líquido final (R$ 10.914,02), com o botão `Fechar` em destaque.

---

### [dre-fluxo-caixa_financeiro_criar-lancamento-manual_04]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_criar-lancamento-manual_04",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "Lançamentos",
  "subassunto": "Criando Lançamento Manual",
  "tipo_conteudo": "procedimento",
  "titulo": "Como criar um lançamento manual no plano de contas",
  "palavras_chave": ["novo lançamento", "plano de contas", "conta classificação", "cliente fornecedor", "banco bloqueto previsão", "lançamento manual"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "4",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Lançamentos > Criação manual.

Para incluir manualmente um título a pagar ou a receber no sistema:

**Passo a passo:**
1. Acesse o `Plano de contas`.
2. Clique com o botão direito do mouse sobre qualquer área livre da grade de lançamentos.
3. No menu de contexto exibido, selecione a opção `Novo Lançamento...`.
4. Na janela "Lançamento (Normal)", preencha os campos obrigatórios:
   - `Empresa`: selecione a loja responsável (ex.: "OTICA").
   - `Conta classificação`: selecione o plano de contas contábil correspondente (exemplo: `ALUGUEL (PAGAR - 2.2.1)`).
   - `Cliente / fornecedor`: informe a razão social ou nome (exemplo: `IMOBILIARIA`).
   - `Número documento`: informe o identificador fiscal/boleto ou crie um código de referência livre (exemplo: `ALUG-06-19`).
5. No bloco `Dados da parcela`:
   - `Data de emissão`: data de competência da despesa.
   - `Data de vencimento`: data prevista para liquidação.
   - Selecione a opção `Pagar` ou `Receber`.
   - `Valor original`: valor bruto nominal do título.
   - Preencha, se houver, `Desconto`, `Juros` ou `Observações`.
6. No bloco `Dados da forma de pagamento`:
   - Selecione no campo `Forma` a opção `Banco/Bloqueto/Previsão`. **Atenção:** Esta forma de pagamento deve sempre ser utilizada para despesas futuras cuja forma definitiva de liquidação ainda não esteja definida.
   - No campo `Conta`, informe a conta bancária do sistema atrelada ao lançamento (exemplo: `BRADESCO | OTICA`).
7. Após conferir os dados, clique no botão `OK` para gravar o lançamento.

**Observações:**
- A forma de pagamento e a conta bancária informadas no momento do cadastro funcionam como previsão e podem ser alteradas sem restrições no momento da baixa real do título.
- A janela de cadastro também apresenta os botões diretos `Receber` e `Baixar` na parte inferior, caso a quitação ocorra no ato.

**Perguntas frequentes relacionadas:**
- Como cadastro manualmente uma conta a pagar ou a receber no Dataweb?
- O que é a forma de pagamento "Banco/Bloqueto/Previsão" e quando devo usá-la?
- É possível mudar depois a conta bancária de um lançamento já criado?

**Imagens associadas:**
- Página 4 (Superior): Tela "Plano de contas" aberta com o menu do botão direito em destaque apontando para a opção `Novo lançamento...`.
- Página 4 (Inferior): Janela modal "Lançamento (Normal)" preenchida com Conta classificação "ALUGUEL", Fornecedor "IMOBILIARIA", Documento "ALUG-06-19", Vencimento "10/06/2019", Valor "2.500,00", Forma "Banco/Bloqueto/Previsão" e Conta "BRADESCO | OTICA".

---

### [dre-fluxo-caixa_financeiro_pesquisa-lancamentos_05]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_pesquisa-lancamentos_05",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "Lançamentos",
  "subassunto": "Pesquisa de Lançamentos",
  "tipo_conteudo": "procedimento",
  "titulo": "Como pesquisar um lançamento no financeiro",
  "palavras_chave": ["pesquisa de lançamentos", "plano de contas", "pesquisar F3", "situação aberta", "lançamento vencido"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Lançamentos > Pesquisa.

Para localizar títulos específicos cadastrados no financeiro:

**Passo a passo:**
1. Acesse o `Plano de contas`.
2. Utilize o painel lateral retrátil intitulado `Pesquisa`. Caso ele não esteja visível, clique no botão `Pesquisa` localizado na barra de ferramentas superior da janela.
3. Preencha um ou mais parâmetros de busca para refinar os resultados:
   - `Empresa`: filial da consulta (ex.: "OTICA").
   - `Situação`: selecione `(Todos)`, `Abertos` ou `Baixados`.
   - `Tipo`: marque `Pagar` ou `Receber`.
   - `Cliente/Fornecedor`: informe o nome da entidade (ex.: "IMOBILIARIA").
   - `Datas`: defina filtros de `Vencimento` ou `Pagamento`.
4. Clique no botão `Pesquisar (F3)`.
5. Os lançamentos correspondentes aos critérios serão exibidos na grade principal à direita.

**Regras visuais e de status:**
- **Lançamento em aberto:** É identificado pela ausência de preenchimento nos campos de data de pagamento ou data de recebimento.
- **Lançamento vencido:** Os lançamentos cuja data de vencimento for anterior à data atual e que ainda estejam em aberto são destacados visualmente com a cor **vermelha**.

**Perguntas frequentes relacionadas:**
- Como encontro um lançamento específico no financeiro do Dataweb?
- Como sei se um lançamento já foi pago ou ainda está em aberto?
- Por que alguns lançamentos aparecem em vermelho no plano de contas?

**Imagens associadas:**
- Página 5: Painel lateral de pesquisa com preenchimento de Fornecedor "IMOBILIARIA", Tipo "Pagar", Vencimento "10/06/2019" e destaque no botão `Pesquisar (F3)`. À direita, exibição da linha do título com valor de R$ 2.500,00 e totalizadores de saldo no rodapé.

---

### [dre-fluxo-caixa_financeiro_alterar-parcela_06]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_alterar-parcela_06",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "Lançamentos",
  "subassunto": "Alteração de Lançamento",
  "tipo_conteudo": "procedimento",
  "titulo": "Como alterar um lançamento (Alterar parcela) no financeiro",
  "palavras_chave": ["alterar parcela", "plano de contas", "tela principal do financeiro", "contas a pagar e receber", "lançamento em aberto"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "5-6",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Lançamentos > Alteração.

**Regra mandatória:** O sistema permite a edição e alteração de informações **exclusivamente** para lançamentos que estejam na situação **aberta** (não quitados).

Existem dois caminhos operacionais para alterar uma parcela:

- **Opção 1 — Pela tela principal do Financeiro (no dia do vencimento):**
  1. Na tela principal do módulo Financeiro, localize o bloco `Contas a pagar e receber` (que lista automaticamente os vencimentos do dia corrente).
  2. Localize o título desejado, clique com o botão direito sobre ele e selecione a opção `Alterar parcela...`.

- **Opção 2 — Pelo Plano de contas (qualquer vencimento):**
  1. Acesse o `Plano de contas` e localize o lançamento através dos filtros de pesquisa.
  2. Dê um duplo clique com o botão esquerdo sobre a linha do lançamento OU clique com o botão direito sobre ele e selecione `Alterar parcela...`.
  3. Atualize as informações necessárias na janela de lançamento e clique em `OK` para salvar.

**Perguntas frequentes relacionadas:**
- Como edito um lançamento financeiro já cadastrado no Dataweb?
- É possível alterar um lançamento que já foi baixado/pago?
- Onde consultar rapidamente os lançamentos que vencem no dia de hoje?

**Imagens associadas:**
- Páginas 5-6: Tela principal do módulo Financeiro destacando a grade inferior de `Contas a pagar e receber`, com o botão direito sobre o título "ALUG-06-19" abrindo as opções `Alterar parcela...` e `Baixar parcela...`. Detalhe complementar da tela do Plano de Contas com a seleção de `Alterar parcela...`.

---

### [dre-fluxo-caixa_financeiro_baixa-lancamento_07]
**Metadados:**
```json
{
  "id": "dre-fluxo-caixa_financeiro_baixa-lancamento_07",
  "manual_origem": "DRE e Fluxo de Caixa",
  "modulo": "Financeiro",
  "assunto": "Lançamentos",
  "subassunto": "Baixa de Lançamento",
  "tipo_conteudo": "procedimento",
  "titulo": "Como dar baixa em um lançamento (Baixar parcela) no financeiro",
  "palavras_chave": ["baixar parcela", "baixa de lançamento", "forma de pagamento", "desconto", "juros", "conta bancária", "data de pagamento"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "7",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Lançamentos > Baixa de títulos.

A baixa (liquidação/pagamento/recebimento) pode ser executada tanto pela grade de `Contas a pagar e receber` da tela principal do Financeiro quanto pela interface do `Plano de contas`.

**Passo a passo:**
1. Localize o lançamento em aberto desejado.
2. Clique com o botão direito do mouse sobre ele e selecione a opção `Baixar parcela...` (localizada dentro da seção "Baixa" do menu).
3. O sistema abrirá a janela "Baixar parcelas", contendo os dados do documento e campos de composição de valores:
   - Se aplicável, preencha os campos `Desconto` ou `Juros` negociados. O sistema atualizará automaticamente o `Total a pagar`.
4. No quadro `Dados da forma de pagamento`:
   - **Confirme ou altere a Forma de pagamento:** Sempre confira o meio de pagamento real utilizado para liquidar o título.
   - Informe a `Conta` bancária correspondente de onde saiu ou entrou o recurso financeiro (ex.: `BRADESCO | OTICA`).
   - Caso possua créditos de fornecedor/cliente, o valor disponível será exibido no campo `Crédito disponível`.
5. No quadro `Dados da baixa`:
   - Confirme o nome do `Pagador`.
   - Defina a `Data de pagamento` efetiva da transação.
6. Clique no botão `OK` para consolidar e baixar a parcela no sistema.

**Observação:**
- É nesta tela de baixa que a previsão de conta bancária e de forma de pagamento cadastradas no momento do lançamento inicial podem ser corrigidas e efetivadas.

**Perguntas frequentes relacionadas:**
- Como faço a baixa (pagamento/recebimento) de um lançamento no Dataweb?
- É possível aplicar desconto ou juros no momento da baixa de uma conta?
- Como alterar a conta bancária utilizada na quitação de um lançamento?

**Imagens associadas:**
- Página 7: Menu de contexto sobre o lançamento da IMOBILIARIA destacando a opção `Baixar parcela...` e janela modal "Baixar parcelas" com o valor de R$ 2.500,00, seleção de Forma "Banco/Bloqueto/Previs...", Conta "BRADESCO | OTICA", Pagador "OTICA", Data de pagamento "10/06/2019" e botões `OK` e `Cancelar`.

---

## 3. Glossário do Manual
- **DRE (Demonstrativo de Resultado do Exercício):** Relatório contábil e gerencial que confronta receitas brutas, deduções, custos operacionais (CMV) e despesas fixas/variáveis para apurar o resultado operacional líquido de um período.
- **Plano de contas:** Módulo operacional central do Financeiro onde são realizadas a consulta, criação manual, manutenção e quitação de títulos a pagar e a receber da empresa.
- **Lançamento:** Registro financeiro individualizado de uma obrigação a pagar ou direito a receber, atrelado a um fornecedor/cliente, centro de custo e conta de classificação.
- **Conta classificação:** Estrutura contábil padronizada que identifica a natureza da receita ou despesa (ex.: ALUGUEL, DESPESAS COM PESSOAL).
- **Banco/Bloqueto/Previsão:** Modalidade transitória de forma de pagamento recomendada para lançamentos de despesas futuras cuja forma definitiva de liquidação ainda não esteja definida.
- **Alterar parcela:** Funcionalidade de edição de valores, vencimentos ou classificações de um lançamento, habilitada unicamente enquanto o título estiver com status em aberto.
- **Baixar parcela:** Registro de quitação financeira definitiva no sistema, onde é informada a conta bancária real de débito/crédito e eventuais juros ou descontos aplicados.
- **CMV (Custo da Mercadoria Vendida):** Conta redutora da receita bruta no DRE que quantifica o custo de aquisição dos produtos e insumos comercializados no período.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- *Nenhum ponto sinalizado como `[REVISAR]` neste manual.*
- **Nota de Origem do Material:** Conforme informado no manual, os arquivos `DRE.pdf` e `DRE_DATAWEB.pdf` apresentavam conteúdo idêntico, tendo sido unificados sem divergências conceituais ou operacionais.