# Base de Conhecimento RAG — Periféricos Compatíveis Dataweb

> Documento de origem: **Comparativo_Perifericos_Dataweb.docx** (comparação entre os manuais "Periféricos Compatíveis 2019" — última revisão junho/2019 — e "Periféricos Compatíveis 2023" — última revisão junho/2022, PDF de 04/set/2023).
>
> **Nota importante sobre a natureza deste manual:** diferente de um manual operacional (que traria passo a passo de telas do sistema), este documento é uma **referência técnica de hardware/periféricos compatíveis** com o sistema Dataweb. Por isso, a maioria dos chunks abaixo é do tipo `pré-requisito`, `conceito` ou `aviso`, e não `procedimento`. Nenhuma imagem foi referenciada no documento de origem.

---

## 1. Resumo estrutural do manual (árvore de tópicos reconstituída)

```
Comparativo — Periféricos Compatíveis Dataweb
├── 1. Visão geral
├── 2. Principais diferenças (tabela comparativa 2019 x 2023)
│   ├── Computadores — Servidor
│   ├── Computadores — Estação
│   ├── Sistema Operacional
│   ├── ECF (impressora fiscal)
│   ├── NFC-e
│   ├── Impressoras
│   ├── Mini-impressoras (não fiscais)
│   ├── Impressora térmica (etiquetas)
│   ├── TEF
│   ├── Leitores de código de barras
│   ├── Coletores de dados
│   ├── Backup
│   ├── Tablets (Optfacil.com)
│   ├── Equipamentos COMPATÍVEIS (lista alternativa)
│   └── Identidade visual / dados da empresa
├── 3. Itens removidos na versão 2023
├── 4. Itens novos ou atualizados na versão 2023
├── 5. Itens que permaneceram iguais
└── 6. Conclusão
```

---

## 2. Lista de chunks

