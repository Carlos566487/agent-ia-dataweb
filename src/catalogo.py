from __future__ import annotations

import re
import unicodedata
from .dominio import Resultado

# Mapeamento completo dos 36 manuais em documentos/ organizados em 7 módulos
CATALOGO_TEMAS = [
    {
        "modulo": "Módulo Caixa e Frente de Loja",
        "emoji": "💳",
        "temas": [
            {
                "titulo": "Manual Operacional do Caixa",
                "descricao": "Abertura, operações de venda, recebimentos, sangria e encerramento de caixa.",
                "arquivo": "MANUAL OPERACIONAL DO SISTEMA DATAWEB – MÓDULO CAIXA.pdf",
            },
            {
                "titulo": "Operações do Módulo Caixa",
                "descricao": "Aporte, retirada, resumo de caixa, consultas financeiras e impressão de 2ª via.",
                "arquivo": "RAG_dataweb_modulo_caixa.md",
            },
            {
                "titulo": "Garantia, Devolução e Crédito (V3)",
                "descricao": "Diferença conceitual entre Garantia e Devolução e utilização de crédito do cliente.",
                "arquivo": "RAG_dataweb_garantia_devolucao_credito.md",
            },
            {
                "titulo": "Devoluções de Mercadoria",
                "descricao": "Passo a passo para cancelamento e devolução de itens com ou sem crédito.",
                "arquivo": "RAG_dataweb_garantia_devolucao_credito2.md",
            },
            {
                "titulo": "Baixa de Carnê",
                "descricao": "Quitação e baixa manual ou automática de parcelas de carnês.",
                "arquivo": "RAG_dataweb_baixar_carne.md",
            },
            {
                "titulo": "Tipos de Carnê",
                "descricao": "Cadastro e parametrização das modalidades de carnê da loja.",
                "arquivo": "RAG_dataweb_tipos_carne.md",
            },
            {
                "titulo": "Configuração de Juros do Carnê",
                "descricao": "Definição de taxas e cálculo de juros para parcelas em atraso.",
                "arquivo": "RAG_dataweb_carne_configuracao_juros.md",
            },
            {
                "titulo": "Cadastro de Campanhas no Caixa",
                "descricao": "Ativação e aplicação de regras de campanhas promocionais de frente de loja.",
                "arquivo": "RAG_dataweb_cadastro_campanhas.md",
            },
            {
                "titulo": "Campanhas Promocionais Detalhadas",
                "descricao": "Configuração de descontos e critérios avançados de campanhas.",
                "arquivo": "RAG_dataweb_cadastro_campanhas2.md",
            },
            {
                "titulo": "Promoção Lente em Dobro",
                "descricao": "Regras comerciais e lançamento de pedidos participantes da promoção Lente em Dobro.",
                "arquivo": "RAG_dataweb_lente_em_dobro.md",
            },
        ],
    },
    {
        "modulo": "Pedidos e Faturamento",
        "emoji": "📦",
        "temas": [
            {
                "titulo": "Gestão de Pedidos e Faturamento",
                "descricao": "Emissão de pedidos, transações de saída, faturamento e controle fiscal de notas.",
                "arquivo": "RAG_dataweb_pedidos.md",
            },
            {
                "titulo": "Split de Venda (E-commerce)",
                "descricao": "Emissão de NFSe a partir de O.S de retenção/split gerada por vendas no e-commerce.",
                "arquivo": "RAG_dataweb_split_venda.md",
            },
            {
                "titulo": "Ativação de Produto para Devolução ao Fornecedor",
                "descricao": "Reativação de produtos inativos para emissão de nota de devolução.",
                "arquivo": "RAG_dataweb_ativar_produto_inativo_devolucao_fornecedor.md",
            },
            {
                "titulo": "Transferência entre Empresas",
                "descricao": "Procedimento de transferência de mercadorias entre filiais da rede.",
                "arquivo": "RAG_dataweb_transferencia_entre_empresas.md",
            },
            {
                "titulo": "Análise de Vendas e Ordem de Compra",
                "descricao": "Cruzamento de vendas com ordens de compra para reposição de produtos.",
                "arquivo": "RAG_dataweb_analise_vendas_ordem_compra.md",
            },
        ],
    },
    {
        "modulo": "Estoque e Laboratório",
        "emoji": "🏷️",
        "temas": [
            {
                "titulo": "Ajuste de Estoque por Marca e Armação",
                "descricao": "Contagem de inventário e acerto de saldos de armações por marca.",
                "arquivo": "RAG_dataweb_ajustar_estoque_marca_armacao.md",
            },
            {
                "titulo": "Lentes que Não Movimentam Estoque",
                "descricao": "Manutenção em lote de dados cadastrais para desativar controle de estoque de lentes.",
                "arquivo": "RAG_dataweb_definir_lentes_nao_movimentar_estoque.md",
            },
            {
                "titulo": "Análise de Custo, Preço e Markup",
                "descricao": "Ferramenta de controle de margem, markup e análise de custo x venda.",
                "arquivo": "RAG_dataweb_analise_custo_venda.md",
            },
            {
                "titulo": "Monitor de Produção",
                "descricao": "Acompanhamento do status de ordens de serviço no laboratório e na montagem.",
                "arquivo": "RAG_dataweb_monitor_de_producao.md",
            },
        ],
    },
    {
        "modulo": "Módulo Financeiro",
        "emoji": "💰",
        "temas": [
            {
                "titulo": "Cadastro de Condições de Pagamento",
                "descricao": "Criação de regras de parcelamento, prazos e descontos financeiros.",
                "arquivo": "RAG_dataweb_cadastrar_condicoes_pagamento.md",
            },
            {
                "titulo": "Programação de Contas a Pagar",
                "descricao": "Agendamento, acompanhamento e liquidação de compromissos financeiros.",
                "arquivo": "RAG_dataweb_programacao_contas.md",
            },
            {
                "titulo": "Ajuste de Saldo de Contas Bancárias",
                "descricao": "Conciliação bancária e ajuste de saldos de contas correntes no sistema.",
                "arquivo": "RAG_dataweb_ajuste_saldo_contas_bancarias.md",
            },
            {
                "titulo": "DRE e Fluxo de Caixa",
                "descricao": "Relatórios de Demonstração do Resultado do Exercício e projeção de caixa.",
                "arquivo": "RAG_dataweb_dre_fluxo_caixa.md",
            },
        ],
    },
    {
        "modulo": "Relatórios e Comissões",
        "emoji": "📊",
        "temas": [
            {
                "titulo": "Relatório de Comissão por Vendedor",
                "descricao": "Emissão e conferência de comissões por vendedor conforme a forma de pagamento.",
                "arquivo": "RAG_dataweb_relatorio_comissao_vendedor.md",
            },
            {
                "titulo": "Regras de Comissão de Vendas",
                "descricao": "Parametrização de faixas percentuais e critérios de comissionamento.",
                "arquivo": "RAG_dataweb_regras_relatorio_comissao.md",
            },
            {
                "titulo": "Relatório de Vendas por Marca",
                "descricao": "Análise quantitativa e financeira de produtos vendidos por fabricante/marca.",
                "arquivo": "RAG_dataweb_relatorio_vendas_marca.md",
            },
            {
                "titulo": "Relatório de Clientes Aniversariantes",
                "descricao": "Listagem de aniversariantes do período para campanhas de relacionamento.",
                "arquivo": "RAG_dataweb_relatorio_aniversariantes.md",
            },
            {
                "titulo": "Verificar Clientes Cadastrados por Período",
                "descricao": "Pesquisa de clientes registrados no sistema por intervalo de datas.",
                "arquivo": "RAG_dataweb_verificar_clientes_cadastrados_data.md",
            },
        ],
    },
    {
        "modulo": "OptFácil (Mobile, CRM & Analytics)",
        "emoji": "📱",
        "temas": [
            {
                "titulo": "OptFácil Loja (Mobile)",
                "descricao": "Acesso ao sistema Optfácil via dispositivos móveis e seleção de aplicações.",
                "arquivo": "RAG_dataweb_optfacil_loja.md",
            },
            {
                "titulo": "OptFácil CRM",
                "descricao": "Gestão de relacionamento com o cliente, contatos, agendamentos e pós-venda.",
                "arquivo": "RAG_dataweb_optfacil_crm.md",
            },
            {
                "titulo": "OptFácil Analytics",
                "descricao": "Inteligência de vendas, acompanhamento de metas e indicadores da ótica.",
                "arquivo": "RAG_dataweb_optfacil_analytics.md",
            },
            {
                "titulo": "OptFácil Analytics Mobile",
                "descricao": "Métricas financeiras, análise de compras e perfil de consumo no celular.",
                "arquivo": "RAG_dataweb_optfacil_analytics2.md",
            },
            {
                "titulo": "OptFácil Total (Visão Geral)",
                "descricao": "Manual unificado de todos os recursos da plataforma Optfácil.",
                "arquivo": "RAG_dataweb_optfacil_total.md",
            },
        ],
    },
    {
        "modulo": "Infraestrutura, TI & Suporte Técnico",
        "emoji": "🛠️",
        "temas": [
            {
                "titulo": "Abertura de Chamados no Suporte Help Desk",
                "descricao": "Procedimento oficial para envio de chamados, canais de contato e regras de SLA.",
                "arquivo": "RAG_dataweb_abertura_chamados_suporte.md",
            },
            {
                "titulo": "Periféricos e Hardware Compatíveis",
                "descricao": "Especificações e requisitos de servidores, estações, impressoras, leitores e TEF.",
                "arquivo": "RAG_dataweb_perifericos_dataweb.md",
            },
            {
                "titulo": "Instalação de Impressora Térmica",
                "descricao": "Procedimento passo a passo para conexão física, drivers e configuração de impressora térmica (Bematech MP-4000 TH).",
                "arquivo": "RAG_dataweb_impressora_termica.md",
            },
            {
                "titulo": "Importação de Certificado Digital",
                "descricao": "Instalação, homologação e renovação de Certificado Digital A1 e A3.",
                "arquivo": "RAG_dataweb_importar_certificado_digital.md",
            },
            {
                "titulo": "Exportação de XML de Notas Fiscais",
                "descricao": "Geração e download de arquivos XML de notas fiscais para contabilidade.",
                "arquivo": "RAG_dataweb_exportar_xml.md",
            },
            {
                "titulo": "Glossário Geral Consolidado",
                "descricao": "Definições dos termos técnicos, comandos e conceitos do sistema DataWeb.",
                "arquivo": "RAG_dataweb_glossario_geral_e_revisoes.md",
            },
        ],
    },
]

