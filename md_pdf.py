import markdown
import pdfkit
from xhtml2pdf import pisa
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color

def aplicar_marca_dagua(pdf_original, pdf_marca, pdf_final):
    reader = PdfReader(pdf_original)
    marca = PdfReader(pdf_marca)
    writer = PdfWriter()

    pagina_marca = marca.pages[0]

    for pagina in reader.pages:
        pagina.merge_page(pagina_marca)
        writer.add_page(pagina)

    with open(pdf_final, "wb") as f:
        writer.write(f)

def criar_marca_dagua_com_imagem(caminho_pdf_marca, logo_path):
    c = canvas.Canvas(caminho_pdf_marca, pagesize=A4)
    largura, altura = A4

    c.saveState()
    c.setFillAlpha(0.25)

    c.translate(largura / 2, altura / 2)
    c.rotate(30)

    c.drawImage(
        logo_path,
        -200,
        -200,
        width=400,
        height=400,
        mask='auto'
    )

    c.restoreState()
    c.save()




def markdown_para_html(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "tables", "toc", "fenced_code"]
    )

    html = f"""
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">

        <style>
            @page {{
                size: A4;
                margin: 2.5cm;
            }}

            body {{
                font-family: "Helvetica", "Arial", sans-serif;
                font-size: 11pt;
                color: #2c3e50;
                line-height: 1.6;
            }}

            /* Cabeçalho */
            .header {{
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 2px solid #2980b9;
                padding-bottom: 10px;
            }}

            .header h1 {{
                margin: 0;
                font-size: 22pt;
                color: #2980b9;
            }}

            .header p {{
                margin: 5px 0 0;
                font-size: 10pt;
                color: #7f8c8d;
            }}

            /* Títulos */
            h1, h2, h3 {{
                color: #2c3e50;
                margin-top: 25px;
            }}

            h2 {{
                border-bottom: 1px solid #ccc;
                padding-bottom: 4px;
            }}

            h3 {{
                color: #34495e;
            }}

            /* Parágrafos */
            p {{
                margin: 10px 0;
                text-align: justify;
            }}

            /* Listas */
            ul, ol {{
                margin-left: 20px;
            }}

            li {{
                margin-bottom: 5px;
            }}

            /* Tabelas */
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 10pt;
            }}

            th {{
                background-color: #2980b9;
                color: white;
                padding: 8px;
                border: 1px solid #ddd;
                text-align: left;
            }}

            td {{
                padding: 8px;
                border: 1px solid #ddd;
            }}

            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}

            /* Código */
            pre {{
                background-color: #f4f6f7;
                border-left: 4px solid #2980b9;
                padding: 10px;
                font-size: 9pt;
                overflow-x: auto;
            }}

            code {{
                font-family: "Courier New", monospace;
                color: #c0392b;
            }}

            /* Rodapé */
            .footer {{
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                text-align: center;
                font-size: 9pt;
                color: #7f8c8d;
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Relatório Técnico</h1>
            <p>Gerado por Via_Access</p>
        </div>

        {html_body}

        <div class="footer">
            Página <pdf:pagenumber /> de <pdf:pagecount />
        </div>

    </body>
    </html>
    """

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)



import subprocess
import shutil

import subprocess

def md_para_pdf(md_file, pdf_file):
    pass
    with open(md_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    pdfkit.from_string(html_content, pdf_file)


html_file = "reports/relatorio_humanizado.html"
with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()


def html_para_pdf(html, nome_arquivo):
    with open(nome_arquivo, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)
    return pisa_status.err


#html_file = "reports/relatorio_humanizado.html"
#pdf_file = "reports/Relatorio_GuiaAcesso.pdf"
#md_para_pdf(html_file, pdf_file)