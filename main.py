from selenium import webdriver #Importa o módulo principal do Selenium, usado para controlar o navegador.
from selenium.webdriver.chrome.service import Service #Importa a classe Service, usada para configurar o serviço do ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager #Importa uma ferramenta que baixa automaticamente a versão correta do ChromeDriver.
from axe_selenium_python import Axe #Importa a biblioteca AXE, usada para rodar testes de acessibilidade no navegador.
import json #Permite salvar dados em arquivos JSON.
import time #Permite usar sleep() para esperar alguns segundos.
import os #Permite criar pastas, verificar arquivos, etc.

def gerar_relatorio_resumido(resultados):
    resumo = []

    for violacao in resultados["violations"]:
        item = {
            "regra": violacao.get("id"),
            "impacto": violacao.get("impact"),
            "descricao": violacao.get("description"),
            "ajuda": violacao.get("help"),
            "elementos_afetados": len(violacao.get("nodes", []))
        }
        resumo.append(item)

    return resumo


def avaliar_acessibilidade(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        print(f"Acessando a seguinte url: {url}")
        driver.get(url)
        time.sleep(2)

        axe = Axe(driver)
        axe.inject()

        print("Fazendo de acessibilidade...")
        resultados = axe.run()

        violacoes = resultados["violations"]
        print(f"Total de violações encontradas: {len(violacoes)}")

        # Cria pasta para relatórios
        if not os.path.exists("reports"):
            os.makedirs("reports")

        # Caminhos dos arquivos
        relatorio_completo = "reports/resultado_axe_completo.json"
        relatorio_resumido = "reports/resultado_axe_resumido.json"

        # Relatório completo
        with open(relatorio_completo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        # Relatório resumido
        resumo = gerar_relatorio_resumido(resultados)
        with open(relatorio_resumido, "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        print(f"Relatório completo salvo em: {relatorio_completo}")
        print(f"Relatório resumido salvo em: {relatorio_resumido}")

        return resultados

    finally:
        driver.quit()


if __name__ == "__main__":
    url = input("Digite a URL que você deseja avaliar: ")
    avaliar_acessibilidade(url)
