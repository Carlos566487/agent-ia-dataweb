# Base de Conhecimento RAG: Relatório de Aniversariantes

## Informações do Documento Original
- **Manual de Origem:** Relatorio de Aniversariantes.pdf
- **Módulo Principal:** Administrador / CRM
- **Série:** Pílulas Semanais (Versão 01.01 - Setembro/2024)
- **Elaboração:** Carlos Eduardo - Analista de Suporte e Implantação PDV
- **Homologação:** Lincoln Akira - Supervisor de TI

---

## 1. Resumo Estrutural do Manual (Árvore de Tópicos)
- Módulo Administrador
  - Guia Gerente (Gerente ADM)
    - Tabelas
      - Cliente (Análises: Cliente)
        - Conceito e Benefícios Comerciais / CRM
        - Passo a Passo de Emissão
          - Seleção da Tabela e Mês de Aniversário
          - Configuração de Colunas e Parâmetros (Identificador)
          - Execução da Consulta e Visualização da Lista

---

## 2. Chunks Estruturados para RAG

### [relatorio-aniversariantes_adm-crm_conceito_01]
**Metadados:**
```json
{
  "id": "relatorio-aniversariantes_adm-crm_conceito_01",
  "manual_origem": "Relatorio de Aniversariantes.pdf",
  "modulo": "Administrador / CRM",
  "assunto": "Marketing e Relacionamento com o Cliente",
  "subassunto": "Conceito do Relatório de Aniversariantes",
  "tipo_conteudo": "conceito",
  "titulo": "Finalidade e benefícios do relatório de clientes aniversariantes",
  "palavras_chave": ["aniversariantes", "marketing", "CRM", "fidelização", "relacionamento com o cliente"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**
**Contexto:** Módulo Administrador / CRM > Marketing e Relacionamento com o Cliente.

O sistema ERP conta com uma funcionalidade voltada ao setor de Marketing e Relacionamento com o Cliente (CRM) que possibilita a geração automática de relatórios de clientes que fazem aniversário em um mês específico. Essa ferramenta permite planejar campanhas personalizadas, estreitar laços e direcionar ofertas especiais aos clientes.

**Benefícios da funcionalidade:**
- **Mensagens personalizadas:** Envio planejado de mensagens de "Feliz Aniversário", demonstrando cuidado e atenção com o cliente.
- **Convite para visitar a loja:** Oportunidade de enviar um convite especial junto com a mensagem, estimulando o cliente a comparecer à unidade para retirar um brinde, usufruir de desconto exclusivo ou participar de uma campanha promocional.
- **Engajamento e fidelização:** Fortalecimento do vínculo de confiança com o consumidor e aumento real da probabilidade de recompra ao longo do tempo.
- **Implementação simplificada:** Configuração rápida e intuitiva pelo ERP, liberando a equipe comercial/marketing para focar no planejamento criativo e na estratégia do relacionamento.

**Perguntas frequentes relacionadas:**
- Como usar o relatório de aniversariantes para criar campanhas de marketing?
- Quais os principais benefícios comerciais do relatório de aniversariantes?
- O Dataweb permite extrair aniversariantes por mês com foco em fidelização?

**Imagens associadas:** nenhuma

---

### [relatorio-aniversariantes_adm_gerar-relatorio_02]
**Metadados:**
```json
{
  "id": "relatorio-aniversariantes_adm_gerar-relatorio_02",
  "manual_origem": "Relatorio de Aniversariantes.pdf",
  "modulo": "Administrador",
  "assunto": "Análises Gerenciais",
  "subassunto": "Emissão de Relatório de Clientes Aniversariantes",
  "tipo_conteudo": "procedimento",
  "titulo": "Como gerar o relatório de clientes aniversariantes do mês",
  "palavras_chave": ["gerente adm", "análise cliente", "aniversariantes do mês", "identificador de campos", "executar consulta"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-4",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Administrador > Guia GERENTE > Tabelas > Cliente.

**Pré-requisitos:** Permissão de acesso ao módulo `Administrador` e à guia `Gerente`.

**Passo a passo para emissão do relatório:**
1. Acesse o módulo `Administrador`.
2. Na barra de ícones e ferramentas superiores, clique na guia `GERENTE`.
3. No painel de navegação à esquerda, localize o agrupamento `Tabelas` e clique sobre a opção `Cliente` (abre a tela "Análises: Cliente").
4. No campo de filtro `Aniversário:`, clique na lista suspensa e selecione o mês desejado (ex.: "Setembro").
5. No topo da área de dados, clique no botão cinza `Identificador` para abrir o catálogo de seleção de colunas/atributos cadastrais do cliente.
6. Escolha e marque as caixas de seleção correspondentes aos campos que devem constar no relatório (ex.: `Nome`, `Fone res 1`, `Fone res 2`, `Celular`, `Fone com 1`, `Fone com 2`, `E-MAIL`, `Mês de aniversário`, `Dia do nascimento`, etc.).
7. Clique no botão de execução no topo da tela [REVISAR: o passo a passo textual indica "clique em <EXECUTAR COMANDO>", mas o rótulo do botão na interface do sistema é "Executar consulta"].
8. O sistema processará os registros e disponibilizará a relação dos clientes aniversariantes do mês escolhido, exibindo as colunas selecionadas e o totalizador geral de clientes encontrados no rodapé da grade.

**Perguntas frequentes relacionadas:**
- Onde fica a opção de relatório de aniversariantes no módulo Administrador?
- Como incluir números de telefone e e-mail no relatório de aniversariantes?
- Qual o nome do botão para processar a busca de aniversariantes na tela Análises: Cliente?

**Imagens associadas:**
- Figura 1 (pág. 2): Barra de navegação do Administrador destacando a guia `GERENTE`.
- Figura 2 (pág. 2): Painel esquerdo destacando a árvore `Tabelas > Cliente` e tela inicial de consulta.
- Figura 3 (pág. 2): Campo suspenso `Aniversário` aberto com as opções de meses do ano, destacando a seleção de "Setembro".
- Figura 4 (pág. 3): Detalhe com seta indicando a localização do botão retangular `Identificador`.
- Figura 5 (pág. 3): Painel completo de campos cadastrais selecionáveis (`Nome`, `Celular`, `E-MAIL`, etc.) e destaque no botão de execução superior.
- Figura 6 (pág. 4): Exibição do relatório gerado com a grade de clientes aniversariantes, datas, contatos e o contador final ("Clientes: 7071").

---

## 3. Glossário do Manual
- **Guia Gerente / Gerente ADM:** Módulo de inteligência gerencial e auditoria integrado ao módulo Administrador do sistema Dataweb, utilizado para consultas dinâmicas de vendas, estoques e cadastros.
- **Identificador:** Botão e funcionalidade presente nas consultas de análise que permite personalizar dinamicamente as colunas e atributos cadastrais visíveis no relatório.
- **Análises: Cliente:** Ferramenta de cruzamento e extração de dados da base central de clientes cadastrados na rede.

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Página 3 (Item 7):** O texto original orienta clicar no botão `<EXECUTAR COMANDO>`, entretanto o botão correspondente exibido no topo da tela (Figura 5) está rotulado oficialmente como `Executar consulta`.