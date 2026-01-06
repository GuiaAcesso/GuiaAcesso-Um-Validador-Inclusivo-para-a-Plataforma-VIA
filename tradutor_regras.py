# tradutor_regras.py
# Mapeamento COMPLETO de erros técnicos para ABNT NBR 17225 e Explicações Humanizadas

DICIONARIO_TRADUCAO = {

    # ==============================================================================
    # 1. DEFICIÊNCIA VISUAL (Cegueira / Baixa Visão)
    # ==============================================================================
    "image-alt": {
        "titulo_humanizado": "Imagem sem Descrição (Texto Alternativo)",
        "explicacao_gerente": "Uma imagem que transmite informação não possui descrição. Usuários cegos (que usam leitores de tela) não saberão o que ela representa.",
        "explicacao_dev": "Adicione o atributo alt='descrição' na tag <img>. Se for decorativa, use alt=''.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.2.1) - Texto alternativo para imagens",
        "nivel_selo": "A"
    },
    "input-image-alt": {
        "titulo_humanizado": "Botão de Imagem sem Nome",
        "explicacao_gerente": "Um botão gráfico não tem texto. O usuário ouve apenas 'botão' e não sabe se é para 'Salvar', 'Excluir' ou 'Buscar'.",
        "explicacao_dev": "Input type='image' precisa de atributo alt descrevendo a ação.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.2.2) - Imagens funcionais",
        "nivel_selo": "A"
    },
    "color-contrast": {
        "titulo_humanizado": "Contraste de Cores Insuficiente",
        "explicacao_gerente": "O texto é difícil de ler porque a cor da letra é muito parecida com a do fundo. Prejudica idosos e pessoas com baixa visão.",
        "explicacao_dev": "Aumente o contraste para 4.5:1 (texto normal) ou 3:1 (texto grande).",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.11.3) - Contraste mínimo",
        "nivel_selo": "AA"
    },
    "document-title": {
        "titulo_humanizado": "Página sem Título na Aba",
        "explicacao_gerente": "A aba do navegador fica sem nome. Usuários de leitores de tela não sabem em qual página estão quando trocam de aba.",
        "explicacao_dev": "A tag <title> no <head> não pode estar vazia.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.1) - Título da página",
        "nivel_selo": "A"
    },
    "html-has-lang": {
        "titulo_humanizado": "Idioma da Página não Definido",
        "explicacao_gerente": "O site não avisa que está em Português. Leitores de tela tentarão ler o texto com sotaque inglês, tornando-o ininteligível.",
        "explicacao_dev": "Adicione o atributo lang='pt-BR' na tag <html>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.2) - Idioma da página",
        "nivel_selo": "A"
    },

    # ==============================================================================
    # 2. DEFICIÊNCIA MOTORA (Navegação por Teclado / Controle Fino)
    # ==============================================================================
    "label": {
        "titulo_humanizado": "Campo de Formulário sem Rótulo",
        "explicacao_gerente": "Um campo de digitação não diz o que deve ser preenchido. Usuários que navegam por voz ou teclado ficam bloqueados.",
        "explicacao_dev": "Todo <input> precisa de um <label> associado (for/id).",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.9.1) - Rótulo de campo",
        "nivel_selo": "A"
    },
    "button-name": {
        "titulo_humanizado": "Botão Vazio (Sem Texto)",
        "explicacao_gerente": "Um botão existe visualmente (ícone), mas não tem nome no código. Quem usa comando de voz não consegue clicar nele.",
        "explicacao_dev": "Botões devem ter texto interno ou aria-label.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.8.3) - Propósito do botão",
        "nivel_selo": "A"
    },
    "link-name": {
        "titulo_humanizado": "Link Vazio ou Vago",
        "explicacao_gerente": "Links sem texto ou com texto vago ('clique aqui') dificultam a navegação fora de contexto.",
        "explicacao_dev": "Links devem ter texto discernível que descreva o destino.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.7.4) - Propósito do link",
        "nivel_selo": "A"
    },
    "region": {
        "titulo_humanizado": "Conteúdo fora de Região Marcada",
        "explicacao_gerente": "Partes do site estão 'soltas', fora das áreas de Cabeçalho, Menu ou Principal. Dificulta a navegação rápida por atalhos.",
        "explicacao_dev": "Envolva o conteúdo em tags semânticas (<header>, <main>, <footer>, <nav>).",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.4.3) - Conteúdo em regiões",
        "nivel_selo": "A"
    },

    # ==============================================================================
    # 3. DEFICIÊNCIA AUDITIVA E COGNITIVA
    # ==============================================================================
    "video-caption": {
        "titulo_humanizado": "Vídeo sem Legendas",
        "explicacao_gerente": "Vídeos no site não possuem legendas. Pessoas surdas não têm acesso ao conteúdo falado.",
        "explicacao_dev": "Elementos <video> precisam de uma trilha <track kind='captions'>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.14.2) - Legendas descritivas",
        "nivel_selo": "A"
    },
    "audio-caption": {
        "titulo_humanizado": "Áudio sem Transcrição",
        "explicacao_gerente": "Arquivos de som não têm uma versão em texto. Pessoas surdas não podem acessar a informação.",
        "explicacao_dev": "Forneça um link para a transcrição textual do áudio.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.14.1) - Alternativa em texto",
        "nivel_selo": "A"
    },
    "heading-order": {
        "titulo_humanizado": "Hierarquia de Títulos Confusa",
        "explicacao_gerente": "A estrutura da página está bagunçada (pula do Título 1 para o Título 4). Isso confunde quem usa a estrutura para entender o conteúdo.",
        "explicacao_dev": "Mantenha a ordem lógica: <h1>, depois <h2>, depois <h3>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.3.5) - Estrutura de cabeçalhos",
        "nivel_selo": "A"
    }
}

# Função de busca segura (não precisa mudar)
def buscar_traducao(id_erro):
    return DICIONARIO_TRADUCAO.get(id_erro, {
        "titulo_humanizado": f"Erro Técnico não Catalogado: {id_erro}",
        "explicacao_gerente": "Este é um erro específico detectado pelo motor Axe que ainda não foi traduzido para o nosso padrão humanizado.",
        "explicacao_dev": f"Verifique a documentação em: https://dequeuniversity.com/rules/axe/4.4/{id_erro}",
        "norma_oficial": "WCAG 2.2 (Critério a verificar)",
        "nivel_selo": "Desconhecido"
    })