import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe
from google import genai


REPORTS_DIR = "reports"
TOTAL_CRITERIOS_WCAG = 50
API_KEY_GEMINI = "AIzaSyCmx1TP38Z_HjI7ZvOndMHibVCXR5cr0J8"


def iniciar_gemini(api_key: str):
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None


gemini_client = iniciar_gemini(API_KEY_GEMINI)


def extrair_nome_site(url: str) -> str:
    for prefixo in ("https://", "http://", "www."):
        url = url.replace(prefixo, "")
    return url.split("/")[0].split(".")[0]


def identificar_nivel_wcag(tags: list[str]) -> list[str]:
    niveis = set()
    for tag in tags:
        if tag.endswith("aaa"):
            niveis.add("AAA")
        elif tag.endswith("aa"):
            niveis.add("AA")
        elif tag.endswith("a"):
            niveis.add("A")
    return sorted(niveis)


def calcular_conformidade_aa(violacoes: list[dict]) -> float:
    violacoes_aa = sum(
        1
        for v in violacoes
        if any(tag.endswith(("a", "aa")) for tag in v.get("tags", []))
    )
    aprovados = TOTAL_CRITERIOS_WCAG - violacoes_aa
    return round(max((aprovados / TOTAL_CRITERIOS_WCAG) * 100, 0), 2)


def gerar_relatorio_resumido(resultados: dict) -> dict:
    return {
        "conformidade_wcag": resultados["conformidade_wcag"],
        "problemas": [
            {
                "regra": v.get("id"),
                "impacto": v.get("impact"),
                "nivel_wcag": identificar_nivel_wcag(v.get("tags", [])),
                "descricao": v.get("description"),
                "elementos_afetados": len(v.get("nodes", [])),
            }
            for v in resultados.get("violations", [])
        ],
    }


def gerar_relatorio_manual(caminho_json: str, nome_site: str) -> None:
    with open(caminho_json, encoding="utf-8") as f:
        dados = json.load(f)

    linhas = [
        "RELATÓRIO DE ACESSIBILIDADE DIGITAL\n",
        f"Conformidade WCAG {dados['conformidade_wcag']['nivel']}: "
        f"{dados['conformidade_wcag']['porcentagem']}%\n",
        "PROBLEMAS IDENTIFICADOS:\n",
    ]

    for i, p in enumerate(dados["problemas"], start=1):
        linhas.extend(
            [
                f"{i}. {p['descricao']}",
                f"   Impacto: {p['impacto']}",
                f"   Nível WCAG: {', '.join(p['nivel_wcag'])}",
                f"   Elementos afetados: {p['elementos_afetados']}\n",
            ]
        )

    linhas.extend(
        ["CONCLUSÃO", "Correções são recomendadas para melhoria da acessibilidade."]
    )

    caminho_txt = os.path.join(REPORTS_DIR, f"{nome_site}_relatorio_humanizado.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print("rlatório humanizado gerado manual")


def gerar_relatorio_gemini(caminho_json: str, nome_site: str) -> None:
    if not gemini_client:
        raise RuntimeError

    with open(caminho_json, encoding="utf-8") as f:
        dados = json.load(f)

    prompt = (
        "Crie um relatório de acessibilidade para leigos usando apenas os dados abaixo.\n\n"
        f"{json.dumps(dados, ensure_ascii=False, indent=2)}"
    )

    response = gemini_client.models.generate_content(
        model="gemini-1.0-pro", contents=prompt
    )

    caminho_txt = os.path.join(REPORTS_DIR, f"{nome_site}_relatorio_humanizado.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(response.text.strip())

    print("relatório humanizado gerado por IA finalmente funciona")


def iniciar_driver() -> webdriver.Chrome:
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=ChromeOptions()
    )


def avaliar_acessibilidade(url: str) -> None:
    os.makedirs(REPORTS_DIR, exist_ok=True)

    driver = iniciar_driver()
    nome_site = extrair_nome_site(url)

    try:
        driver.get(url)
        time.sleep(2)

        axe = Axe(driver)
        axe.inject()
        resultados = axe.run()

        resultados["conformidade_wcag"] = {
            "nivel": "AA",
            "porcentagem": calcular_conformidade_aa(resultados.get("violations", [])),
        }

        caminho_completo = os.path.join(REPORTS_DIR, f"{nome_site}_completo.json")
        caminho_resumido = os.path.join(REPORTS_DIR, f"{nome_site}_resumido.json")

        with open(caminho_completo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        resumo = gerar_relatorio_resumido(resultados)
        with open(caminho_resumido, "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        try:
            gerar_relatorio_gemini(caminho_resumido, nome_site)
        except Exception:
            gerar_relatorio_manual(caminho_resumido, nome_site)

        print("Processo finalizado com sucesso.")

    finally:
        driver.quit()


if __name__ == "__main__":
    url = input("Digite a URL que deseja avaliar: ").strip()
    avaliar_acessibilidade(url)
