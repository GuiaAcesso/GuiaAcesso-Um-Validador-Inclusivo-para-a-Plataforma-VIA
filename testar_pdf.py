import json
from gerador_relatorio import criar_pdf_humanizado

print("Lendo os dados da pasta reports...")

# 1. Abre o arquivo que o Robô já gerou antes
try:
    with open("reports/resultado_axe_completo.json", "r", encoding="utf-8") as f:
        dados_brutos = json.load(f)
        
    # 2. Pega a lista de erros
    lista_de_erros = dados_brutos["violations"]

    # 3. Chama a sua máquina de PDF
    print(f"Encontrei {len(lista_de_erros)} erros. Gerando PDF...")
    criar_pdf_humanizado("Teste Local (JSON Existente)", lista_de_erros)

except FileNotFoundError:
    print("❌ Erro: Não encontrei o arquivo 'reports/resultado_axe_completo.json'. Rode o main.py primeiro!")