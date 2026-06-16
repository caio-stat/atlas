# Atlas

<p align="center">
  <strong>Um laboratório modular de Dados, IA, Estatística, Automação, Infraestrutura e Engenharia de Software.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Banco%20de%20Dados-336791" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-Containers-2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/Status-Fundação%20Inicial-yellow" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Licença-MIT-green" alt="Licença">
</p>

<p align="center">
  🌎 Idioma: <a href="README.md">English</a> | Português
</p>

---

## Visão Geral

**Atlas** é um portfólio técnico de longo prazo e um laboratório de aprendizado criado para evoluir como um ecossistema modular de:

* engenharia de software
* engenharia de dados
* estatística
* machine learning
* deep learning
* IA generativa
* automação
* ferramentas de suporte técnico
* redes
* computação em nuvem
* sistemas distribuídos
* aplicações web e mobile

O objetivo não é construir tutoriais isolados ou scripts desconectados. O Atlas está sendo desenvolvido como um ecossistema real, incremental e documentado, onde cada módulo demonstra uma competência profissional por meio de código, testes, decisões de arquitetura e casos de uso práticos.

O Atlas começa como um **monólito modular** e pode evoluir para serviços distribuídos apenas quando houver uma justificativa técnica clara.

---

## Status Atual

O Atlas está em sua **fase inicial de fundação**.

O repositório atualmente contém a base inicial do projeto e uma pasta `requirements/` em crescimento, que mapeia as principais trilhas de estudo e experimentação técnica.

Foco atual:

* manter o repositório organizado e compreensível
* documentar a visão arquitetural de longo prazo
* construir a fundação do backend de forma incremental
* evitar overengineering cedo demais
* separar dependências por domínio técnico
* transformar estudos em módulos com valor de portfólio

Próximo marco imediato:

```text
Atlas Core + Health API
```

Esse primeiro marco deve incluir:

* estrutura inicial com FastAPI
* endpoint `/health`
* endpoint `/version`
* conexão com PostgreSQL
* organização modular básica
* primeira entidade de domínio
* primeiro caso de uso
* testes iniciais com `pytest`
* primeiro Architecture Decision Record, ou ADR

---

## Objetivos do Projeto

O Atlas tem como objetivo integrar e demonstrar conhecimento em:

* desenvolvimento backend com Python
* programação orientada a objetos em Python
* FastAPI e desenho de APIs REST
* PostgreSQL e SQL
* coleta de dados, web scraping e ETL
* OCR e inteligência documental
* engenharia de dados e pipelines analíticos
* estatística, probabilidade, inferência, regressão e modelagem Bayesiana
* métodos numéricos, otimização e simulação
* machine learning e rastreamento de experimentos
* deep learning com redes neurais, embeddings, visão computacional, NLP e Transformers
* IA generativa, RAG e agentes inteligentes
* automação de fluxos com ferramentas como n8n
* automação de suporte/helpdesk e scripts de diagnóstico
* redes, sockets e diagnóstico de infraestrutura
* mensageria, filas e processamento assíncrono
* cloud computing, DevOps e observabilidade
* análise geoespacial, dados epidemiológicos e bases públicas
* dashboards, visualização de dados e storytelling
* desenvolvimento Android com Kotlin e aplicações offline-first
* Linux, segurança, concorrência e sistemas distribuídos
* arquitetura de software, DDD, TDD e Design Patterns

---

## Filosofia Arquitetural

O Atlas segue uma estratégia arquitetural pragmática:

1. **Começar simples**, com um monólito modular.
2. **Manter fronteiras claras** entre domínio, aplicação, infraestrutura e interfaces.
3. **Usar DDD de forma pragmática**, sem transformar o projeto em cerimônia abstrata.
4. **Aplicar TDD quando isso trouxer clareza e segurança**.
5. **Documentar decisões relevantes** por meio de ADRs.
6. **Separar módulos em serviços apenas no futuro**, quando houver necessidade real de escala, deploy independente ou isolamento tecnológico.
7. **Instalar dependências por trilha**, e não tudo de uma vez.