PADRAO_PERGUNTA_CATALOGO = re.compile(
    r"(quais\s+(?:os\s+)?(?:temas|assuntos|modulos|topicos|manuais)|"
    r"(?:temas|assuntos|modulos|topicos|manuais)\s+disponiveis|"
    r"o que\s+(?:posso|consigo|tem)\s+(?:pesquisar|consultar|perguntar|na base)|"
    r"o que\s+voce\s+(?:sabe|cobre|responde)|"
    r"lista\s+de\s+(?:temas|assuntos|modulos|manuais)|"
    r"quantos\s+(?:temas|manuais|arquivos))"
)


def eh_pergunta_de_catalogo(pergunta: str) -> bool:
    """Detecta se a pergunta do usuário é uma consulta geral sobre os temas/módulos disponíveis."""
    texto_normalizado = "".join(
        c for c in unicodedata.normalize("NFD", pergunta) if unicodedata.category(c) != "Mn"
    ).lower()
    return bool(PADRAO_PERGUNTA_CATALOGO.search(texto_normalizado))


def obter_catalogo_formatado() -> str:
    """Gera a descrição consolidada e formatada de todos os 36 manuais disponíveis."""
    total_temas = sum(len(m["temas"]) for m in CATALOGO_TEMAS)
    linhas = [
        f"A base de conhecimento do **DataWeb** conta com **{total_temas} temas operacionais**, organizados pelos seguintes módulos:\n"
    ]
    for grupo in CATALOGO_TEMAS:
        modulo = grupo["modulo"]
        emoji = grupo["emoji"]
        linhas.append(f"**{emoji} {modulo}**\n")
        for t in grupo["temas"]:
            linhas.append(f"• **{t['titulo']}:** {t['descricao']}")
        linhas.append("")

    linhas.append("Para consultar qualquer procedimento, basta digitar sua dúvida diretamente no chat.")
    return "\n".join(linhas)


def obter_resultado_catalogo() -> Resultado:
    """Cria um Resultado de RAG estruturado contendo o catálogo completo para injeção de contexto."""
    return Resultado(
        texto=obter_catalogo_formatado(),
        fonte="Catálogo Oficial de Temas do Sistema DataWeb",
        pagina=1,
        score=1.0,
        extra={"assunto": "Catálogo Completo dos 36 Temas Disponíveis", "modulo": "Geral"},
    )
