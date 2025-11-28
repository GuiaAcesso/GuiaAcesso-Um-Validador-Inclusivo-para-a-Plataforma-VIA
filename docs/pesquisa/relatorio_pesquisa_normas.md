# Relatório de Pesquisa: Diretrizes de Acessibilidade Digital
**Análise da Norma ABNT NBR 17225:2025 e WCAG 2.2 para o Projeto GuiaAcesso**

---

## 1. Introdução

A acessibilidade digital é um requisito fundamental para garantir que plataformas web sejam inclusivas para todas as pessoas, independentemente de suas capacidades físico-motoras, perceptivas, culturais e sociais.

Este relatório apresenta o levantamento técnico realizado para fundamentar o desenvolvimento do validador **GuiaAcesso**. A pesquisa baseia-se na norma brasileira **ABNT NBR 17225:2025** (1ª Edição), que harmoniza as diretrizes nacionais com o padrão internacional **Web Content Accessibility Guidelines (WCAG) 2.2**.

O objetivo deste estudo é identificar e categorizar os requisitos técnicos que devem ser automatizados para assegurar a conformidade de websites com a legislação vigente.

---

## 2. Fundamentação Teórica: A Estrutura da Conformidade

A norma ABNT NBR 17225 estabelece critérios claros para avaliar se um conteúdo web é acessível. A conformidade é dividida em níveis hierárquicos que determinam a profundidade da acessibilidade.

### 2.1. Níveis de Classificação
A norma classifica seus itens em três níveis, alinhados aos critérios de sucesso (C.S.) da WCAG:

* **Nível A (Essencial):** Requisitos mínimos. O não cumprimento destes itens cria barreiras que impedem o acesso da maioria dos usuários com deficiência.
* **Nível AA (Regular):** Representa o padrão de mercado e o nível de conformidade exigido para a maioria das legislações. Garante acesso a um espectro mais amplo de usuários e dispositivos.
* **Nível AAA (Recomendação):** Nível de excelência. Abrange requisitos mais rígidos e refinamentos de usabilidade, classificados na norma brasileira como "Recomendações".

### 2.2. Áreas Funcionais Cruciais
Para atingir a **Conformidade Regular** (Níveis A e AA), a pesquisa identificou sete áreas técnicas prioritárias detalhadas na Seção 5 da norma:

1.  **Interação por Teclado:** Essencial para quem não utiliza mouse. Exige que todo elemento interativo (links, botões) seja operável via teclado, com foco visível e ordem lógica.
2.  **Imagens:** Exige alternativas textuais para conteúdo não textual. Imagens informativas devem ter descrição (`alt`), enquanto imagens decorativas devem ser ignoradas por tecnologias assistivas.
3.  **Codificação e Marcação:** O código deve ser robusto e semanticamente correto (títulos únicos, idioma declarado) para ser interpretado corretamente por leitores de tela.
4.  **Conteúdo Textual e Cores:** A informação não deve depender exclusivamente de características sensoriais (como cor). O contraste entre texto e fundo deve respeitar proporções mínimas para legibilidade.
5.  **Formulários:** Campos de entrada exigem rótulos (`labels`) claros e associados programaticamente. Mensagens de erro devem ser descritivas e sugerir correções.
6.  **Multimídia:** Conteúdos de áudio e vídeo devem oferecer alternativas como legendas, transcrições e audiodescrição.
7.  **Tempo e Animação:** Usuários devem ter controle sobre limites de tempo e a capacidade de pausar conteúdos em movimento ou piscantes.

---

## 3. Resultados da Pesquisa: Checklist de Validação Técnica

A partir da análise da norma, foi elaborado um checklist com as **50 regras técnicas mais críticas** para a validação automática, organizadas por nível de severidade.

### 3.1. Requisitos de Nível A (Bloqueantes)
*O atendimento a estes itens é obrigatório para qualquer nível de acessibilidade.*