A direção arquitetural inicial é inspirada por:

* Monólito Modular
* Clean Architecture
* Arquitetura Hexagonal
* Domain-Driven Design
* Test-Driven Development
* Arquitetura orientada a eventos, quando fizer sentido
* Arquitetura orientada a dados, quando fizer sentido

---

## Estrutura Geral Planejada

O repositório pode evoluir para uma organização parecida com esta:

```text
atlas/
├── apps/
│   ├── web/                         # Dashboards React e interface do portfólio
│   ├── mobile/                      # App Android Kotlin, offline-first
│   └── desktop/                     # Experimentos futuros com desktop
│
├── services/
│   ├── atlas_api/                   # Aplicação principal FastAPI
│   ├── atlas_worker/                # Workers e tarefas em segundo plano
│   ├── atlas_ai/                    # RAG, agentes e integrações com LLMs
│   ├── atlas_scraper/               # Web scraping e coleta de dados
│   ├── atlas_stats/                 # Estatística, probabilidade e regressão
│   ├── atlas_support/               # Diagnósticos de suporte/helpdesk
│   ├── atlas_networking/            # Experimentos e diagnósticos de rede
│   └── atlas_automation/            # n8n, WhatsApp, relatórios e workflows
│
├── packages/
│   ├── atlas_core/                  # Entidades, objetos de valor e casos de uso
│   ├── atlas_shared/                # Schemas, DTOs e utilitários compartilhados
│   └── atlas_plugins/               # Provedores e integrações plugáveis
│
├── requirements/
│   ├── core.txt
│   ├── dev.txt
│   ├── data.txt
│   ├── statistics.txt
│   ├── ml.txt
│   ├── deep_learning.txt
│   ├── generative_ai.txt
│   ├── scraping.txt
│   ├── ocr.txt
│   ├── document_intelligence.txt
│   ├── support.txt
│   ├── networking.txt
│   ├── cloud.txt
│   ├── messaging.txt
│   └── ...
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── warehouse/
│   └── samples/
│
├── notebooks/
│   ├── statistics/
│   ├── machine_learning/
│   ├── deep_learning/
│   ├── calculus/
│   └── experiments/
│
├── infra/
│   ├── docker/
│   ├── postgres/
│   ├── monitoring/
│   └── github_actions/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── roadmap/
│   ├── modules/
│   └── portfolio/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── load/
│
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

Essa estrutura representa uma direção planejada, não uma promessa de que todos os diretórios já existem hoje.

---

## Trilhas de Requirements

A pasta `requirements/` é organizada por domínio técnico. Isso evita instalar um ambiente gigante e frágil antes de cada módulo realmente precisar daquelas dependências.

| Arquivo                                  | Finalidade                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------- |
| `requirements/core.txt`                  | Ferramentas centrais para arrays, dataframes, tabelas e armazenamento analítico local |
| `requirements/dev.txt`                   | Ferramentas de desenvolvimento, formatação, lint, testes e qualidade local            |
| `requirements/data.txt`                  | Análise e manipulação geral de dados                                                  |
| `requirements/visualization.txt`         | Gráficos, dashboards e storytelling                                                   |
| `requirements/statistics.txt`            | Estatística descritiva, inferência e modelagem estatística                            |
| `requirements/bayesian.txt`              | Modelagem Bayesiana e programação probabilística                                      |
| `requirements/ml.txt`                    | Machine learning clássico                                                             |
| `requirements/deep_learning.txt`         | Redes neurais e frameworks de deep learning                                           |
| `requirements/nlp.txt`                   | Processamento de linguagem natural                                                    |
| `requirements/computer_vision.txt`       | Processamento de imagens e visão computacional                                        |
| `requirements/generative_ai.txt`         | LLMs, embeddings e fluxos de IA generativa                                            |
| `requirements/ai.txt`                    | Utilitários gerais de IA e integrações                                                |
| `requirements/agents.txt`                | Workflows agentivos e experimentos multiagentes                                       |
| `requirements/scraping.txt`              | Web scraping, crawling e automação de navegador                                       |
| `requirements/ocr.txt`                   | OCR para imagens e documentos escaneados                                              |
| `requirements/document_intelligence.txt` | Parsing de PDF, layout documental e extração estruturada                              |
| `requirements/data_engineering.txt`      | SQL, ORM, migrations e pipelines de dados                                             |
| `requirements/big_data.txt`              | Big Data e experimentos com processamento distribuído                                 |
| `requirements/mlops.txt`                 | Rastreamento, deploy e ciclo de vida de modelos                                       |
| `requirements/time_series.txt`           | Séries temporais e previsão                                                           |
| `requirements/geospatial.txt`            | Mapas, dados geoespaciais e inteligência territorial                                  |
| `requirements/optimization.txt`          | Pesquisa operacional e otimização matemática                                          |
| `requirements/simulation.txt`            | Simulação de eventos discretos e experimentos estocásticos                            |
| `requirements/automation.txt`            | Automação de workflows e orquestração de tarefas                                      |
| `requirements/support.txt`               | Automação de suporte/helpdesk e diagnóstico de máquinas                               |
| `requirements/networking.txt`            | Diagnóstico de rede, DNS, SSH, sockets e varredura                                    |
| `requirements/cloud.txt`                 | Experimentos com SDKs da AWS, Google Cloud e Azure                                    |
| `requirements/devops.txt`                | Automação de infraestrutura e ferramentas de deploy                                   |
| `requirements/observability.txt`         | Logs, métricas, traces e monitoramento                                                |
| `requirements/messaging.txt`             | Filas, workers e processamento assíncrono                                             |
| `requirements/distributed_system.txt`    | Experimentos com sistemas distribuídos e coordenação de serviços                      |
| `requirements/iot.txt`                   | IoT e comunicação com hardware                                                        |
| `requirements/security.txt`              | Criptografia, autenticação e utilitários de segurança                                 |

Uso recomendado:

```bash
# Comece pela trilha mínima/base
pip install -r requirements/core.txt
pip install -r requirements/dev.txt

