import json
import os
import time
import uuid
import webbrowser
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe

from utils.gerador_prompt import gerar_prompt_relatorio
from utils.llm_relatorio import gerar_relatorio_llm
from utils.md_pdf import gerar_pdf_relatorio


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
TOTAL_CRITERIOS_WCAG = 50
LOGO_PATH = os.path.join(BASE_DIR, "assets", "logo.png")


def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")


def gerar_uuid_curto():
    return uuid.uuid4().hex[:6]


def extrair_nome_site(url):
    for p in ("https://", "http://", "www."):
        url = url.replace(p, "")
    return url.split("/")[0].split(".")[0]


def criar_pastas_site(nome_site):
    base = os.path.join(REPORTS_DIR, nome_site)
    json_dir = os.path.join(base, "json")
    txt_dir = os.path.join(base, "txt")
    pdf_dir = os.path.join(base, "pdf")

    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(txt_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    return json_dir, txt_dir, pdf_dir


def limpar_tudo(pasta_site, dias=30):
    agora = time.time()
    limite = dias * 86400

    for root, _, files in os.walk(pasta_site):
        for arquivo in files:
            caminho = os.path.join(root, arquivo)
            if agora - os.path.getmtime(caminho) > limite:
                os.remove(caminho)


def identificar_nivel_wcag(tags):
    niveis = set()
    for tag in tags:
        if tag.endswith("aaa"):
            niveis.add("AAA")
        elif tag.endswith("aa"):
            niveis.add("AA")
        elif tag.endswith("a"):
            niveis.add("A")
    return sorted(niveis)


def calcular_conformidade_aa(violacoes):
    violacoes_aa = sum(
        1
        for v in violacoes
        if any(tag.endswith(("a", "aa")) for tag in v.get("tags", []))
    )
    aprovados = TOTAL_CRITERIOS_WCAG - violacoes_aa
    return round(max((aprovados / TOTAL_CRITERIOS_WCAG) * 100, 0), 2)


def gerar_relatorio_resumido(resultados):
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


def gerar_relatorio_manual(caminho_json, caminho_txt):
    with open(caminho_json, encoding="utf-8") as f:
        dados = json.load(f)

    linhas = [
        "RELATÓRIO DE ACESSIBILIDADE DIGITAL\n",
        f"Conformidade WCAG {dados['conformidade_wcag']['nivel']}: "
        f"{dados['conformidade_wcag']['porcentagem']}%\n",
        "PROBLEMAS IDENTIFICADOS:\n",
    ]

    for i, p in enumerate(dados["problemas"], 1):
        linhas.extend(
            [
                f"{i}. {p['descricao']}",
                f"   Impacto: {p['impacto']}",
                f"   Nível WCAG: {', '.join(p['nivel_wcag'])}",
                f"   Elementos afetados: {p['elementos_afetados']}\n",
            ]
        )

    linhas.append("Correções são recomendadas para melhoria da acessibilidade.")

    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print("Relatório humanizado gerado manualmente")


def gerar_relatorio_llm_txt(url, resumo_json, caminho_txt):
    prompt = gerar_prompt_relatorio(url, resumo_json)
    texto = gerar_relatorio_llm(prompt)

    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(texto.strip())

    print("Relatório humanizado gerado por LLM (Groq)")


def iniciar_driver():
    options = ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    options.add_argument("--window-size=1920,1080")

    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-popup-blocking")

    options.add_argument("--log-level=3")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )

    driver.execute_cdp_cmd("Page.setWebLifecycleState", {"state": "frozen"})

    return driver


def obter_url_valida():
    while True:
        url = input("Digite a URL que deseja avaliar: ").strip()

        if not url.startswith(("http://", "https://")):
            print("link invalido , digite novamente :")
            continue

        driver = None
        try:
            driver = iniciar_driver()
            driver.set_page_load_timeout(15)
            driver.get(url)
            return url
        except (WebDriverException, TimeoutException):
            print("link invalido , digite novamente :")
        finally:
            if driver:
                driver.quit()


def limpar_pycache(pasta_base):
    """Apaga todos os __pycache__ dentro de pasta_base recursivamente"""
    for root, dirs, _ in os.walk(pasta_base):
        for d in dirs:
            if d == "__pycache__":
                caminho = os.path.join(root, d)
                try:
                    for arquivo in os.listdir(caminho):
                        os.remove(os.path.join(caminho, arquivo))
                    os.rmdir(caminho)
                except Exception as e:
                    print(f"Erro ao limpar {caminho}: {e}")


def avaliar_acessibilidade(url):
    nome_site = extrair_nome_site(url)
    json_dir, txt_dir, _ = criar_pastas_site(nome_site)

    limpar_tudo(os.path.join(REPORTS_DIR, nome_site), dias=30)

    driver = iniciar_driver()
    uid = gerar_uuid_curto()
    data = timestamp()

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

        nome_base = f"{nome_site}_relatorio_humanizado_{data}_{uid}"

        caminho_completo = os.path.join(
            json_dir, f"{nome_site}_completo_{data}_{uid}.json"
        )
        caminho_resumido = os.path.join(
            json_dir, f"{nome_site}_resumido_{data}_{uid}.json"
        )
        caminho_txt = os.path.join(txt_dir, f"{nome_base}.txt")

        with open(caminho_completo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        resumo = gerar_relatorio_resumido(resultados)

        with open(caminho_resumido, "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        try:
            gerar_relatorio_llm_txt(url, resumo, caminho_txt)
        except Exception as e:
            print("Erro na LLM, usando fallback manual:", e)
            gerar_relatorio_manual(caminho_resumido, caminho_txt)

        pdf_final = gerar_pdf_relatorio(
            caminho_txt=caminho_txt,
            pasta_site=os.path.join(REPORTS_DIR, nome_site),
            nome_base=nome_base,
            logo_path=LOGO_PATH,
        )

        print("Processo finalizado com sucesso.")

        if os.path.exists(pdf_final):
            webbrowser.open(f"file:///{os.path.abspath(pdf_final)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    url_valida = obter_url_valida()
    avaliar_acessibilidade(url_valida)
    limpar_pycache(BASE_DIR)
