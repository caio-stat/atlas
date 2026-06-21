# Trilhas de dependências

> Catálogo modular de dependências Python para instalar apenas a capacidade exigida pelo trabalho atual.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Documentação](../docs/README.pt-BR.md) · [Trilhas técnicas](../docs/tracks/README.pt-BR.md)

## Objetivo

Esta pasta separa dependências por domínio para manter ambientes menores, reduzir conflitos e tornar explícita a intenção de cada experimento. Os arquivos não afirmam que toda biblioteca esteja em uso; eles definem conjuntos candidatos para módulos e laboratórios específicos.

O ambiente executável atual do backend usa o arquivo fixado [`backend/requirements.txt`](../backend/requirements.txt). As trilhas desta pasta são conjuntos exploratórios sem pinagem global e não substituem um lock file de aplicação.

## Princípios

- Instale somente as trilhas necessárias para a tarefa.
- Use ambientes virtuais separados para stacks experimentais incompatíveis.
- Mantenha uma dependência na menor trilha coerente com seu uso.
- Aceite repetição entre trilhas; elimine repetição dentro do mesmo arquivo.
- Não liste módulos da biblioteca padrão do Python.
- Use `-r` apenas para composições intencionais e documentadas.
- Fixe versões no ambiente da aplicação ou lock file, não por reflexo em todas as trilhas.

## Instalação

Crie e ative um ambiente virtual antes de instalar. Execute os comandos a partir da raiz do repositório.

```bash
python -m venv .venv
# Activate the environment for your shell
python -m pip install --upgrade pip
python -m pip install -r requirements/core.txt
```

Várias trilhas podem ser combinadas explicitamente:

```bash
python -m pip install \
  -r requirements/core.txt \
  -r requirements/data.txt \
  -r requirements/statistics.txt
```

## Perfis de exemplo

| Perfil | Arquivos sugeridos |
|---|---|
| Desenvolvimento backend | `core.txt`, `dev.txt`, `code_quality.txt`, `advanced_testing.txt` |
| Análise estatística | `data.txt`, `statistics.txt`, `visualization.txt`, `notebooks.txt` |
| Experimento de ML | `data.txt`, `statistics.txt`, `ml.txt`, `mlops.txt` |
| Protótipo RAG/agente | `document_intelligence.txt`, `generative_ai.txt`, `agents.txt` |
| Automação operacional | `scripting.txt`, `automation.txt`, `observability.txt` |
| Cloud local e entrega | `devops.txt`, `cloud_orchestration.txt`, `security.txt` |
| Experimento IoT | `iot.txt`, `hardware_protocols.txt`, `observability.txt` |

## Catálogo completo

### Fundamentos e desenvolvimento

Bibliotecas base, ferramentas de desenvolvimento, arquitetura, automação e manutenibilidade.

| Arquivo | Uso principal |
|---|---|
| [`core.txt`](core.txt) | Base tabular e analítica usada por pequenos fluxos de dados. |
| [`dev.txt`](dev.txt) | Testes, formatação, tipagem, hooks e apoio ao desenvolvimento local. |
| [`support.txt`](support.txt) | Diagnóstico de máquinas, inventário, integração Windows e CLIs de suporte. |
| [`scripting.txt`](scripting.txt) | Construção de CLIs, automação de tarefas, relatórios, HTTP e logging. |
| [`automation.txt`](automation.txt) | Agendadores, ferramentas de workflow, workers e automação de arquivos. |
| [`oop.txt`](oop.txt) | Modelos de dados, tipagem, serialização e experimentos de injeção de dependência. |
| [`software_design.txt`](software_design.txt) | Injeção de dependência, plugins, máquinas de estado, validação e apoio arquitetural. |
| [`plugins.txt`](plugins.txt) | Descoberta de plugins, configuração, validação e mecanismos de extensão. |
| [`refactoring.txt`](refactoring.txt) | Ferramentas AST, formatadores, tipagem, código morto e complexidade. |
| [`code_quality.txt`](code_quality.txt) | Linting, tipagem estática, segurança, qualidade documental e hooks. |

### Dados e analytics

Trabalho tabular, estatística, análise numérica, relatórios e processamento em escala.

| Arquivo | Uso principal |
|---|---|
| [`data.txt`](data.txt) | Trabalho geral com dataframes, Arrow, DuckDB e planilhas. |
| [`data_engineering.txt`](data_engineering.txt) | Acesso SQL, modelos ORM, migrações e conectores analíticos. |
| [`big_data.txt`](big_data.txt) | Processamento distribuído e out-of-core com Spark, Dask, Ray e Modin. |
| [`statistics.txt`](statistics.txt) | Estatística científica, regressão, testes e apoio simbólico. |
| [`bayesian.txt`](bayesian.txt) | Modelagem bayesiana, inferência e diagnósticos posteriores. |
| [`optimization.txt`](optimization.txt) | Pesquisa operacional e modelos de otimização matemática. |
| [`simulation.txt`](simulation.txt) | Simulação de eventos discretos e processos. |
| [`time_series.txt`](time_series.txt) | Frameworks de previsão e experimentos com modelos temporais. |
| [`anomaly_detection.txt`](anomaly_detection.txt) | Análise de outliers, drift, change points, streaming e monitoramento. |
| [`visualization.txt`](visualization.txt) | Visualização estática, interativa, declarativa e word clouds. |
| [`notebooks.txt`](notebooks.txt) | Autoria Jupyter, execução, conversão, versionamento, relatórios e cache. |
| [`bi.txt`](bi.txt) | Acesso a dados, dashboards, profiling, Excel, relatórios e BI geoespacial. |
| [`powerbi.txt`](powerbi.txt) | Power BI, Fabric, autenticação Microsoft, dados tabulares e notebooks. |
| [`geospatial.txt`](geospatial.txt) | Análise vetorial, raster, mapas, geocodificação e redes viárias. |
| [`game_data.txt`](game_data.txt) | Análise estatística e visual de telemetria de jogos. |