# Adicione apenas a trilha que estiver estudando no momento
pip install -r requirements/statistics.txt
pip install -r requirements/scraping.txt
pip install -r requirements/support.txt
```

Algumas trilhas podem exigir dependências externas do sistema operacional. Por exemplo, OCR, automação de navegador, bibliotecas geoespaciais e frameworks de deep learning podem exigir pacotes do sistema, drivers ou download de modelos.

---

## Módulos Principais

### Atlas Core

A fundação de domínio do sistema.

Responsabilidades planejadas:

* entidades
* objetos de valor
* casos de uso
* interfaces de repositório
* eventos de domínio
* regras de negócio
* lógica pura em Python

Exemplos de entidades futuras:

* `DataSource`
* `Dataset`
* `Pipeline`
* `PipelineRun`
* `Experiment`
* `ModelRun`
* `StatisticalTest`
* `Agent`
* `Workflow`
* `Report`
* `SupportCheck`
* `NetworkProbe`

---

### Atlas API

A camada HTTP do projeto.

Responsabilidades planejadas:

* rotas FastAPI
* schemas de requisição e resposta
* injeção de dependências
* experimentos com autenticação
* documentação automática da API
* integração com casos de uso do domínio

Endpoints iniciais:

```text
GET /health
GET /version
```

---

### Atlas Data Mining

Responsável por coleta de dados e inteligência web.

Essa área inclui:

* **Atlas Web Scraping Lab**
* **Atlas OCR Lab**
* **Atlas Document Intelligence Lab**

Tópicos planejados:

* coleta de dados via APIs
* parsing de HTML
* scraping assíncrono
* automação de navegador
* práticas responsáveis de scraping
* OCR para documentos escaneados
* extração de PDFs e análise de layout
* chunking de documentos para RAG
* coleta de dados públicos

Casos de uso possíveis:

* monitoramento de concursos públicos e editais
* bases governamentais
* DATASUS e dados de saúde pública
* informações acadêmicas da UFBA
* relatórios públicos, decretos, portarias, editais e PDFs
* radar de tendências tecnológicas

---

### Atlas ETL e Engenharia de Dados

Responsável por transformar dados brutos em dados utilizáveis.

Tópicos planejados:

* extração
* limpeza
* validação
* transformação
* carga no PostgreSQL
* verificações de qualidade de dados
* cargas incrementais
* logs de pipeline
* experimentos com versionamento de dados
* armazenamento analítico com DuckDB
* ORM e migrations com SQLAlchemy, SQLModel e Alembic

Fluxo geral:

```text
Fonte Externa
    ↓
