import os

import markdown
from xhtml2pdf import pisa
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# =========================================================
# CRIA PDF DE MARCA D’ÁGUA (IMAGEM MAIS SUAVE)
# =========================================================
def criar_marca_dagua_com_imagem(caminho_pdf_marca: str, logo_path: str):
    c = canvas.Canvas(caminho_pdf_marca, pagesize=A4)
    largura, altura = A4

    c.saveState()

    # 🔽 Opacidade reduzida (marca d’água mais clara)
    c.setFillAlpha(0.15)

    c.translate(largura / 2, altura / 2)
    c.rotate(30)

    c.drawImage(
        logo_path,
        -150,
        -150,
        width=300,
        height=300,
        mask="auto",
    )

    c.restoreState()
    c.save()


# =========================================================
# APLICA MARCA D’ÁGUA EM TODAS AS PÁGINAS
# =========================================================
def aplicar_marca_dagua(pdf_original: str, pdf_marca: str, pdf_final: str):
    reader = PdfReader(pdf_original)
    marca = PdfReader(pdf_marca)
    writer = PdfWriter()

    pagina_marca = marca.pages[0]

    for pagina in reader.pages:
        pagina.merge_page(pagina_marca)
        writer.add_page(pagina)

    with open(pdf_final, "wb") as f:
        writer.write(f)


# =========================================================
# CONVERTE MARKDOWN → HTML (TEXTO MAIS ESCURO)
# =========================================================
def markdown_para_html(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "tables", "toc", "fenced_code"],
    )

    return f"""
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <style>
        @page {{
            size: A4;
            margin: 2.5cm;
        }}

        body {{
            font-family: Helvetica, Arial, sans-serif;
            font-size: 11.5pt;
            color: #1a1a1a;
            line-height: 1.7;
        }}

        h1, h2, h3 {{
            margin-top: 25px;
            color: #000000;
        }}

        h2 {{
            border-bottom: 1px solid #bbb;
            padding-bottom: 4px;
        }}

        p {{
            text-align: justify;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}

        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
        }}

        th {{
            background-color: #2c3e50;
            color: white;
        }}

        .footer {{
            position: fixed;
            bottom: 0;
            text-align: center;
            font-size: 9pt;
            color: #555;
        }}
    </style>
</head>

<body>
    {html_body}

    <div class="footer">
        Página <pdf:pagenumber /> de <pdf:pagecount />
    </div>
</body>
</html>
"""


# =========================================================
# CONVERTE HTML → PDF
# =========================================================
def html_para_pdf(html: str, pdf_path: str):
    with open(pdf_path, "wb") as f:
        pisa.CreatePDF(html, dest=f)


# =========================================================
# FUNÇÃO PRINCIPAL DE GERAÇÃO DO PDF
# =========================================================
def gerar_pdf_relatorio(
    caminho_txt: str,
    pasta_site: str,
    nome_base: str,
    logo_path: str,
):
    """
    - caminho_txt: reports/site/txt/arquivo.txt
    - pasta_site: reports/site/
    - nome_base: nome do arquivo sem extensão
    """

    pasta_pdf = os.path.join(pasta_site, "pdf")
    os.makedirs(pasta_pdf, exist_ok=True)

    pdf_temp = os.path.join(pasta_pdf, f"{nome_base}_temp.pdf")
    pdf_final = os.path.join(pasta_pdf, f"{nome_base}.pdf")
    pdf_marca = os.path.join(pasta_pdf, "marca_dagua.pdf")

    # Lê o texto base (gerado pela LLM ou fallback manual)
    with open(caminho_txt, encoding="utf-8") as f:
        texto = f.read()

    # Markdown → HTML
    html = markdown_para_html(texto)

    # HTML → PDF temporário
    html_para_pdf(html, pdf_temp)

    # Marca d’água
    criar_marca_dagua_com_imagem(pdf_marca, logo_path)
    aplicar_marca_dagua(pdf_temp, pdf_marca, pdf_final)

    # Limpeza
    os.remove(pdf_temp)
    os.remove(pdf_marca)

    print(f"PDF gerado com sucesso em: {pdf_final}")

    return pdf_final
