# Base de Conhecimento RAG: Relatório de Vendas de Produtos por Marca

## Informações do Documento Original
- **Manual de Origem:** RELATÓRIO DE VENDAS DE PRODUTOS POR MARCA.pdf
- **Módulo Principal:** Financeiro
- **Versão:** 01.01 (24-set-2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Financeiro
  - Relatórios e Gráficos
    - Relatórios
      - Vendas
        - Vendas - Produtos (Versão 2016) - Vendas de produtos e serviços
          - Visão Geral e Benefícios Estratégicos
          - Acesso ao Menu de Relatórios
          - Seleção do Relatório de Vendas de Produtos
          - Parametrização de Filtros (Período, Empresa, Agrupamento e Marca)
          - Visualização e Análise do Relatório

---

## 2. Chunks Estruturados para RAG

### [vendas-marca_financeiro_conceito_01]
**Metadados:**
```json
{
  "id": "vendas-marca_financeiro_conceito_01",
  "manual_origem": "RELATÓRIO DE VENDAS DE PRODUTOS POR MARCA.pdf",
  "modulo": "Financeiro",
  "assunto": "Vendas de Produtos por Marca",
  "subassunto": "Conceito e Benefícios Comerciais",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral e funcionalidades do relatório de vendas por marca",
  "palavras_chave": ["vendas por marca", "desempenho comercial", "rentabilidade", "mix de produtos", "tomada de decisão"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Relatório de Vendas de Produtos por Marca.

O Relatório de Vendas de Produto por Marca é uma ferramenta essencial para gestores e equipes comerciais que desejam obter uma visão aprofundada e segmentada do desempenho de vendas com base nas marcas comercializadas.

**Funcionalidades e benefícios comerciais:**
- **Visão segmentada por marca:** Apresenta divisão transparente das vendas de cada marca, facilitando o diagnóstico das marcas líderes de mercado e das que necessitam de incentivo comercial.
- **Desempenho de vendas:** Exibe o volume de vendas em quantidade de unidades físicas e em valor financeiro, possibilitando análise comparativa direta entre diferentes fabricantes.
- **Métricas de rentabilidade:** Pode ser configurado para exibir margens de lucro e rentabilidade associada a cada linha de produtos.
- **Suporte à tomada de decisão:** Apoia os setores de compras e marketing no ajuste de compras futuras, reposição estratégica e concentração de verbas promocionais.

**Perguntas frequentes relacionadas:**
- Para que serve o relatório de vendas de produtos por marca no Dataweb?
- É possível comparar o volume vendido e o faturamento entre marcas diferentes?
- Como os gestores podem utilizar o relatório de marcas para decisões de compra?

**Imagens associadas:** nenhuma

---

### [vendas-marca_financeiro_gerar-relatorio_02]
**Metadados:**
```json
{
  "id": "vendas-marca_financeiro_gerar-relatorio_02",
  "manual_origem": "RELATÓRIO DE VENDAS DE PRODUTOS POR MARCA.pdf",
  "modulo": "Financeiro",
  "assunto": "Relatórios de Vendas",
  "subassunto": "Parametrização do Relatório de Produtos e Serviços por Marca",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerar o relatório de vendas de produtos e serviços agrupado por marca",
  "palavras_chave": ["vendas de produtos", "agrupamento por marca", "marca armação", "tipo armação", "filtro de classificações"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-5",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Financeiro > Relatórios e Gráficos > Relatórios > Vendas.

**Pré-requisitos:** Permissão de acesso ao módulo `Financeiro` e produtos classificados por marca e tipo no cadastro.

**Passo a passo:**
1. No módulo `Financeiro` do DATAWEB, clique na opção `Relatórios e Gráficos` e escolha `Relatórios`.
2. Na árvore de `Tipo Relatório`, localize e selecione a opção `Vendas`.
3. Na lista expandida de relatórios de vendas, selecione a opção `Vendas - Produtos (Versão 2016) -Vendas de produtos e serviços)`.
4. No painel lateral direito, configure rigorosamente os critérios de filtro:
   - `Período`: informe o intervalo de datas (ex.: `01/07/2024` a `24/09/2024`) e em `Considerar intervalo` selecione `Data de aprovação`.
   - `Empresa`: selecione as lojas que deseja consultar marcando as caixas correspondentes (ex.: `DINIZ PRIMITIVA I`, `DINIZ PRIMITIVA II`).
   - `Agrupamento`: no quadro de agrupamentos disponíveis, dê duplo clique sobre os seguintes itens, respeitando estritamente a ordem indicada para incluí-los em `Agrupamentos selecionados`:
     1. `Empresa`
     2. `Marca armação`
     3. `Tipo armação`
   - `Classificações de produtos`:
     - No campo `Tipo de classificação:`, selecione a opção `Marca armação`.
     - No campo de marca (abaixo), clique na seta de seleção e escolha a marca desejada (exemplo do manual: `DII COLLECTION`) [REVISAR: no formulário de filtro da captura de tela está digitado "DEI COLLECTION", enquanto na listagem do combo exibe "DII COLLECTION"].
5. Clique no botão `Visualizar` na barra superior de ações.
6. O sistema renderizará a tela de visualização demonstrando:
   - Estrutura hierárquica por Empresa > Marca (`DII COLLECTION`) > Tipo de armação (`ARMACAO` e `OCULOS SOLAR`);
   - Colunas: `Transações`, `Quantidade vendida`, `Venda bruta` e `Venda líquida`;
   - Totalizadores gerais: `Total de Transações`, `Quantidade total de produtos/serviços`, `Total de V.Bruta`, `Total de V.Líquida` e `Nº de registros desse relatório`.

**Perguntas frequentes relacionadas:**
- Qual ordem exata de agrupamentos deve ser usada no relatório de vendas por marca?
- Como filtrar apenas uma marca de armação específica no relatório de vendas?
- Como visualizar a separação entre armações receituário e óculos solares no relatório?

**Imagens associadas:**
- Página 2: Menus do módulo Financeiro indicando `Relatórios e gráficos > Relatórios`.
- Página 3: Seleção do submenu `Vendas` e destaque no item `Vendas - Produtos (Versão 2016) -Vendas de produtos e serviços)`.
- Página 4: Telas de parametrização detalhadas com seleção de Período (Data de aprovação), seleção de Lojas em Empresa, ordem de itens no quadro Agrupamentos e preenchimento de Classificações de produtos com `Marca armação` e `DII COLLECTION`.
- Página 5: Destaque no botão superior `Visualizar` e tela final do relatório gerado com os agrupamentos por empresa, marca e tipo de armação com suas respectivas vendas brutas e líquidas.

---

## 3. Glossário do Manual
- **Venda Bruta:** Faturamento total registrado no faturamento da transação comercial antes de quaisquer descontos.
- **Venda Líquida:** Valor monetário total efetivamente apurado após aplicação de descontos comerciais concedidos ao cliente.
- **Agrupamentos:** Estrutura hierárquica que define como as linhas e subtotais do relatório serão escalonados na tela de visualização e impressão.
- **Classificações de produtos:** Parâmetros cadastrais que organizam as mercadorias por atributos operacionais (marca da armação, tipo de aro, material e fabricante).

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 4:** No campo de filtro por marca, o texto explicativo indica selecionar `DII COLLECTION`, porém a digitação visível na caixa de texto do filtro da captura de tela mostra `DEI COLLECTION`.