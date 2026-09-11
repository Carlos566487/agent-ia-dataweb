# Base de Conhecimento RAG: Exportação de Arquivos XML de Notas Fiscais

## Informações do Documento Original
- **Manual de Origem:** Exportar XML.docx
- **Módulos Disponíveis:** Pedido / Ordem de Serviço / Caixa / Financeiro
- **Autor Original:** Implantação
- **Datação do Registro:** Há 2 meses (Atualizado)

---

## 1. Resumo Estrutural do Manual
- Módulo Pedido (ou Ordem de Serviço / Caixa / Financeiro)
  - Ferramentas
    - Manutenção de NF...
      - Definição de Empresa, Tipo de Intervalo e Datas
      - Pesquisa das Notas Fiscais
      - Exportação de Lote XML para Diretório Local

---

## 2. Chunks Estruturados para RAG

### [exportar-xml_pedido_procedimento_01]
**Metadados:**
```json
{
  "id": "exportar-xml_pedido_procedimento_01",
  "manual_origem": "Exportar XML.docx",
  "modulo": "Pedido / Ordem de Serviço / Caixa / Financeiro",
  "assunto": "Notas Fiscais",
  "subassunto": "Exportação de Arquivos XML",
  "tipo_conteudo": "procedimento",
  "titulo": "Como exportar arquivos XML de notas fiscais eletrônicas (NF-e)",
  "palavras_chave": ["exportar xml", "manutenção de nf", "nota fiscal eletrônica", "nfe", "xml emitidas", "contabilidade"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": true,
  "pagina_origem": "1",
  "revisar": true
}
```

**Conteúdo:**
**Contexto:** Módulo Pedido (ou Ordem de Serviço / Caixa / Financeiro) > Ferramentas > Manutenção de NF...

**Pré-requisitos:** Notas Fiscais Eletrônicas autorizadas, canceladas ou inutilizadas registradas no período.

**Passo a passo:**
1. Acesse o sistema pelo `MÓDULO PEDIDO` (ou pelos módulos `Ordem de Serviço`, `Caixa` ou `Financeiro`).
2. No menu superior, clique em `Ferramentas` e escolha `Manutenção de NF...`.
3. Na janela "Manutenção de notas fiscais", informe os parâmetros de consulta:
   - `Empresas:` selecione a loja desejada.
   - `Tipo de intervalo:` defina a referência temporal (ex.: `POR DATA EMISSÃO`).
   - `Intervalo de data de emissão:` defina as datas inicial e final (`de: DD/MM/AAAA até: DD/MM/AAAA`).
   - `Validar intervalo de notas`: marque a caixa de seleção se estiver disponível.
   - `Filtros / Situação`: selecione `TODAS` ou o status fiscal desejado.
4. Clique no botão `Pesquisar` (ícone de lupa).
5. O sistema listará a quantidade de notas emitidas e recebidas agrupadas por situação (Autorizada, Cancelada, Inutilizada, etc.).
6. Clique no botão `Exportar`.
7. Selecione a opção `Exportar para XML` no submenu.
8. Indique no computador a pasta de destino onde os arquivos deverão ser gravados.
9. Clique em `OK`.
10. Todos os arquivos XML das notas pesquisadas serão salvos no diretório indicado.

**Perguntas frequentes relacionadas:**
- Como salvar os arquivos XML das notas fiscais para enviar ao escritório de contabilidade?
- Em quais módulos do Dataweb consigo acessar a Manutenção de NF?
- Posso exportar XML de notas canceladas ou inutilizadas?

**Imagens associadas:**
- Imagem 1: Menu superior do Módulo Pedido com acesso a `Ferramentas > Manutenção de NF...`.
- Imagem 2: Janela "Manutenção de notas fiscais" com setas vermelhas indicando a parametrização de datas, a opção `Validar intervalo de notas`, o botão `Pesquisar` e o menu do botão `Exportar` desdobrado em `Exportar para XML`.

---

## 3. Glossário do Manual
- **Manutenção de NF:** Ferramenta operacional e fiscal do sistema destinada à administração, consulta de status, cancelamento, inutilização e exportação de documentos fiscais eletrônicos.
- **Arquivo XML:** Arquivo de formatação digital com assinatura eletrônica oficial que constitui a existência jurídica da Nota Fiscal Eletrônica (NF-e).

---

## 4. Pontos Sinalizados para Revisão (`[REVISAR]`)
- **Passo 3 do original:** O texto da instrução orienta selecionar o *"TIPO DE PERÍODO"*, porém a nomenclatura exata exibida na interface é `Tipo de intervalo`.