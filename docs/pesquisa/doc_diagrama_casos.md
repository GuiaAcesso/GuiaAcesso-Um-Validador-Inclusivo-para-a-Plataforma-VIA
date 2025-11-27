# Documentação do Diagrama de Casos de Uso - Sistema VIA


### 1. Visão Geral e Objetivo

O **Sistema VIA** é uma plataforma especializada na avaliação de acessibilidade em sites, com foco em identificar possíveis barreiras que possam impedir o acesso de pessoas com deficiência no geral.

A ferramenta permite que clientes enviem URLs, qu eprofissionais de TI executem diagnósticos baseados em diretrizes como WCAG, e que gestores visualizem relatórios humanizados com os principais problemas encontrados e sugestões de correções.

O objetivo principal do Sistema VIA é facilitar a adequação de sites à normas de acessibilidade digital, promovendo inclusão, conformidade e melhor experiência para todos os usuários.


### 2. Atores Envolvidos

Os atores foram estruturados de forma unificada para facilitar a compreensão do fluxo de desenvolvimento:

| Ator | Papéis Principais |
| :--- | :--- |
| **Cliente**| Responsável por cadastrar o site que será analisado quanto a critérios de acessibilidade. |
| **Desenvolvedor TI** |Executa o diagnóstico técnico da acessibilidade do site, utilizando ferramentas internas do sistema. |
| **Gerente do Projeto** | Acompanha os resultados por meio de relatórios humanizados, facilitando decisões relacionadas à implementação de melhorias. |


### 3. Casos de Uso 

 #### 3.1 Cadastrar Site para Análise

 - Ator Principal: Cliente
 - Objetivo: Enviar a URL do site para que o sistema execute a análise de acessibilidade.
 - Descrição:

   1. O cliente acessa o sistema.

   2. Informa a URL do site.

   3. O sistema registra o site na fila de análises de acessibilidade.

 #### 3.2 Realizar Diagnóstico do Site

 - Ator Principal: Desenvolvedor TI
 - Objetivo: Iniciar um diagnóstico automatizado e, se necessário, manual, sobre a acessibilidade do site.
 - Descrição:

  1. O desenvolvedor seleciona o site cadastrado.

  2. O sistema executa verificações baseadas nas diretrizes WCAG (contraste, textos alternativos, navegação por teclado, entre outros.).

  3. O caso de uso inclui:

      - Identificar Soluções e Correções

 #### 3.3 Identificar Soluções e Correções 

 - Ator Principal: — (Executado pelo sistema)
 - Objetivo: Identificar problemas de acessibilidade e sugerir ações corretivas.
 - Possíveis saídas:

   - Alertas sobre ausência de texto alternativo
 
   - Problemas de contraste

   - Problemas de navegação via teclado

   - Estrutura HTML inadequada

   - Uso incorreto de ARIA

   - Falta de responsividade

   - Recomendações técnicas com base na WCAG

   Este processo é acionado automaticamente sempre que o diagnóstico é realizado.

 #### 3.4 Visualizar Relatório Humanizado

 - Atores: Cliente, Desenvolvedor TI, Gerente do Projeto
 - Objetivo: Exibir os resultados do diagnóstico em um relatório acessível e de fácil compreensão.
 - Conteúdo do relatório:
 
   - Resumo geral da avaliação
 
   - Lista de barreiras encontradas
 
   - Sugestões de correção explicadas de forma simples
 
   - Priorização dos problemas (alta, média, baixa)
  
   - Impacto na experiência de usuários com deficiência
 
   - Recomendações baseadas no WCAG
 
  Esse caso de uso inclui:

   - Identificar Soluções e Correções, pois o relatório depende dessas informações.


### 4. Relacionamentos entre os Casos de Uso

| Caso de Uso | Tipo | Relacionado a | Descrição |
|:---|:---|:---|:---|
| Realizar Diagnóstico do Site | include | Identificar Soluções e Correções | A análise só é concluída após identificar barreiras e soluções. |
| Visualizar Relatório Humanizado | include | Identificar Soluções e Correções | O relatório depende dos problemas/sugestões encontradas no diagnóstico. |


### 5. Descrição do Diagrama

 O diagrama apresenta:

  - Três atores principais interagindo com funcionalidades do Sistema VIA.

  - Os casos de uso organizados dentro da fronteira do sistema.

  - O processo de diagnóstico e geração de relatório como atividades centrais.

  - Uso de **include** para processos obrigatórios (identificação de soluções).

  - Diferentes níveis de interesse e interação:

     - Cliente inicia a análise,

     - Desenvolvedor executa o diagnóstico técnico,

     - Gerente e cliente visualizam o relatório final.