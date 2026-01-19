###### PT-BR

# GuiaAcesso — VIA  
### Validador Inclusivo de Acessibilidade Digital (WCAG)

⚠️ **ATENÇÃO — REQUISITOS OBRIGATÓRIOS**  
Para utilizar este projeto, é necessário ter:

- ✅ **Python 3 instalado** (recomendado Python 3.10 ou superior)
- ✅ **Google Chrome instalado** no sistema

Sem esses requisitos, o projeto **não funcionará corretamente**, pois utiliza Selenium com ChromeDriver.

---

## 📘 Sobre o Projeto

O **GuiaAcesso — VIA (Validador Inclusivo de Acessibilidade)** é uma ferramenta automatizada para análise de acessibilidade digital baseada nas diretrizes **WCAG 2.1** e **eMAG**.

O sistema analisa páginas web, identifica falhas de acessibilidade, calcula o nível de conformidade **WCAG nível AA** e gera **relatórios técnicos e humanizados**, incluindo **PDF profissional com marca d’água**, voltado tanto para equipes técnicas quanto para gestores e usuários não técnicos.

---

## 🚀 Funcionalidades

- ✅ Análise automática de acessibilidade com **axe-core**
- 📊 Cálculo de conformidade **WCAG nível AA**
- 📁 Geração automática de relatórios:
  - **JSON completo** (dados técnicos detalhados)
  - **JSON resumido**
  - **TXT humanizado** (linguagem simples e acessível)
  - **PDF profissional** com marca d’água
- 🤖 Relatório humanizado gerado por **IA (Groq via OpenAI SDK)**
- 🔁 Fallback automático para relatório manual caso a IA falhe
- 📂 Organização automática por site analisado
- 📄 Abertura automática do PDF ao final da execução
- 🧱 Estrutura preparada para **escalabilidade do projeto**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Selenium WebDriver**
- **axe-selenium-python (axe-core)**
- **WebDriver Manager**
- **OpenAI SDK (Groq)**
- **Markdown**
- **xhtml2pdf**
- **PyPDF**
- **ReportLab**
- **Google Chrome**

---

## 📦 Instalação e Execução

### 1️⃣ Clone o repositório

```bash
git clone https://github.com.seu-usuarioGuiaAcesso-Um-Validador-Inclusivo-para-a-Plataforma-VIA.git

cd GuiaAcesso-Um-Validador-Inclusivo-para-a-Plataforma-VIA
```
### 2️⃣ Instale todas as dependências (de uma só vez)

⚠️ Este comando deve ser executado na RAIZ do projeto
```
pip install -r requirements.txt
```
Esse comando instalará todas as bibliotecas necessárias, com versões compatíveis, de forma automática.
### 3️⃣ Crie o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione a chave da API conforme o modelo disponível em `.env.example`.

> ⚠️ **Importante:** nunca versionar o arquivo `.env`. Ele contém informações sensíveis.

### 4️⃣ Execute o projeto

Entre na pasta BackEnd:
```
cd BackEnd
```

Execute o arquivo principal:

```
python main.py
```

Também é possível executar o arquivo main.py diretamente pela sua IDE.

### 5️⃣ Informe a URL

No terminal, cole uma URL válida quando solicitado:

Digite a URL que deseja avaliar:


Exemplo:

- *https://www.google.com*


Caso a URL seja inválida, o sistema exibirá a mensagem:

link invalido , digite novamente :


permitindo que o usuário informe uma nova URL sem que o programa quebre.

📄 Saída do Projeto

Ao final da execução:

📂 Será criada automaticamente uma pasta em BackEnd/reports/ com o nome do site analisado

📁 Dentro dessa pasta estarão:

/json → arquivos .json (completo e resumido)

/txt → relatório humanizado em .txt

/pdf → relatório final em PDF

📄 O PDF será aberto automaticamente

🖥️ O terminal exibirá o caminho completo onde os arquivos foram gerados

Essa estrutura permite que o projeto seja facilmente expandido, integrado a APIs ou adaptado para novos fluxos.

📂 Estrutura do Projeto (resumo)
```
BackEnd/
├── assets/
│   └── logo.png
├── reports/
│   └── site_analisado/
│       ├── json/
│       ├── txt/
│       └── pdf/
├── utils/
│   ├── gerador_prompt.py
│   ├── llm_relatorio.py
│   └── md_pdf.py
├── main.py
└── .env
```

### 🤝 Agradecimentos

Um agradecimento especial às pessoas que contribuíram para este projeto:


## 🤝 Time de Desenvolvimento

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Veroshy">
        <img src="https://github.com/Veroshy.png" width="80px;" alt="Foto Guinevere"/><br>
        <sub><b>Guinevere Cavalcanti</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/wk-ss">
        <img src="https://github.com/wk-ss.png" width="80px;" alt="Foto Willians"/><br>
        <sub><b>Willians Keiichi</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/AndrezaGSantana">
        <img src="https://github.com/AndrezaGSantana.png" width="80px;" alt="Foto Andreza"/><br>
        <sub><b>Andreza Gomes</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MCantalice">
        <img src="https://github.com/MCantalice.png" width="80px;" alt="Foto Maria"/><br>
        <sub><b>Maria Cantalice</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/thais-collab">
        <img src="https://github.com/thais-collab.png" width="80px;" alt="Foto Thais"/><br>
        <sub><b>Thais Adryene</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/C-Juniorr">
        <img src="https://github.com/C-Juniorr.png" width="80px;" alt="Foto Clodoaldo"/><br>
        <sub><b>Clodoaldo Junior</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jotav06">
        <img src="https://github.com/jotav06.png" width="80px;" alt="Foto João"/><br>
        <sub><b>João Victor</b></sub>
      </a>
    </td>
  </tr>
</table>
