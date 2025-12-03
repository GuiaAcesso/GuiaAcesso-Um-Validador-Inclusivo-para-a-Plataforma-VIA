================================================================================
                     DOCUMENTAÇÃO DO DIAGRAMA DE FLUXO 
================================================================================

1. ATORES ENVOLVIDOS
--------------------------------------------------------------------------------
1.1 ADMINISTRADOR
      - Gerencia usuários
      - Cadastra clientes
      - Associa usuários a clientes

1.2 ANALISTA
      - Visualiza e opera análises

1.3 CLIENTE
      - Envia URLs para análise
      - Acompanha histórico e baixa relatórios

1.4 WEBHOOK (Sistema Externo)
      - Recebe notificações automáticas após conclusão de análises


2. FLUXO PASSO A PASSO
================================================================================

2.1 ACESSO E USUÁRIOS
--------------------------------------------------------------------------------
2.1.1 Iniciar Autenticação  
2.1.2 Autenticar Usuário  
        -> Se falhar, retorno ao login  
        -> Se sucesso, libera acesso  

2.1.3 Gerenciar Usuários (Administrador)
        - Criar / editar / desativar usuários

2.1.4 Cadastro de Usuário  
2.1.5 Cadastrar Cliente  
2.1.6 Associar Usuário ao Cliente  

--------------------------------------------------------------------------------


2.2 ANÁLISE DE ACESSIBILIDADE
================================================================================

2.2.1 Enviar URL para Análise (Cliente)

2.2.2 Executar Análise de Acessibilidade

2.2.3 Verificar Condição:
        URL INVÁLIDA OU BLOQUEADA?
        ---------------------------------------
        | SIM  -> Tratar URL inválida         |
        | NÃO  -> Prosseguir análise          |
        ---------------------------------------

2.2.4 Executar Varredura Axe ou Lighthouse  
2.2.5 Processar Scripts Dinâmicos  
2.2.6 Identificar Falhas de Acessibilidade  
2.2.7 Classificar Gravidade dos Erros  
2.2.8 Calcular Conformidade WCAG 2.2  
2.2.9 Extrair Metadados da Página  
2.2.10 Normalizar Resultados  
2.2.11 Armazenar Histórico da Análise  
2.2.12 Enviar Notificação via Webhook (se configurado)

--------------------------------------------------------------------------------


2.3 GERAÇÃO DE RELATÓRIO
--------------------------------------------------------------------------------
2.3.1 Gerar Relatório em PDF  
          - Lista completa de erros  
          - Severidades  
          - Recomendações  
          - Grau de conformidade  

--------------------------------------------------------------------------------


2.4 CONSULTA E RELATÓRIOS
--------------------------------------------------------------------------------
2.4.1 Consultar Histórico de Análises  
2.4.2 Baixar Relatório em PDF  

FIM DO FLUXO

================================================================================


3. ESTRUTURA DE DADOS (CLASSES E ATRIBUTOS)
================================================================================

3.1 CLASSE USUÁRIO
--------------------------------------------------------------------------------
- id  
- nome  
- email  
- senha_hash  
- perfil (ADMIN, ANALISTA, CLIENTE)  
- status_ativo  
- cliente_id (opcional)

3.2 CLASSE CLIENTE
--------------------------------------------------------------------------------
- id  
- nome  
- cnpj (opcional)  
- data_cadastro  
- status  

3.3 CLASSE ANALISE
--------------------------------------------------------------------------------
- id  
- cliente_id  
- url_analisada  
- status (pendente, analisada, erro)  
- data_solicitacao  
- data_conclusao  
- conformidade_wcag  
- total_erros  
- total_alertas  
- metadados (json)  

3.4 CLASSE RESULTADO_ACESSIBILIDADE
--------------------------------------------------------------------------------
- id  
- analise_id  
- tipo_erro  
- descricao  
- severidade  
- selector  
- trecho_html  
- recomendacao  

3.5 CLASSE WEBHOOK
--------------------------------------------------------------------------------
- id  
- cliente_id  
- url_callback  
- ativo  
- ultimo_envio  

================================================================================