| Categoria | Regra Técnica | Referência ABNT | Critério de Validação |
| :--- | :--- | :--- | :--- |
| **Imagens** | Imagem de Conteúdo | 5.2.1 | Tag `<img>` deve ter atributo `alt` preenchido. |
| **Imagens** | Imagem Decorativa | 5.2.3 | Imagem decorativa deve ter `alt=""` (vazio). |
| **Imagens** | Imagem Funcional | 5.2.2 | Input `type="image"` deve ter `alt` descrevendo a ação. |
| **Visual** | Uso de Cores | 5.11.1 | Não usar apenas cor para indicar erro/status. |
| **Áudio** | Controle de Áudio | 5.14.7 | Áudio automático > 3s deve ter pausa. |
| **Teclado** | Acesso via Teclado | 5.1.13 | Elementos interativos devem funcionar com Teclado. |
| **Teclado** | Sem Armadilha | 5.1.6 | Foco não pode ficar preso em loop sem saída. |
| **Teclado** | Ordem de Foco | 5.1.4 | A navegação (TAB) deve seguir a leitura lógica. |
| **Navegação** | Pular Blocos | 5.7.12 | Deve haver link para ir direto ao conteúdo ("Skip Link"). |
| **Navegação** | Propósito do Link | 5.7.4 | Texto do link deve ser descritivo (evitar "clique aqui"). |
| **Estrutura** | Idioma da Página | 5.13.2 | Tag `<html>` deve ter atributo `lang`. |
| **Estrutura** | Título da Página | 5.13.1 | Tag `<title>` deve ser única e preenchida. |
| **Estrutura** | IDs Únicos | 5.13.12 | Atributo `id` não pode ser duplicado na página. |
| **Estrutura** | Semântica de Títulos | 5.3.1 | Usar tags `h1-h6` para títulos. |
| **Estrutura** | Hierarquia | 5.3.5 | Não pular níveis de cabeçalho (ex: `h1` para `h3`). |
| **Estrutura** | Listas | 5.5.1 | Listas devem usar tags `<ul>`, `<ol>`, `<dl>`. |
| **Estrutura** | Ordem de Leitura | 5.13.6 | Código HTML deve seguir a ordem visual. |
| **Formulários** | Rótulos (Labels) | 5.9.1 | Todo `<input>` deve ter `<label>` associado. |
| **Formulários** | Nome Acessível | 5.13.10 | Botões devem ter texto ou `aria-label`. |
| **Formulários** | Identificação de Erro | 5.9.9 | Erro deve ser descrito em texto junto ao campo. |
| **Formulários** | Instruções | 5.9.2 | Fornecer instruções quando a entrada é exigida. |
| **Interação** | Gestos | 5.8.12 | Funcionalidades complexas devem ter alternativa simples. |
| **Interação** | Cancelamento | 5.8.11 | Ação deve ocorrer ao soltar o clique (`up-event`). |
| **Interação** | Label no Nome | 5.13.7 | Texto visível do botão deve estar no seu nome acessível. |

### 3.2. Requisitos de Nível AA (Padrão de Mercado)
*Estes itens são exigidos para a conformidade regular e selos de qualidade.*