Extractor
    ↓
Dado Bruto
    ↓
Validator
    ↓
Transformer
    ↓
PostgreSQL / DuckDB
    ↓
Analytics / ML / RAG
    ↓
API / Dashboard / Relatório
```

---

### Atlas Statistical Lab

Módulo focado em conectar estatística acadêmica com software real.

Tópicos planejados:

* estatística descritiva
* distribuições de probabilidade
* amostragem
* simulação Monte Carlo
* bootstrap
* intervalos de confiança
* testes de hipótese
* regressão linear
* diagnóstico de regressão
* modelagem Bayesiana
* experimentos com séries temporais
* métodos numéricos
* fundamentos de cálculo aplicados à otimização

A ideia é implementar conceitos estatísticos em Python antes de esconder tudo atrás de bibliotecas de alto nível.

---

### Atlas Machine Learning Lab

Módulo para machine learning clássico e experimentação supervisionada/não supervisionada.

Tópicos planejados:

* regressão linear
* regressão logística
* KNN
* árvores de decisão
* Random Forest
* Gradient Boosting
* clustering
* PCA
* validação cruzada
* métricas de avaliação
* engenharia de atributos
* experimentos reprodutíveis
* comparação entre implementações manuais e modelos de bibliotecas consolidadas

---

### Atlas Deep Learning Lab

Módulo dedicado ao estudo e implementação de redes neurais profundas, conectando fundamentos matemáticos, estatística, otimização e aplicações modernas de IA.

Tópicos planejados:

* redes neurais artificiais do zero
* perceptron e multilayer perceptron, ou MLP
* funções de ativação
* funções de perda
* gradiente descendente
* backpropagation
* regularização
* dropout
* batch normalization
* otimizadores como SGD, RMSProp e Adam
* Convolutional Neural Networks, ou CNNs
* Recurrent Neural Networks, LSTM e GRU
* autoencoders
* embeddings
* modelos de NLP
* mecanismo de atenção
* Transformers
* fine-tuning de modelos pré-treinados
* experimentos com PyTorch
* experimentos com TensorFlow e Keras

Esse módulo deve evitar tratar redes neurais como caixas-pretas. A ideia é primeiro estudar os fundamentos, implementar versões simples e só depois usar frameworks modernos com mais consciência técnica.

---

### Atlas AI Lab

Módulo para IA generativa, RAG e sistemas baseados em agentes.

Tópicos planejados:

* integrações com LLMs
* Ollama para modelos locais
* Replicate e modelos em nuvem
* embeddings
* busca vetorial
* pipelines RAG
* agentes de IA
* workflows multiagentes
* avaliação de prompts
* guardrails
* tool calling
* experimentos com memória
* estratégias de fallback entre modelos

Fluxo futuro possível:

```text
Usuário
 ↓
Chat / API / WhatsApp
 ↓
Agent Router
 ↓
Retriever
 ↓
Tool Executor
 ↓
