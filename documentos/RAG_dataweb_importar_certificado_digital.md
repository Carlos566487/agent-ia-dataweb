# Base de Conhecimento RAG — Importar Certificado Digital no Sistema

## 1. Resumo Estrutural do Manual

```
Módulo: Administrador
└── Configurações > Nota Fiscal
    └── Certificado Digital
        ├── Conceito: O que é um Certificado Digital (tipos A1 e A3)
        └── Procedimento: Cadastrar, selecionar, inserir senha e carregar o certificado no BD
```

Manual "Procedimento / Manual" (V 01.01, agosto de 24), criado por Carlos Eduardo — Analista de Suporte e Implantação PDV, homologado por Lincoln Akira — Supervisor de TI. Sem sumário numerado explícito; estrutura reconstituída a partir dos títulos de seção do próprio conteúdo.

---

## 2. Chunks

### importar-certificado-digital_administrador_certificado-digital_01

**Metadados:**
```json
{
  "id": "importar-certificado-digital_administrador_certificado-digital_01",
  "manual_origem": "ADMINISTRADOR_-_IMPORTAR_CERTIFICADO_DIGITAL_NO_SISTEMA_v2.pdf",
  "modulo": "Administrador",
  "assunto": "Certificado Digital",
  "subassunto": "Conceito e tipos",
  "tipo_conteudo": "conceito",
  "titulo": "O que é um Certificado Digital e quais tipos são compatíveis com o Dataweb",
  "palavras_chave": ["certificado digital", "certificado A1", "certificado A3", "NFe", "NFCe", "CTe"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": false,
  "pagina_origem": "1",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Administrador | Assunto: Certificado Digital

Um certificado digital é um arquivo eletrônico que atua como uma assinatura digital para pessoas físicas e jurídicas, com validade jurídica. Ele garante a autenticidade de transações eletrônicas e a identidade do portador (pessoa ou empresa).

O certificado digital autentica a empresa em transações online, permitindo, entre outras operações:
- Emissão de **NFe** (Notas Fiscais Eletrônicas) e **NFCe** (Notas Fiscais de Consumidor Eletrônicas);
- Emissão de **CTe** (Conhecimento de Transporte Eletrônico).

**Certificado Digital Tipo A1**
O Certificado Digital Tipo A1 é armazenado diretamente nos dispositivos (notebooks, smartphones e outros), permitindo o uso em qualquer lugar e a qualquer momento — especialmente útil para a emissão de NFe de serviços, com disponibilidade contínua. Possui validade de um ano e não necessita de dispositivo externo para armazenamento. Pode ser utilizado imediatamente após a compra, em qualquer computador (dentro ou fora da empresa) e simultaneamente em diferentes ambientes — sendo ideal para empresas com setores fiscais e contábeis em locais físicos distintos ou em operações remotas.

**Certificado Digital Tipo A3**
**Não é compatível com o sistema DATAWEB.**

**Perguntas frequentes relacionadas:**
- O que é um certificado digital e para que ele serve no Dataweb?
- Qual a diferença entre certificado digital A1 e A3?
- O certificado A3 funciona no sistema Dataweb?

**Imagens associadas:**
Ilustração decorativa de abertura da seção "O que é um Certificado Digital?", com o ícone de um arquivo de certificado (nome de exemplo "certificado.pfx"). Não representa uma tela do sistema.

---

### importar-certificado-digital_administrador_certificado-digital_02

**Metadados:**
```json
{
  "id": "importar-certificado-digital_administrador_certificado-digital_02",
  "manual_origem": "ADMINISTRADOR_-_IMPORTAR_CERTIFICADO_DIGITAL_NO_SISTEMA_v2.pdf",
  "modulo": "Administrador",
  "assunto": "Certificado Digital",
  "subassunto": "Cadastro e importação",
  "tipo_conteudo": "procedimento",
  "titulo": "Como importar/cadastrar um certificado digital no sistema Dataweb",
  "palavras_chave": ["certificado digital", "importar certificado", "configurações", "nota fiscal", "carregar no BD"],
  "perfil_usuario": "administrador",
  "possui_imagem_referenciada": true,
  "pagina_origem": "2-3",
  "revisar": false
}
```

**Conteúdo:**

Módulo: Administrador | Assunto: Certificado Digital > Cadastro e importação

Como importar/cadastrar um certificado digital no sistema Dataweb:

1º. Acesse **Módulo Administrador** > **Configurações** > **Nota fiscal...**.
2º. Na parte inferior, no campo **Certificado digital**, clique nos **3 pontos ("...")** para selecionar o arquivo digital.
3º. Insira a **senha** do certificado no campo **Senha**.
4º. Clique no botão **Carregar no BD**. Após isso, para salvar, clique no botão **OK** (caso o botão não apareça, aperte **Alt + O** para salvar).

**Observações:**
- Ao clicar nos 3 pontos, é preciso buscar no computador onde está o certificado — normalmente ele fica na pasta **Downloads**.
- Após o carregamento, o certificado é considerado atualizado. Para funcionamento em todas as máquinas, é preciso **sair e voltar ao sistema**.
- O certificado fica vinculado à empresa, para uso de todos os usuários, se necessário.

**Perguntas frequentes relacionadas:**
- Como faço para importar um certificado digital no Dataweb?
- Onde configuro o certificado digital no módulo Administrador?
- Depois de carregar o certificado, preciso fazer mais alguma coisa para ele funcionar em todos os computadores?

**Imagens associadas:**
1. Tela do módulo Administrador com o menu **Configurações** aberto, exibindo as opções Empresa, Entradas de mercadorias, Pedido, Caixa, Financeiro, Agenda, Email, Produtos, Cadastros, Pesquisas, **Nota fiscal...** (destacada/selecionada), NCM, Configurações de metas da empresa, Assistentes, Contatos, Configurações gerais, Configurações do Frente de Caixa, Configurações de relatórios e Configurações de fuso horário.
2. Painel **Certificado digital** com o campo **Certificado digital** vazio e o botão de reticências "..." destacado (retângulo vermelho) ao lado do botão **Carregar no BD**; campo **Senha** vazio; opção **Certificados digitais por número de série** com botão **Configurar**; botões **Ok** e **Cancelar**.
3. Mesmo painel **Certificado digital**, agora com o campo preenchido com o caminho "C:\Cert\AMBIENTE.pfx" e o campo **Senha** preenchido (mascarado com pontos), ambos destacados por um retângulo vermelho.
4. Mesmo painel, com o campo **Certificado digital** exibindo "(arquivo PFX armazenado no DB)", o botão **Carregar no BD** destacado (retângulo azul) e o botão **Ok** destacado (retângulo vermelho).

---

## 3. Glossário

| Termo | Definição (conforme uso no documento) |
|---|---|
| Certificado Digital | Arquivo eletrônico com validade jurídica que funciona como assinatura digital de uma pessoa física ou jurídica, usado para autenticar transações eletrônicas. |
| Certificado Digital A1 | Tipo de certificado armazenado diretamente em dispositivos (notebook, smartphone etc.), com validade de 1 ano; compatível com o Dataweb. |
| Certificado Digital A3 | Tipo de certificado que depende de dispositivo externo (não compatível com o Dataweb, segundo o manual). |
| NFe | Nota Fiscal Eletrônica. |
| NFCe | Nota Fiscal de Consumidor Eletrônica. |
| CTe | Conhecimento de Transporte Eletrônico. |
| PFX | Extensão de arquivo do certificado digital (exemplo citado no manual: "AMBIENTE.pfx"). |

---

## 4. Pontos Sinalizados para Revisão

Nenhum ponto de revisão identificado neste manual — conteúdo completo e sem ambiguidades.