| Categoria | Regra Técnica | Referência ABNT | Critério de Validação |
| :--- | :--- | :--- | :--- |
| **Visual** | Contraste (Texto) | 5.11.3 | Relação mínima de **4.5:1** para texto normal. |
| **Visual** | Contraste (Gráfico) | 5.11.4 | Relação mínima de **3:1** para ícones/bordas. |
| **Visual** | Redimensionar | 5.12.7 | Zoom de até 200% sem quebrar layout. |
| **Visual** | Responsividade | 5.10.4 | Layout adapta a 320px sem rolagem horizontal. |
| **Visual** | Espaçamento | 5.12.1 | Texto suporta aumento de espaçamento sem perda. |
| **Teclado** | Foco Visível | 5.1.1 | Indicador de foco (borda) deve ser visível. |
| **Navegação** | Localização | 5.7.13 | Oferecer mais de uma via de acesso (Menu + Busca). |
| **Navegação** | Consistência | 5.7.15 | Menus na mesma ordem em todas as páginas. |
| **Interação** | Identificação | 5.8.5 | Ícones iguais devem ter a mesma função sempre. |
| **Interação** | Hover/Focus | 5.1.8 | Conteúdo em hover deve ser persistente/dispensável. |
| **Interação** | Área de Toque | 5.8.7 | Elementos interativos com tamanho mínimo de **24x24px**. |
| **Formulários** | Sugestão de Erro | 5.9.10 | Sistema deve sugerir como corrigir o erro. |
| **Formulários** | Prevenção de Erro | 5.9.12 | Dados críticos devem ser revisáveis antes do envio. |
| **Formulários** | Autocomplete | 5.9.15 | Campos comuns devem ter atributo `autocomplete`. |
| **Código** | Status Messages | 5.13.8 | Mensagens de status devem ser anunciadas (`role="status"`). |

### 3.3. Recomendações de Nível AAA (Excelência)
*Diferenciais de qualidade recomendados pela norma.*

| Categoria | Regra Técnica | Referência ABNT | Critério de Validação |
| :--- | :--- | :--- | :--- |
| **Visual** | Contraste Ouro | 5.11.2 | Relação de **7:1** para texto. |
| **Tempo** | Sem Interrupções | 5.16.4 | Usuário pode adiar alertas não urgentes. |
| **Tempo** | Sem Tempo Limite | 5.16.1 | Não há cronômetros ou podem ser desligados. |
| **Formulários** | Ajuda Contextual | 5.9.13 | Ajuda disponível para preenchimento de campos. |
| **Formulários** | Reautenticação | 5.16.5 | Sessão expira sem perda de dados. |
| **Interação** | Área de Toque+ | 5.8.6 | Elementos com tamanho mínimo de **44x44px**. |
| **Navegação** | Migalhas de Pão | 5.7.14 | Usuário sabe onde está na hierarquia. |
| **Conteúdo** | Leitura Simples | 5.12.12 | Nível de leitura adequado ou versão simplificada. |
| **Conteúdo** | Pronúncia | 5.12.13 | Identificação de pronúncia de palavras ambíguas. |
| **Estrutura** | Cabeçalhos Totais | 5.3.4 | Seções iniciadas obrigatoriamente por cabeçalhos. |
| **Visual** | Sem Flash | 5.15.3 | Nada deve piscar mais de 3 vezes por segundo. |

---

## 4. Pontos de Atenção e Desempenho Funcional

Além das regras de validação automática, a pesquisa destacou itens nos Anexos A e B da norma que exigem atenção especial durante o desenvolvimento para garantir o desempenho funcional:

* **CAPTCHA (A.1.1):** Deve oferecer alternativa não visual (ex: desafio lógico simples ou áudio) e não depender apenas de reconhecimento de caracteres.
* **Biometria (A.1.2):** Não pode ser a única forma de acesso. Deve haver alternativa (senha/PIN).
* **Tabelas de Layout (A.1.8):** É recomendado não utilizar tabelas `<table>` para diagramação visual, apenas para dados tabulares.
* **Utilização sem Visão (B.1.1):** A estrutura semântica correta (Títulos, Regiões) é o que permite que usuários cegos naveguem com autonomia.
* **Utilização com Cognição Limitada (B.1.10):** A consistência na navegação e a tolerância a erros (mensagens claras, tempo ajustável) são cruciais para este grupo.

## 5. Conclusão

A análise da norma ABNT NBR 17225 confirma que a legislação brasileira possui requisitos técnicos claros e mapeáveis para automação. O sistema **GuiaAcesso** utilizará este mapeamento para traduzir os erros técnicos encontrados pelas bibliotecas de análise (como `Axe`) em relatórios compreensíveis, citando diretamente as seções da norma brasileira para orientar as correções.