### dataweb-perifericos_hardware_estacao_01
**Metadados:**
```json
{
  "id": "dataweb-perifericos_hardware_estacao_01",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Requisitos de hardware",
  "subassunto": "Computador - Estação",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Configuração mínima recomendada para o computador de estação (versão vigente)",
  "palavras_chave": ["computador", "estação", "hardware", "requisitos mínimos", "processador", "RAM"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: documento de origem (docx comparativo) não numera páginas]",
  "revisar": true
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Requisitos de hardware > Computador - Estação.

Na versão mais recente (2023) do manual de periféricos compatíveis, o perfil de computador recomendado como "Estação" é:
1. Processador: Intel Core i5.
2. Memória RAM: 4GB.
3. Armazenamento: HD com 500GB.

Essa configuração é a recomendação mínima para uma empresa com até 5 computadores. Para maiores capacidades, é necessário consultar a Dataweb.

**Observação histórica:** na versão anterior (2019), o perfil de Estação era Intel Core i3, 4GB de RAM, SSD de 120GB — ou seja, a versão atual exige um processador mais forte (i5 em vez de i3), mas substitui o SSD por HD.

**Perguntas frequentes relacionadas:**
- Qual a configuração mínima de computador recomendada para rodar o Dataweb?
- Quantos GB de RAM e qual processador o Dataweb recomenda para a estação de trabalho?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_hardware_servidor_02
**Metadados:**
```json
{
  "id": "dataweb-perifericos_hardware_servidor_02",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Requisitos de hardware",
  "subassunto": "Computador - Servidor (descontinuado)",
  "tipo_conteudo": "conceito",
  "titulo": "Perfil de computador Servidor deixou de ser especificado separadamente",
  "palavras_chave": ["servidor", "hardware", "descontinuado", "SSD", "NVMe"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Requisitos de hardware > Computador - Servidor.

Na versão 2019 do manual, havia um perfil de hardware próprio para "Servidor": Intel Core i5, 8GB de RAM, SSD ou NVMe de 240GB, mais HD de 1TB. Esse perfil era destinado a empresas com banco de dados local.

Na versão mais recente (2023), esse perfil de "Servidor" não é mais especificado separadamente — a seção de computadores passou a listar apenas a configuração de "Estação".

**Perguntas frequentes relacionadas:**
- O Dataweb ainda especifica uma configuração de servidor separada da estação?
- Qual era a configuração antiga recomendada para servidor?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_sistema_operacional_03
**Metadados:**
```json
{
  "id": "dataweb-perifericos_sistema_operacional_03",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Sistema Operacional",
  "subassunto": "Requisitos de sistema operacional",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Sistema operacional exigido para uso do Dataweb",
  "palavras_chave": ["sistema operacional", "Windows", "licença", "Windows 8.1", "Windows Server"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Sistema Operacional.

Na versão vigente (2023), o sistema operacional exigido é:
1. Windows 8.1 ou superior.
2. É exigida licença original Microsoft.

**Observação:** a versão vigente não menciona mais Windows Server como opção.

**Observação histórica:** na versão 2019, o sistema operacional recomendado era Windows 10, com a recomendação adicional de Windows Server 2016 ou superior para empresas com banco de dados local (servidor próprio) e mais de 5 computadores.

**Perguntas frequentes relacionadas:**
- Qual versão do Windows o Dataweb exige?
- É preciso ter licença original do Windows para usar o Dataweb?
- O Dataweb ainda recomenda Windows Server para bases locais grandes?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_ecf_impressora_fiscal_04
**Metadados:**
```json
{
  "id": "dataweb-perifericos_ecf_impressora_fiscal_04",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Emissor de Documentos Fiscais (ECF)",
  "subassunto": "Marcas e modelos de impressora fiscal compatíveis",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Marcas de impressora fiscal (ECF) compatíveis com o Dataweb",
  "palavras_chave": ["ECF", "impressora fiscal", "Bematech", "Daruma", "conexão serial", "USB"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Emissor de Documentos Fiscais (ECF).

Na versão vigente (2023), a única marca de impressora fiscal (ECF) homologada é:
1. Bematech — todos os modelos térmicos.

**Aviso importante (válido em ambas as versões):** se o sistema operacional for 64 bits, a impressora Bematech **precisa** usar conexão serial — conexão USB **não funcionará**.

**Observação histórica:** na versão 2019, além da Bematech, a marca Daruma (todos os modelos térmicos) também era homologada como ECF. Na versão 2023, a Daruma não é mais citada.

**Perguntas frequentes relacionadas:**
- Quais marcas de impressora fiscal são compatíveis com o Dataweb?
- Posso usar impressora fiscal Daruma com o Dataweb?
- Por que minha impressora fiscal Bematech não funciona via USB?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_nfce_05
**Metadados:**
```json
{
  "id": "dataweb-perifericos_nfce_05",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "NFC-e",
  "subassunto": "Requisitos para emissão de NFC-e",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Requisitos para emitir Nota Fiscal de Consumidor eletrônica (NFC-e)",
  "palavras_chave": ["NFC-e", "certificado digital", "A1", "mini impressora", "Santa Catarina"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > NFC-e (Nota Fiscal de Consumidor eletrônica).

Para emitir NFC-e pelo Dataweb (válido em ambas as versões do manual):
1. É necessário adquirir certificado digital do tipo A1.
2. Recomenda-se o uso de mini impressora não fiscal para a impressão do documento.

**Observação histórica:** a versão 2019 trazia a ressalva de que a NFC-e não estava disponível no estado de Santa Catarina. Essa ressalva não consta mais na versão 2023.

**Perguntas frequentes relacionadas:**
- Que tipo de certificado digital é necessário para emitir NFC-e no Dataweb?
- Qual impressora usar para imprimir a NFC-e?
- A NFC-e está disponível para o estado de Santa Catarina?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_impressoras_gerais_06
**Metadados:**
```json
{
  "id": "dataweb-perifericos_impressoras_gerais_06",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Impressoras",
  "subassunto": "Recomendações gerais de impressora",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Recomendações gerais para escolha de impressora (rede x Wi-Fi)",
  "palavras_chave": ["impressora", "rede", "Wi-Fi", "Windows Server", "certificação Windows"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Impressoras.

Essas recomendações são idênticas nas versões 2019 e 2023 do manual:
1. Qualquer impressora certificada para Windows pode ser usada.
2. Modelos com conectividade de rede em geral apresentam melhor performance e menos problemas de compatibilidade ou drivers.
3. Modelos com rede Wi-Fi são recomendados apenas para uso temporário ou doméstico.
4. Se a impressora possuir ambas as conexões (rede física e Wi-Fi), deve-se dar preferência à conexão física.
5. Para utilizar a impressora via acesso remoto, é necessário verificar a compatibilidade dela com Windows SERVER (consulta disponível em www.windowservercatalog.com).

**Perguntas frequentes relacionadas:**
- Que tipo de impressora posso usar com o Dataweb?
- Devo usar impressora Wi-Fi ou de rede cabeada?
- Como verifico se uma impressora é compatível com Windows Server para acesso remoto?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_mini_impressoras_07
**Metadados:**
```json
{
  "id": "dataweb-perifericos_mini_impressoras_07",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Mini-impressoras",
  "subassunto": "Modelos de mini impressora não fiscal",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Modelo de mini impressora não fiscal recomendado",
  "palavras_chave": ["mini impressora", "não fiscal", "Bematech MP-4200 TH", "Bematech MP-4000 TH", "Bematech MP-2100 TH"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Mini-impressoras (não fiscais).

Na versão vigente (2023), o modelo recomendado é:
1. Bematech MP-4200 TH.

**Observação histórica:** na versão 2019, havia dois modelos recomendados: Bematech MP-4000 TH e Bematech MP-2100 TH. Na versão 2023, apenas o modelo mais novo (MP-4200 TH) é listado.

**Perguntas frequentes relacionadas:**
- Qual mini impressora não fiscal o Dataweb recomenda atualmente?
- Os modelos MP-4000 TH e MP-2100 TH ainda são recomendados?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_impressora_termica_etiquetas_08
**Metadados:**
```json
{
  "id": "dataweb-perifericos_impressora_termica_etiquetas_08",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Impressora Térmica de Etiquetas",
  "subassunto": "Modelo recomendado",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Modelo de impressora térmica de etiquetas recomendado",
  "palavras_chave": ["impressora térmica", "etiquetas", "Argox", "Argox OS 214 PLUS"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Impressora Térmica (Etiquetas).

Na versão vigente (2023), o modelo recomendado é:
1. Impressora Térmica Argox OS 214 PLUS.

**Observação histórica:** na versão 2019, a recomendação era genérica — "Impressora Térmica Argox", sem especificar o modelo exato.

**Perguntas frequentes relacionadas:**
- Qual impressora de etiquetas o Dataweb recomenda?
- Existe um modelo específico de impressora Argox indicado?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_tef_sitef_09
**Metadados:**
```json
{
  "id": "dataweb-perifericos_tef_sitef_09",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "TEF (Transferência Eletrônica de Fundos)",
  "subassunto": "Solução de TEF homologada",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Solução de TEF homologada para uso com o Dataweb",
  "palavras_chave": ["TEF", "SITEF", "homologado", "transferência eletrônica de fundos"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Transferência Eletrônica de Fundos (TEF).

Essa informação é idêntica nas versões 2019 e 2023 do manual:
1. A única solução de TEF homologada é o SITEF.
2. O correto funcionamento é garantido unicamente com o SITEF.
3. Para informações ou dúvidas sobre outras soluções de TEF, é necessário entrar em contato com o consultor Dataweb.

**Perguntas frequentes relacionadas:**
- Qual solução de TEF o Dataweb suporta?
- Posso usar uma solução de TEF diferente do SITEF?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_leitores_codigo_barras_10
**Metadados:**
```json
{
  "id": "dataweb-perifericos_leitores_codigo_barras_10",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Leitores de código de barras",
  "subassunto": "Formatos suportados e configuração",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Formatos de código de barras suportados e configuração exigida do leitor",
  "palavras_chave": ["leitor de código de barras", "UPC A", "UPC E", "EAN-13", "EAN-8", "Code 128", "Code 39", "ENTER"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Leitores de código de barras.

Essa informação é idêntica nas versões 2019 e 2023 do manual:
1. Qualquer leitor que aceite um ou mais dos seguintes formatos é compatível: UPC A, UPC E, EAN-13, EAN-8, International 2-5, Code 128, Code 39, Postnet, FIM, Codabar e MSI.
2. **Importante:** o leitor deve permitir configuração para enviar um ENTER após a leitura.

**Perguntas frequentes relacionadas:**
- Quais formatos de código de barras o Dataweb suporta?
- Por que meu leitor de código de barras precisa enviar ENTER após a leitura?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_tablets_optfacil_11
**Metadados:**
```json
{
  "id": "dataweb-perifericos_tablets_optfacil_11",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Tablets",
  "subassunto": "Requisitos de tablet para Optfacil.com",
  "tipo_conteudo": "pré-requisito",
  "titulo": "Requisitos de sistema operacional de tablet para uso do Optfacil.com",
  "palavras_chave": ["tablet", "Optfacil.com", "Android", "iOS"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Modelo de Tablet para Optfacil.com (OS na Web).

Essa informação é idêntica nas versões 2019 e 2023 do manual:
1. Sistema operacional Android: recomenda-se tablets com no mínimo a versão 6 do Android.
2. Sistema operacional iOS: recomenda-se tablets com no mínimo a versão 9 do iOS.

**Perguntas frequentes relacionadas:**
- Qual versão mínima de Android ou iOS o tablet precisa ter para usar o Optfacil.com?
- Posso usar qualquer tablet com o Optfacil.com?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_itens_descontinuados_2023_12
**Metadados:**
```json
{
  "id": "dataweb-perifericos_itens_descontinuados_2023_12",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Itens descontinuados",
  "subassunto": "Seções removidas na versão 2023",
  "tipo_conteudo": "aviso",
  "titulo": "Seções e itens que existiam em 2019 e não constam mais na versão 2023 do manual",
  "palavras_chave": ["descontinuado", "removido", "coletores de dados", "backup", "equipamentos compatíveis", "ATOM", "thin client"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Itens descontinuados (comparativo 2019 x 2023).

Os itens abaixo constavam no manual de 2019 e não aparecem mais na versão vigente (2023):

1. **Perfil de computador "Servidor"** separado — restou apenas o perfil de Estação.
2. **Daruma** como opção de emissor fiscal (ECF) — hoje apenas Bematech é homologada.
3. **Ressalva de indisponibilidade de NFC-e em Santa Catarina.**
4. **Seção "Equipamentos COMPATÍVEIS"** — no manual de 2019 essa seção listava uma configuração alternativa mais tolerante: qualquer PC fabricado há menos de 4 anos, com 2GB de RAM e 250GB de HDD, rodando Windows 8.1, com exceção feita à linha de processadores ATOM (recomendados apenas para estações thin client, sem sistema instalado localmente).
5. **Seção "Coletores de Dados"** — informava que os coletores não interagem diretamente com o sistema, mas precisam gerar um arquivo em formato reconhecido pelo sistema (era necessário contatar a Dataweb para verificar compatibilidade dos arquivos gerados).
6. **Seção "Backup"** — explicava que a configuração de backup automático é feita pela Dataweb logo após a instalação do sistema, mas que o armazenamento e cuidado com o arquivo gerado é responsabilidade exclusiva da empresa contratante.
7. **Menção a Windows Server** como opção de sistema operacional para bases locais com mais de 5 computadores.

**Perguntas frequentes relacionadas:**
- Ainda existe uma lista de "Equipamentos Compatíveis" mais flexível além da lista recomendada?
- O Dataweb ainda dá orientações sobre coletores de dados?
- Existe orientação sobre backup no manual atual de periféricos?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_itens_novos_2023_13
**Metadados:**
```json
{
  "id": "dataweb-perifericos_itens_novos_2023_13",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Itens novos ou atualizados",
  "subassunto": "Novidades da versão 2023",
  "tipo_conteudo": "aviso",
  "titulo": "O que mudou ou foi adicionado na versão 2023 do manual",
  "palavras_chave": ["licença original", "Microsoft", "MP-4200 TH", "Argox OS 214 PLUS", "identidade visual"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Itens novos ou atualizados (comparativo 2019 x 2023).

1. Exigência explícita de **licença original Microsoft** para o Windows.
2. Modelo específico de mini-impressora atualizado para **Bematech MP-4200 TH** (substituindo os dois modelos anteriores, MP-4000 TH e MP-2100 TH).
3. Modelo específico de impressora térmica de etiquetas atualizado para **Argox OS 214 PLUS**.
4. Nova identidade visual da empresa e dados de contato (endereço: Av. Carlos Gomes, 817, 90.480-003, Porto Alegre/RS; site: dataweb.com.br) passam a constar no rodapé do manual.

**Perguntas frequentes relacionadas:**
- Preciso ter licença original do Windows para o Dataweb funcionar corretamente?
- Qual o modelo atual de mini impressora recomendado?
- Onde encontro os dados de contato da Dataweb no manual?

**Imagens associadas:** nenhuma.

---

### dataweb-perifericos_faq_geral_14
**Metadados:**
```json
{
  "id": "dataweb-perifericos_faq_geral_14",
  "manual_origem": "Comparativo_Perifericos_Dataweb",
  "modulo": "Infraestrutura e Periféricos",
  "assunto": "Visão geral",
  "subassunto": "Comparativo entre versões do manual",
  "tipo_conteudo": "conceito",
  "titulo": "Visão geral das diferenças entre os manuais de periféricos compatíveis de 2019 e 2023",
  "palavras_chave": ["comparativo", "periféricos", "versão 2019", "versão 2023", "equipamentos recomendados"],
  "perfil_usuario": "todos",
  "possui_imagem_referenciada": false,
  "pagina_origem": "[REVISAR: página não informada no documento de origem]",
  "revisar": false
}
```

**Conteúdo:**
Infraestrutura e Periféricos > Visão geral.

O manual de periféricos compatíveis com o Dataweb existe em duas versões principais: uma de 2019 e uma mais recente, de 2023. A versão de 2023 é mais enxuta e atualizada em relação à de 2019: reduz a seção de "Computadores" a um único perfil de Estação, remove por completo a seção "Equipamentos COMPATÍVEIS" (que trazia uma lista alternativa mais tolerante de hardware) e atualiza os modelos específicos de impressoras recomendados. A versão de 2023 também traz nova identidade visual e dados de contato da empresa.

De forma geral, a versão 2023 é mais restritiva quanto às marcas homologadas (por exemplo, ECF apenas Bematech) e mais específica quanto aos modelos exatos recomendados de mini-impressora e impressora de etiquetas, mas removeu orientações sobre backup e coletores de dados que existiam em 2019.

**Perguntas frequentes relacionadas:**
- Qual a diferença entre o manual de periféricos de 2019 e o de 2023?
- Qual versão do manual de periféricos devo seguir hoje?

**Imagens associadas:** nenhuma.

---

## 3. Glossário de termos específicos do Dataweb

| Termo/Sigla | Definição (conforme usado no documento) |
| --- | --- |
| **ECF** | Emissor de Documentos Fiscais — impressora fiscal térmica usada para emissão de cupons fiscais, homologada pelas marcas Bematech (2019 e 2023) e Daruma (apenas 2019). |
| **NFC-e** | Nota Fiscal de Consumidor eletrônica — documento fiscal que exige certificado digital tipo A1 para emissão. |
| **TEF** | Transferência Eletrônica de Fundos — integração de meios de pagamento eletrônico ao sistema; homologada apenas com o SITEF. |
| **SITEF** | Solução de TEF homologada e garantida pela Dataweb para funcionamento correto do sistema de pagamentos. |
| **Certificado digital A1** | Tipo de certificado digital necessário para emissão de NFC-e. |
| **Optfacil.com** | Sistema referido como "OS na Web", acessado via tablet (Android 6+ ou iOS 9+). |
| **Thin client** | Perfil de estação de acesso remoto sem sistema instalado localmente; único uso recomendado para processadores da linha ATOM (citado apenas na versão 2019, seção "Equipamentos COMPATÍVEIS", hoje removida). |
| **Windows SERVER Catalog** | Site (www.windowservercatalog.com) usado para verificar a compatibilidade de uma impressora com Windows Server, quando o uso é via acesso remoto. |

---

## 4. Lista de pontos sinalizados para revisão [REVISAR]

- **[REVISAR: numeração de página]** — O documento de origem (Comparativo_Perifericos_Dataweb.docx) não contém numeração de páginas nem indicação de página de origem dos trechos; o campo `pagina_origem` de todos os chunks foi marcado como pendente de revisão. Caso os manuais originais em PDF ("Periféricos Compatíveis 2019" e "Periféricos Compatíveis 2023") sejam disponibilizados, recomenda-se reprocessar e preencher esse campo com o número de página real de cada seção.
- **[REVISAR: manual de origem]** — O conteúdo processado aqui é derivado de um **documento comparativo** já elaborado anteriormente (não dos manuais originais em PDF). Recomenda-se, quando possível, gerar esta base de conhecimento diretamente a partir dos manuais originais "Periféricos Compatíveis 2019" e "Periféricos Compatíveis 2023" para garantir fidelidade total e permitir a citação de página real.
- **[REVISAR: ausência de instruções operacionais]** — Nenhum dos dois manuais de origem contém passo a passo de telas/botões do sistema Dataweb (não há chunks do tipo `procedimento`); todo o conteúdo é referência de hardware/periféricos compatíveis.
