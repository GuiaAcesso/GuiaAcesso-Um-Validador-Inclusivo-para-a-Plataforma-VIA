from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from axe_selenium_python import Axe
import json
import time
import os

# 🔹 SDK NOVO DO GEMINI
from google import genai

# 🔐 CONFIGURE SUA API KEY AQUI
client = genai.Client(api_key="AIzaSyAq7F4pLh9vO5uDNaYfAxkrVYpebBIX5l0")

# --------------------------------------------------
# Extrai nome do site
# --------------------------------------------------
def extrair_nome_site(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    if url.startswith("www."):
        url = url[4:]
    if "/" in url:
        url = url.split("/")[0]
    return url.split(".")[0]


# --------------------------------------------------
# Identifica nível WCAG
# --------------------------------------------------
def identificar_nivel_wcag(tags):
    niveis = []
    for tag in tags:
        if tag.endswith("aaa"):
            niveis.append("AAA")
        elif tag.endswith("aa"):
            niveis.append("AA")
        elif tag.endswith("a"):
            niveis.append("A")
    return list(set(niveis))


# --------------------------------------------------
# Calcula conformidade AA
# --------------------------------------------------
def calcular_conformidade_aa(violacoes):
    TOTAL_CRITERIOS_AA_AUTOMATIZAVEIS = 50
    violacoes_aa = 0

    for v in violacoes:
        if any(tag.endswith("a") or tag.endswith("aa") for tag in v.get("tags", [])):
            violacoes_aa += 1

    aprovados = TOTAL_CRITERIOS_AA_AUTOMATIZAVEIS - violacoes_aa
    porcentagem = (aprovados / TOTAL_CRITERIOS_AA_AUTOMATIZAVEIS) * 100
    return round(max(porcentagem, 0), 2)


# --------------------------------------------------
# Relatório resumido técnico
# --------------------------------------------------
def gerar_relatorio_resumido(resultados):
    resumo = []
    for violacao in resultados.get("violations", []):
        resumo.append({
            "regra": violacao.get("id"),
            "impacto": violacao.get("impact"),
            "nivel_wcag": identificar_nivel_wcag(violacao.get("tags", [])),
            "descricao": violacao.get("description"),
            "elementos_afetados": len(violacao.get("nodes", []))
        })
    return resumo


# --------------------------------------------------
# GERA RELATÓRIOS HUMANIZADOS (TXT) COM GEMINI
# --------------------------------------------------
def gerar_relatorios_humanizados(resultados, nome_site):
    prompt = f"""
Você é um especialista em acessibilidade digital seguindo as diretrizes WCAG.

Explique os problemas abaixo para pessoas LEIGAS.

Crie DOIS TEXTOS:
1) RELATÓRIO COMPLETO: explicação detalhada de cada erro, impacto para pessoas com deficiência e resumo final.
2) RELATÓRIO RESUMIDO: visão geral simples, curta e direta.

Inclua a porcentagem de conformidade WCAG AA: {resultados['conformidade_wcag']['porcentagem']}%

Evite termos técnicos sem explicação.
Não use emojis.

Problemas encontrados:
{json.dumps(resultados['violations'], ensure_ascii=False, indent=2)}

Responda exatamente neste formato:

---RELATORIO_COMPLETO---
(TEXTO)

---RELATORIO_RESUMIDO---
(TEXTO)
"""

    response = client.models.generate_content(
        model="models/text-bison-001",
        contents=prompt
    )

    texto = response.text

    if "---RELATORIO_RESUMIDO---" not in texto:
        raise RuntimeError("A IA não retornou no formato esperado.")

    completo, resumido = texto.split("---RELATORIO_RESUMIDO---")

    completo = completo.replace("---RELATORIO_COMPLETO---", "").strip()
    resumido = resumido.strip()

    with open(f"reports/{nome_site}_relatorio_completo.txt", "w", encoding="utf-8") as f:
        f.write(completo)

    with open(f"reports/{nome_site}_relatorio_resumido.txt", "w", encoding="utf-8") as f:
        f.write(resumido)

    prompt = f"""
Você é um especialista em acessibilidade digital seguindo as diretrizes WCAG.

Explique os problemas abaixo para pessoas LEIGAS.

Crie DOIS TEXTOS:
1) RELATÓRIO COMPLETO: explicação detalhada de cada erro, impacto para pessoas com deficiência e resumo final.
2) RELATÓRIO RESUMIDO: visão geral simples, curta e direta.

Inclua a porcentagem de conformidade WCAG AA: {resultados['conformidade_wcag']['porcentagem']}%

Evite termos técnicos sem explicação.
Não use emojis.

Problemas encontrados:
{json.dumps(resultados['violations'], ensure_ascii=False, indent=2)}

Responda exatamente neste formato:

---RELATORIO_COMPLETO---
(TEXTO)

---RELATORIO_RESUMIDO---
(TEXTO)
"""

    response = client.models.generate_content(
        model="models/text-bison-001",
        contents=prompt
    )

    texto = response.text

    completo, resumido = texto.split("---RELATORIO_RESUMIDO---")

    completo = completo.replace("---RELATORIO_COMPLETO---", "").strip()
    resumido = resumido.strip()

    with open(f"reports/{nome_site}_relatorio_completo.txt", "w", encoding="utf-8") as f:
        f.write(completo)

    with open(f"reports/{nome_site}_relatorio_resumido.txt", "w", encoding="utf-8") as f:
        f.write(resumido)


# --------------------------------------------------
# Inicia navegador
# --------------------------------------------------
def iniciar_driver():
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
    except:
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )


# --------------------------------------------------
# Avaliação principal
# --------------------------------------------------
def avaliar_acessibilidade(url):
    driver = iniciar_driver()
    nome_site = extrair_nome_site(url)

    try:
        print(f"Acessando {url}")
        driver.get(url)
        time.sleep(2)

        axe = Axe(driver)
        axe.inject()
        resultados = axe.run()

        violacoes = resultados.get("violations", [])
        porcentagem_aa = calcular_conformidade_aa(violacoes)

        resultados["conformidade_wcag"] = {
            "nivel": "AA",
            "porcentagem": porcentagem_aa
        }

        os.makedirs("reports", exist_ok=True)

        with open(f"reports/{nome_site}_completo.json", "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        resumo = gerar_relatorio_resumido(resultados)
        with open(f"reports/{nome_site}_resumido.json", "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        gerar_relatorios_humanizados(resultados, nome_site)

        print("✔ Relatórios gerados com sucesso em /reports")

    finally:
        driver.quit()


# --------------------------------------------------
# Execução
# --------------------------------------------------
if __name__ == "__main__":
    url = input("Digite a URL que você deseja avaliar: ")
    avaliar_acessibilidade(url)
