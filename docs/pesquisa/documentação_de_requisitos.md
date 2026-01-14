# Documentação de Requisitos – Sistema VIA

**Projeto:** GuiaAcesso: Validador Inclusivo de Acessibilidade  
**Cliente:** T-Access (Consultoria em Acessibilidade)  

---

## 1. Visão do Produto e Negócio

O **Sistema VIA** é uma ferramenta de automação desenvolvida para sustentar o serviço de **Consultoria em Acessibilidade** da T-Access.

Seu objetivo é realizar varreduras técnicas automáticas em sites e transformar dados complexos em **relatórios com linguagem acessível**. A ferramenta atende dois públicos estratégicos:  
1.  **Interno (T-Access):** Otimiza o tempo dos analistas, eliminando a verificação manual repetitiva.  
2.  **Externo (Clientes):** Entrega valor tangível e monitoramento contínuo para as empresas que contratam a consultoria.

---

## 2. Requisitos Funcionais (RF)

### 2.1 Módulo de Segurança e Operação
*Define as diretrizes de execução segura da ferramenta.*

**[RF01] Controle de Execução (Ambiente Seguro)** O sistema deve operar em ambiente controlado (Console/Terminal), restringindo a execução das varreduras apenas a analistas autorizados com acesso à infraestrutura. Isso garante que dados sensíveis dos clientes não sejam expostos em interfaces públicas indevidas.

**[RF02] Gestão de Credenciais de IA** O sistema deve realizar a autenticação com serviços externos (Groq Cloud) utilizando chaves de API criptografadas ou armazenadas estritamente em variáveis de ambiente local (`.env`), eliminando o risco de exposição de segredos no código-fonte.

---

### 2.2 Módulo de Análise (O Motor - MVP)

**[RF03] Submissão e Validação de URL** O sistema deve fornecer uma interface de entrada para recebimento da URL a ser analisada.  
* *Regra de Negócio:* O sistema deve validar automaticamente se a URL está ativa (status online 200 OK) e acessível antes de iniciar o processamento.

**[RF04] Motor de Varredura e Simulação** O sistema deve utilizar um navegador automatizado (**Selenium Webdriver**) para carregar a página completa, renderizar o DOM e executar a biblioteca de auditoria (**Axe-core**).  
* *Justificativa:* O uso de navegador real é obrigatório para identificar erros em elementos dinâmicos carregados via JavaScript.

**[RF05] Identificação de Falhas (Checklist Técnico)** O sistema deve detectar e listar falhas de acessibilidade, cobrindo obrigatoriamente os seguintes itens da WCAG 2.2:  
* Contraste de cores inadequado.  
* Imagens sem texto alternativo (Alt Text).  
* Campos de formulário sem rótulos (Labels).  
* Estrutura incorreta de cabeçalhos (H1-H6).  
* Ausência de atributos ARIA essenciais.

**[RF06] Classificação e Normalização** O sistema deve processar os dados brutos da varredura para:  
1.  Classificar as falhas por gravidade: **Crítico, Sério, Moderado, Menor**.  
2.  Agrupar erros similares para facilitar a leitura.

---

### 2.3 Módulo de Inteligência e Relatórios (A Entrega)

**[RF07] Processamento de Linguagem Natural (GenAI)** O sistema deve utilizar Inteligência Artificial Generativa (**Modelo Llama 3 via API Groq**) para interpretar os dados técnicos brutos.  
* *Requisito de IA:* O modelo deve gerar explicações contextuais, pedagógicas e humanizadas em Português (PT-BR), substituindo o "jargão técnico" por orientações de negócio.

**[RF08] Cálculo de Score de Qualidade** O sistema deve aplicar um algoritmo que pondera a quantidade e a gravidade dos erros para atribuir uma **Nota Final (0 a 100)** ao site analisado, criando um indicador de performance (KPI) claro para o gestor.

**[RF09] Geração de Relatório PDF Profissional** O sistema deve compilar os resultados em um arquivo PDF formatado automaticamente, contendo:  
* **Cabeçalho:** Metadados da página, cliente e data da análise.  
* **Sumário Executivo:** Quadro visual com a Nota Final e o resumo dos erros.  
* **Detalhamento Humanizado:** Lista sequencial das falhas com explicações geradas pela IA.  
* **Identidade Visual:** Aplicação de marca d'água oficial da T-Access.

---

## 3. Requisitos Não Funcionais (Padrões de Qualidade)

*Estes requisitos definem a robustez, segurança e manutenibilidade do sistema.*

**[RNF01] Stack Tecnológica e Arquitetura** O sistema deve ser desenvolvido em **Python 3.x** utilizando arquitetura modular.  
* *Componentes Core:* Selenium (Automação), OpenAI Client (Integração IA Groq), xhtml2pdf (Motor de Documentos).

**[RNF02] Conformidade Normativa** O sistema deve utilizar bibliotecas de análise consolidadas (*Axe-core*) para garantir que a validação técnica siga estritamente os critérios da **WCAG 2.2** e da norma brasileira **ABNT NBR 17225**.

**[RNF03] Segurança e Proteção de Dados (Security by Design)** O sistema deve implementar práticas de segurança de infraestrutura:  
* **Proteção de Chaves:** Nenhuma credencial de API deve ser "hardcoded" (escrita diretamente) no repositório de código.  
* **Tratamento de Erros:** O sistema deve possuir mecanismos de contingência (`try/except`) para evitar falhas críticas em caso de indisponibilidade da API de IA.

**[RNF04] Manutenibilidade e Código Limpo** O código-fonte deve seguir as diretrizes da **PEP-8** (Style Guide for Python Code), garantindo legibilidade e facilidade de manutenção para futuras evoluções do produto (como a criação de interface Web).