LLM Provider
 ↓
Response Validator
 ↓
Resposta + Logs + Métricas
```

---

### Atlas Automation Lab

Módulo para automação de workflows e integrações externas.

Tópicos planejados:

* workflows com n8n
* tarefas agendadas
* workflows orientados a eventos
* alertas por e-mail
* integração com WhatsApp
* automação de social media
* relatórios automáticos
* automação de portfólio
* automações acadêmicas

Fluxo de exemplo:

```text
Novo dado coletado
    ↓
Pipeline processa o dado
    ↓
IA resume os achados
    ↓
Módulo estatístico valida padrões
    ↓
Dashboard é atualizado
    ↓
Automação envia relatório ou alerta
```

---

### Atlas Support Lab

Módulo inspirado em trabalho real de suporte/helpdesk.

Tópicos planejados:

* diagnóstico de máquinas
* relatórios de CPU, RAM e disco
* inspeção de processos e serviços
* experimentos de automação Windows
* inventário via WMI
* relatórios de suporte em Markdown ou HTML
* scripts portáteis de diagnóstico
* health checks para estações de trabalho

Casos de uso possíveis:

* gerar relatório diagnóstico local da máquina
* verificar CPU, RAM, disco e informações de rede
* criar checklist de suporte para máquinas Windows
* coletar dados básicos de inventário para troubleshooting

---

### Atlas Networking Lab

Módulo para diagnóstico de rede e experimentos de infraestrutura.

Tópicos planejados:

* testes de ping e latência
* resolução DNS
* inspeção de interfaces de rede
* automação SSH
* varredura de rede local
* sockets
* experimentos TCP e UDP
* teste de banda
* health checks de APIs e endpoints

Casos de uso possíveis:

* testar DNS, gateway e conectividade com a internet
* diagnosticar latência e perda de pacotes
* escanear hosts alcançáveis em uma rede local
* monitorar endpoints internos

---

### Atlas Messaging Lab

Módulo para filas, workers e processamento assíncrono.

Tópicos planejados:

* filas com Redis
* experimentos com RabbitMQ
* workers com Celery
* jobs em segundo plano
* políticas de retry
* workflows orientados a eventos
* processamento assíncrono de tarefas

Casos de uso possíveis:

* processar jobs de scraping em segundo plano
* enfileirar tarefas de extração documental
* enviar geração de relatórios para workers
* conectar eventos de automação a pipelines

---

### Atlas Cloud, DevOps e Observability

A fundação operacional do projeto.

Tópicos planejados:

* Docker
* Docker Compose
* PostgreSQL
* experimentos com Redis
* GitHub Actions
* deploy em cloud
* experimentos com SDKs da AWS, Google Cloud e Azure
* automação de infraestrutura
* logs
* métricas
* traces
* health checks
* monitoramento
* backups
* experimentos com deploy zero-downtime

---

### Atlas Systems Lab

Módulo para conhecimento de mais baixo nível em sistemas.

Tópicos planejados:

* fundamentos de Linux
* processos e threads
* programação assíncrona
* sockets
* experimentos TCP/UDP
* comunicação P2P
* sistemas distribuídos
* fundamentos de criptografia
* problemas de concorrência
* tolerância a falhas
* testes de carga
* experimentos com IoT

---

### Atlas Web

Futura interface React para dashboards, storytelling e apresentação de portfólio.

Funcionalidades planejadas:

* landing page
* mapa interativo do projeto
* dashboards de dados
* visualizações estatísticas
* monitoramento de pipelines
* histórico de experimentos
* playground de RAG
* dashboard de diagnósticos de suporte
* interface gamificada de aprendizado

---

### Atlas Mobile

Futura aplicação Android construída com Kotlin.

Funcionalidades planejadas:

* acesso offline-first
* cache local com Room/SQLite
* sincronização com API
* notificações
* dashboards simplificados
* acesso a chatbot
* experimentos de coleta mobile de dados
* acesso a checklist de suporte
* experimentos de diagnóstico em campo

---

### Atlas Legacy Lab

Módulo futuro para praticar manutenção e modernização de sistemas legados.

Tópicos planejados:

* scripts legados bagunçados
* testes de caracterização
* refatoração
* adapters
* Strangler Fig Pattern
* documentação de dívida técnica

Esse módulo existe porque software real raramente chega limpo, documentado e emocionalmente disponível.

---

## Stack Tecnológica

### Atual / Inicial

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ou SQLModel
* Pydantic
* Docker
* Docker Compose
* pytest
* Git e GitHub

### Planejada / Experimental

* NumPy
* Pandas
* Polars
* PyArrow
* DuckDB
* OpenPyXL
* scikit-learn
* statsmodels
* PyMC
* PyTorch
* TensorFlow / Keras
* ecossistema Hugging Face
* LangChain / LangGraph
* Flowise
* Ollama
* Replicate
* ChromaDB, Qdrant, FAISS ou PGVector
* BeautifulSoup, Scrapy, Playwright e Selenium
* PyMuPDF, pdfplumber, Unstructured e LayoutParser
* pytesseract e EasyOCR
* experimentos com Redis, Celery e RabbitMQ
* psutil, WMI e ferramentas de automação de suporte
* ferramentas de rede como dnspython, scapy, paramiko e utilitários de ping
* boto3, SDKs do Google Cloud e SDKs do Azure
* Grafana, Prometheus e OpenTelemetry
* React e TypeScript
* Kotlin Android e Room / SQLite
* n8n

---

## Roadmap

### Fase 0: Fundação

* [ ] Organizar a estrutura do backend
* [ ] Criar endpoint `/health`
* [ ] Criar endpoint `/version`
* [ ] Conectar FastAPI ao PostgreSQL
* [ ] Adicionar testes básicos
* [ ] Adicionar documentação inicial
* [ ] Criar o primeiro ADR

### Fase 1: Atlas Core

* [ ] Criar entidades de domínio
* [ ] Criar casos de uso
* [ ] Criar interfaces de repositório
* [ ] Adicionar testes unitários
* [ ] Documentar decisões de domínio

### Fase 2: Data Mining, Scraping e ETL

* [ ] Criar a primeira fonte de dados
* [ ] Construir o primeiro scraper
* [ ] Armazenar dados brutos
* [ ] Validar dados coletados
* [ ] Transformar e carregar dados no PostgreSQL
* [ ] Expor dados pela API

### Fase 3: OCR e Document Intelligence

* [ ] Extrair texto de PDFs
* [ ] Extrair texto de imagens escaneadas
* [ ] Estruturar seções de documentos
* [ ] Preparar chunks para RAG
* [ ] Construir um pequeno protótipo de perguntas e respostas sobre documentos

### Fase 4: Statistical Lab

* [ ] Adicionar módulo de estatística descritiva
* [ ] Adicionar simulações de probabilidade
* [ ] Adicionar experimentos de amostragem
* [ ] Adicionar exemplos de intervalo de confiança
* [ ] Adicionar exemplos de testes de hipótese
* [ ] Adicionar experimentos de regressão
* [ ] Adicionar experimentos de modelagem Bayesiana

### Fase 5: Machine Learning

* [ ] Adicionar experimentos iniciais de ML
* [ ] Adicionar métricas de avaliação de modelos
* [ ] Adicionar rastreamento simples e reprodutível de experimentos
* [ ] Comparar implementações manuais com modelos baseados em bibliotecas

### Fase 6: Deep Learning

* [ ] Implementar uma rede neural simples do zero
* [ ] Implementar gradiente descendente e backpropagation em exemplo didático
* [ ] Criar experimento de MLP com PyTorch
* [ ] Criar experimento de classificação de texto
* [ ] Criar experimento inicial com embeddings
* [ ] Comparar um modelo clássico com uma rede neural no mesmo problema

### Fase 7: IA, RAG e Agentes

* [ ] Adicionar embeddings
* [ ] Criar um protótipo de RAG
* [ ] Integrar um modelo local com Ollama
* [ ] Adicionar ferramentas baseadas em agentes
* [ ] Adicionar avaliação de respostas e logging

### Fase 8: Suporte e Redes

* [ ] Criar script de diagnóstico de máquina
* [ ] Gerar relatório de suporte em Markdown ou HTML
* [ ] Adicionar verificações de DNS e latência
* [ ] Adicionar health checks de endpoints
* [ ] Adicionar experimentos simples de inventário de rede

### Fase 9: Automação e Mensageria

* [ ] Adicionar workflows com n8n
* [ ] Adicionar alertas
* [ ] Automatizar relatórios
* [ ] Adicionar experimento com fila/worker
* [ ] Criar experimentos de integração com WhatsApp ou e-mail

### Fase 10: Web, Storytelling e Portfólio

* [ ] Construir dashboard React
* [ ] Adicionar relatórios visuais
* [ ] Criar mapa visual do portfólio
* [ ] Adicionar visualizações estatísticas
* [ ] Adicionar dashboards de suporte/rede

### Fase 11: Cloud, DevOps e Observabilidade

* [ ] Adicionar pipeline de CI/CD
* [ ] Criar ambiente de deploy
* [ ] Adicionar logs estruturados
* [ ] Adicionar métricas e traces
* [ ] Adicionar monitoramento
* [ ] Adicionar testes de carga

### Fase 12: Sistemas, Segurança e Experimentos Distribuídos

* [ ] Adicionar experimentos com sockets
* [ ] Adicionar protótipos de sistemas distribuídos
* [ ] Adicionar exemplos de criptografia
* [ ] Adicionar experimentos com IoT
* [ ] Adicionar experimentos de caos/resiliência quando a fundação estiver madura

---

## Rodando Localmente

Esta seção será expandida conforme a fundação do projeto for implementada.

Fluxo futuro esperado:

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas

python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale apenas as trilhas necessárias para a tarefa atual:

```bash
pip install -r requirements/core.txt
pip install -r requirements/dev.txt
```

Exemplo para uma trilha específica de estudo:

```bash
pip install -r requirements/statistics.txt
```

Fluxo futuro com Docker:

```bash
docker compose up -d
```

Comando futuro do backend:

```bash
cd backend
uvicorn main:app --reload
```

Comando futuro de testes:

```bash
pytest
```

---

## Estratégia de Aprendizado

O Atlas foi projetado para crescer por ciclos pequenos e documentados.

Cada ciclo deve produzir:

* código funcionando
* testes
* documentação
* uma decisão arquitetural clara
* uma explicação adequada para portfólio
* conexão com dados, estatística, IA, infraestrutura ou engenharia de software

O projeto não deve tentar ficar completo de uma vez. Ele deve evoluir como software real: de forma incremental, com algum sofrimento inevitável e menos ilusões a cada semana.

---

## Valor para Portfólio

O Atlas tem como objetivo demonstrar a capacidade de:

* projetar sistemas modulares
* construir APIs
* trabalhar com bancos de dados
* coletar e processar dados
* aplicar estatística a problemas reais
* construir experimentos de machine learning
* estudar e implementar modelos de deep learning
* usar IA generativa de forma responsável
* automatizar workflows
* construir ferramentas de diagnóstico para suporte e redes
* organizar experimentos de cloud, DevOps e observabilidade
* documentar decisões técnicas
* pensar em escalabilidade, resiliência e manutenibilidade

---

## Licença

Este projeto está licenciado sob a Licença MIT.

---

## Autor

Desenvolvido por **Caio Costa Cavalcante** como portfólio técnico de longo prazo e laboratório de aprendizado em Dados, IA, Estatística, Automação, Infraestrutura e Engenharia de Software.
