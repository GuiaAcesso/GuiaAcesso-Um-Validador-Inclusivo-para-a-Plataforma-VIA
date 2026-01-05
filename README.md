# GuiaAcesso — VIA  
### Validador Inclusivo de Acessibilidade Digital (WCAG)

O **VIA (Validador Inclusivo de Acessibilidade)** é uma ferramenta automatizada para análise de acessibilidade digital baseada nas diretrizes **WCAG**, com foco em **clareza, inclusão e usabilidade**.

O projeto identifica falhas de acessibilidade em páginas web, calcula o nível de conformidade **WCAG AA**, gera relatórios técnicos em JSON e produz **relatórios humanizados em linguagem simples**, podendo utilizar **IA (Google Gemini)** ou um **fallback manual**.

---

## 🚀 Funcionalidades

- ✅ Análise automática de acessibilidade com **axe-core**
- 📊 Cálculo de conformidade **WCAG nível AA**
- 📁 Geração de relatórios:
  - JSON completo (técnico)
  - JSON resumido
  - TXT humanizado (para não técnicos)
- 🤖 Relatório humanizado com **IA (Gemini)**
- 🔁 Fallback automático para relatório manual caso a IA não esteja disponível
- 🏷️ Estrutura preparada para futura geração de selo de conformidade

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Selenium WebDriver**
- **axe-selenium-python (axe-core)**
- **WebDriver Manager**
- **Google Gemini API**
- **Google Chrome**

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/GuiaAcesso-Um-Validador-Inclusivo-para-a-Plataforma-VIA.git
cd GuiaAcesso-Um-Validador-Inclusivo-para-a-Plataforma-VIA

Instale as dependências:

pip install selenium
pip install webdriver-manager
pip install axe-selenium-python
pip install --upgrade google-genai