### Inteligência artificial e machine learning

Modelos clássicos e neurais, linguagem, visão, agentes, políticas e operações de modelos.

| Arquivo | Uso principal |
|---|---|
| [`ai.txt`](ai.txt) | Agregador sem dependências que direciona para trilhas específicas de IA. |
| [`ml.txt`](ml.txt) | ML clássico, boosting, desbalanceamento, features e tuning. |
| [`deep_learning.txt`](deep_learning.txt) | TensorFlow, Keras, PyTorch, Lightning e dashboards de experimentos. |
| [`mlops.txt`](mlops.txt) | Rastreamento de experimentos, monitoramento de modelos e validação de dados. |
| [`nlp.txt`](nlp.txt) | Processamento textual, embeddings, Transformers, datasets e tokenização. |
| [`computer_vision.txt`](computer_vision.txt) | Processamento de imagem, augmentation, detecção e apoio a OCR. |
| [`document_intelligence.txt`](document_intelligence.txt) | Parsing de documentos, extração de PDF e compreensão de layout. |
| [`ocr.txt`](ocr.txt) | Engines Tesseract e OCR neural. |
| [`generative_ai.txt`](generative_ai.txt) | Provedores LLM, orquestração, bancos vetoriais e modelos locais. |
| [`agents.txt`](agents.txt) | Frameworks de agentes e desenvolvimento de agentes tipados. |
| [`autonomous_systems.txt`](autonomous_systems.txt) | Workflows de agentes, máquinas de estado, agendamento, APIs e validação. |
| [`policy_agents.txt`](policy_agents.txt) | Instalação composta de agentes, motor de políticas e sistemas de decisão. |
| [`policy_engine.txt`](policy_engine.txt) | Motores de regras, lógica JSON, validação, configuração e apoio a auditoria. |
| [`decision_system.txt`](decision_system.txt) | Modelos de decisão, otimização, estado, RL, dados e visualização. |
| [`mobile_ai.txt`](mobile_ai.txt) | ONNX, TensorFlow Lite, visão e inferência mobile leve. |
| [`games_ai.txt`](games_ai.txt) | Reinforcement learning, ambientes multiagentes, pathfinding e evolução. |

### Cloud, distribuição e operações

Provedores de infraestrutura, automação de entrega, redes, mensageria, confiabilidade e segurança.

| Arquivo | Uso principal |
|---|---|
| [`cloud.txt`](cloud.txt) | Conjunto mínimo de SDKs multi-cloud para storage, analytics e identidade. |
| [`aws.txt`](aws.txt) | SDK AWS, CLI, IaC, testes, deploy, segurança e observabilidade. |
| [`cloud_orchestration.txt`](cloud_orchestration.txt) | AWS, GCP, Azure, Pulumi, Terraform, Ansible, Docker e Kubernetes. |
| [`devops.txt`](devops.txt) | Automação remota, gestão de configuração, containers e APIs de forges. |
| [`networking.txt`](networking.txt) | Diagnóstico HTTP, DNS, interfaces, pacotes, SSH e velocidade. |
| [`messaging.txt`](messaging.txt) | Clientes RabbitMQ, workers Redis, Kafka e NATS. |
| [`distributed_system.txt`](distributed_system.txt) | Experimentos com Kafka, NATS e processamento de eventos. |
| [`observability.txt`](observability.txt) | Logs estruturados, métricas, tracing e relato de erros. |
| [`resilience.txt`](resilience.txt) | Retry, circuit breakers, rate limits, saúde, filas e testes de resiliência. |
| [`zero_downtime.txt`](zero_downtime.txt) | Serving, controle de processos, containers, migrações, flags e operação remota. |
| [`self_healing.txt`](self_healing.txt) | Agregador sem dependências para resiliência, observabilidade, automação e autonomia. |
| [`security.txt`](security.txt) | Criptografia, JWT, hashing de senhas e primitivas seguras de credenciais. |

### Concorrência e tempo real

Execução assíncrona, paralelismo, streams, dashboards ao vivo e integração sensível ao tempo.

