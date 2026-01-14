import json

def gerar_prompt_relatorio(url, resumo_violacoes):
    json_resumo = json.dumps(resumo_violacoes, indent=2, ensure_ascii=False)

    prompt = f"""
    Você é um especialista em acessibilidade digital (WCAG 2.1 e eMAG).

    Analise os dados abaixo, gerados automaticamente por uma ferramenta de auditoria
    de acessibilidade, e produza um RELATÓRIO HUMANIZADO em português, voltado para
    gestores e times não técnicos.

    Site analisado:
    {url}

    Instruções para o relatório:
    - Linguagem clara e acessível
    - Explique o impacto das falhas para usuários reais
    - Priorize problemas críticos
    - Traga recomendações práticas
    - Use títulos e subtítulos

    ⚠️ Avaliação geral:
    - Atribua uma NOTA FINAL de 0 a 100 para o nível de acessibilidade do site
    - Explique claramente como a nota foi calculada
    - Considere:
    • Quantidade de falhas
    • Gravidade das falhas
    • Impacto para pessoas com deficiência
    • Aderência às WCAG 2.1 e ao eMAG

    Estrutura esperada:
    0. Titulo sendo : Relatorio de Acessibilidade Digital do Site (sem o http://{url})
    1. Resumo Executivo (incluindo a nota final)
    2. Nota de Acessibilidade (0 a 100) e justificativa
    3. Principais Problemas Encontrados:
    3.1. Avaliação considerou os seguintes fatores: 
    • Quantidade de falhas: numero problemas foram identificados. 
    • Gravidade das falhas: numero problema crítico, numero graves, numero moderado e numero menor.
    • Descrição das falhas: breve descrição de cada problema encontrado.
    • Aderência às WCAG 2.1 e ao eMAG: o site alcançou um nível de conformidade AA,
    4. Impactos para Pessoas com Deficiência
    5. Recomendações Prioritárias
    6. Conclusão

    Dados técnicos (JSON):
    {json_resumo}
    """

    return prompt
