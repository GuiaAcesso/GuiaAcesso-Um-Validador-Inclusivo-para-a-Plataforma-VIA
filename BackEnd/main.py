import json
import os
import time
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe
from google import genai


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
TOTAL_CRITERIOS_WCAG = 50
API_KEY_GEMINI = "AIzaSyDZzAoLx69jQYIkFNJveVESKAqJH1XXerE"
''' https://aistudio.google.com/u/3/api-keys 
    caso o codigo nao funciona , atualiza a chave da api'''

def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")


def gerar_uuid_curto():
    return uuid.uuid4().hex[:6]


def criar_pastas_site(nome_site):
    base = os.path.join(REPORTS_DIR, nome_site)
    json_dir = os.path.join(base, "json")
    txt_dir = os.path.join(base, "txt")

    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(txt_dir, exist_ok=True)

    return json_dir, txt_dir


def limpar_tudo(pasta_site, dias=30):
    agora = time.time()
    limite = dias * 86400

    for root, _, files in os.walk(pasta_site):
        for arquivo in files:
            caminho = os.path.join(root, arquivo)
            if agora - os.path.getmtime(caminho) > limite:
                os.remove(caminho)


def iniciar_gemini(api_key):
    try:
        return genai.Client(api_key=api_key) if api_key else None
    except Exception:
        return None


gemini_client = iniciar_gemini(API_KEY_GEMINI)


def extrair_nome_site(url):
    for p in ("https://", "http://", "www."):
        url = url.replace(p, "")
    return url.split("/")[0].split(".")[0]


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


def gerar_relatorio_gemini(caminho_json, caminho_txt):
    if not gemini_client:
        raise RuntimeError

    with open(caminho_json, encoding="utf-8") as f:
        dados = json.load(f)

    prompt = (
        "Crie um relatório de acessibilidade em linguagem simples para leigos.\n\n"
        f"{json.dumps(dados, ensure_ascii=False, indent=2)}"
    )

    resposta = gemini_client.models.generate_content(
        model="gemini-1.0-pro", contents=prompt
    )

    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(resposta.text.strip())

    print("Relatório humanizado gerado por IA")


def iniciar_driver():
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=ChromeOptions()
    )


def avaliar_acessibilidade(url):
    nome_site = extrair_nome_site(url)
    json_dir, txt_dir = criar_pastas_site(nome_site)

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

        caminho_completo = os.path.join(
            json_dir, f"{nome_site}_completo_{data}_{uid}.json"
        )
        caminho_resumido = os.path.join(
            json_dir, f"{nome_site}_resumido_{data}_{uid}.json"
        )
        caminho_txt = os.path.join(
            txt_dir, f"{nome_site}_relatorio_humanizado_{data}_{uid}.txt"
        )

        with open(caminho_completo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        resumo = gerar_relatorio_resumido(resultados)
        with open(caminho_resumido, "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        try:
            gerar_relatorio_gemini(caminho_resumido, caminho_txt)
        except Exception:
            gerar_relatorio_manual(caminho_resumido, caminho_txt)

        print("Processo finalizado com sucesso.")

    finally:
        driver.quit()


if __name__ == "__main__":
    url = input("Digite a URL que deseja avaliar: ").strip()
    avaliar_acessibilidade(url)