| Arquivo | Uso principal |
|---|---|
| [`async_programming.txt`](async_programming.txt) | Runtimes async, HTTP, WebSockets, arquivos, bancos, mensageria e APIs. |
| [`concurrency.txt`](concurrency.txt) | IO assíncrono, eventos, workers, agendamento, profiling e testes. |
| [`parallel_computing.txt`](parallel_computing.txt) | Paralelismo de processos, execução distribuída, aceleração e benchmarks. |
| [`real_time.txt`](real_time.txt) | WebSockets, SSE, pub/sub, brokers, bancos assíncronos e serialização. |
| [`realtime_programming.txt`](realtime_programming.txt) | Código orientado a eventos, dispositivos, protocolos industriais, controle e simulação. |
| [`hard_realtime_integration.txt`](hard_realtime_integration.txt) | Bindings nativos, RPC, mensageria, dados binários e monitoramento de runtime. |
| [`real_time_dashboard.txt`](real_time_dashboard.txt) | Dataframes ao vivo, gráficos, dashboards, APIs e métricas. |

### Hardware, edge e indústria

Software de dispositivos, protocolos, telemetria, controle, sistemas industriais e robótica.

| Arquivo | Uso principal |
|---|---|
| [`embedded.txt`](embedded.txt) | Serial, IoT, Modbus, BLE, CAN, dados e utilitários de dispositivos. |
| [`embedded_linux.txt`](embedded_linux.txt) | Monitoramento, GPIO, redes, mensageria, APIs, dados e logs na borda. |
| [`micropython.txt`](micropython.txt) | Deploy MicroPython, comunicação serial e apoio por linha de comando. |
| [`fpga.txt`](fpga.txt) | Testes HDL, descrição de hardware, simulação, dados binários e gráficos. |
| [`hardware_protocols.txt`](hardware_protocols.txt) | Serial, Modbus, CAN, MQTT, BLE, OPC-UA, parsing binário e redes. |
| [`iot.txt`](iot.txt) | Clientes focados em MQTT, serial, Modbus, BLE e OPC-UA. |
| [`industrial.txt`](industrial.txt) | Protocolos industriais, redes, mensageria, dados e monitoramento. |
| [`robotics.txt`](robotics.txt) | Matemática, controle, simulação, barramentos, visão e visualização. |
| [`control_system.txt`](control_system.txt) | Controle numérico, PID, simulação e gráficos. |

### Aplicações e testes

Coleta web, aplicações mobile, jogos e testes de maior garantia.

| Arquivo | Uso principal |
|---|---|
| [`scraping.txt`](scraping.txt) | Coleta HTTP e por navegador, parsing HTML, crawling e extração de PDF. |
| [`mobile.txt`](mobile.txt) | Protótipos mobile em Python, APIs de dispositivo, rede, QR e imagens. |
| [`mobile_testing.txt`](mobile_testing.txt) | Appium, ADB, automação de UI, pytest, relatórios e checagens de API. |
| [`games.txt`](games.txt) | Frameworks 2D/3D, física, matemática, assets, áudio e ferramentas CLI. |
| [`games_engines.txt`](games_engines.txt) | Parsing Godot, assets glTF, meshes, OpenGL e janelas. |
| [`advanced_testing.txt`](advanced_testing.txt) | Ecossistema pytest, properties, mutação, fixtures, tempo, mocks HTTP e relatórios. |
| [`safety_testing.txt`](safety_testing.txt) | Testes, análise estática, validação, relatórios e apoio a injeção de falhas. |

## Composições e arquivos agregadores

`policy_agents.txt` é uma composição instalável e inclui `agents.txt`, `policy_engine.txt` e `decision_system.txt` por diretivas `-r`. Caminhos incluídos são relativos a esta pasta.

`ai.txt` e `self_healing.txt` são guias agregadores intencionalmente sem pacotes. Eles apontam para combinações possíveis, mas não impõem uma instalação extensa.

## Como adicionar ou alterar uma trilha

1. Confirme que a biblioteca existe no índice de pacotes e suporta a versão de Python adotada.
2. Escolha o arquivo mais específico; crie outro somente quando houver fronteira técnica clara.
3. Adicione um comentário de seção quando a lista tiver grupos conceituais.
4. Evite pacotes alternativos redundantes sem documentar o motivo.
5. Verifique duplicatas, espaços finais, nomes antigos e includes quebrados.
6. Atualize este catálogo e o README da trilha técnica relacionada.
7. Teste a instalação em um ambiente limpo antes de usá-la em um módulo.

## Validação recomendada

```text
- todos os arquivos usam snake_case e extensão .txt
- não há entrada duplicada dentro de um arquivo
- cada diretiva -r aponta para um arquivo existente
- não há módulos da biblioteca padrão
- o catálogo contém todas as trilhas
- o módulo consumidor declara quais trilhas instala
```

## Limitações

- As listas não são lock files e podem resolver versões diferentes ao longo do tempo.
- Algumas stacks possuem dependências nativas, requisitos de sistema operacional ou conflitos entre frameworks.
- Bibliotecas cloud, IA e automação podem exigir contas, credenciais ou custos externos.
- A presença de uma biblioteca na trilha não autoriza coleta de dados, acesso a dispositivos ou mutações externas.
