# Atlas

<p align="center">
  <strong>Um laboratório modular de Dados, IA, Estatística e Engenharia de Software.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Banco%20de%20Dados-336791" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-Containers-2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/Status-Funda%C3%A7%C3%A3o%20Inicial-yellow" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green" alt="Licença">
</p>

<p align="center">
  🌎 Idioma: Português | <a href="README.md">Inglês</a>
</p>



---

## Visão Geral

**Atlas** é um projeto de portfólio técnico de longo prazo, criado para evoluir como um ecossistema modular voltado para engenharia de dados, computação estatística, machine learning, IA generativa, automação, desenvolvimento web/mobile e arquitetura de software.

A proposta do projeto não é ser uma coleção de tutoriais isolados, scripts soltos ou experimentos abandonados no GitHub, esse cemitério onde boas intenções vão tirar férias permanentes. O Atlas está sendo construído como um laboratório real de aprendizado, onde cada módulo demonstra uma competência profissional por meio de código, documentação, testes e casos de uso práticos.

O Atlas começa como um **monólito modular** e poderá evoluir para serviços distribuídos apenas quando houver uma justificativa técnica clara para isso.

---

## Objetivos do Projeto

O Atlas tem como objetivo integrar e demonstrar conhecimentos em:

- Desenvolvimento backend com Python
- Orientação a Objetos em Python
- FastAPI e desenho de APIs REST
- PostgreSQL e SQL
- Coleta de dados, web scraping e ETL
- Engenharia de dados e pipelines analíticos
- Estatística, probabilidade, inferência e regressão
- Machine learning e experimentação de modelos
- Deep Learning com redes neurais, embeddings, visão computacional, NLP e Transformers
- IA generativa, RAG e agentes inteligentes
- Automação de workflows com ferramentas como n8n
- Dashboards, visualização de dados e storytelling com React
- Desenvolvimento Android com Kotlin e aplicações offline-first
- Docker, CI/CD, cloud deployment e observabilidade
- Linux, redes, concorrência e sistemas distribuídos
- Arquitetura de software, DDD, TDD e Design Patterns

---

## Estado Atual

O Atlas está em sua **fase inicial de fundação**.

Estrutura atual do repositório:

```text
atlas/
├── backend/
├── docker-compose.yml
├── LICENSE
└── README.md
```

Foco atual:

- Estabelecer a base do backend
- Manter o repositório limpo e compreensível
- Documentar a visão arquitetural de longo prazo
- Evoluir de forma incremental, sem exagerar na arquitetura antes da hora

Próximo marco imediato:

```text
Atlas Core + Health API
```

Esse primeiro marco deve incluir:

- Estrutura inicial com FastAPI
- Endpoint `/health`
- Endpoint `/version`
- Conexão com PostgreSQL
- Organização modular básica
- Primeira entidade de domínio
- Primeiro caso de uso
- Testes iniciais com pytest
- Primeiro registro de decisão arquitetural, ou ADR

---

## Filosofia Arquitetural

O Atlas segue uma estratégia arquitetural pragmática:

1. **Começar simples**, com um monólito modular.
2. **Manter fronteiras claras** entre domínio, aplicação, infraestrutura e interfaces.
3. **Usar DDD de forma pragmática**, sem transformar o projeto em uma cerimônia religiosa de abstrações.
4. **Aplicar TDD quando isso trouxer clareza e segurança**.
5. **Documentar decisões relevantes** por meio de ADRs.
6. **Extrair serviços no futuro** apenas quando houver necessidade real de escala, deploy independente ou isolamento tecnológico.

A direção arquitetural inicial é inspirada em:

- Monólito Modular
- Clean Architecture
- Arquitetura Hexagonal
- Domain-Driven Design
- Test-Driven Development
- Pensamento orientado a eventos, quando fizer sentido

---

## Estrutura Planejada de Alto Nível

O repositório poderá evoluir para uma organização como esta:

```text
atlas/
├── apps/
│   ├── web/                    # Dashboards React e interface de portfólio
│   ├── mobile/                 # Aplicativo Android em Kotlin, offline-first
│   └── desktop/                # Experimentos futuros para desktop
│
├── services/
│   ├── atlas_api/              # Aplicação principal em FastAPI
│   ├── atlas_worker/           # Workers e tarefas em background
│   ├── atlas_ai/               # RAG, agentes e integrações com LLMs
│   ├── atlas_scraper/          # Web scraping e coleta de dados
│   ├── atlas_stats/            # Estatística, probabilidade e regressão
│   └── atlas_automation/       # n8n, WhatsApp e automações sociais
│
├── packages/
│   ├── atlas_core/             # Entidades, objetos de valor e casos de uso
│   ├── atlas_shared/           # Schemas, DTOs e utilitários compartilhados
│   └── atlas_plugins/          # Provedores e integrações plugáveis
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

Essa estrutura representa uma direção planejada, não uma promessa de que todas as pastas já existem hoje.

---

## Módulos Principais

### Atlas Core

Base de domínio do sistema.

Responsabilidades planejadas:

- Entidades
- Objetos de valor
- Casos de uso
- Interfaces de repositório
- Eventos de domínio
- Regras de negócio
- Lógica pura em Python

Exemplos de entidades futuras:

- `DataSource`
- `Dataset`
- `Pipeline`
- `PipelineRun`
- `Experiment`
- `ModelRun`
- `StatisticalTest`
- `Agent`
- `Workflow`
- `Report`

---

### Atlas API

Camada HTTP do projeto.

Responsabilidades planejadas:

- Rotas com FastAPI
- Schemas de requisição e resposta
- Injeção de dependências
- Experimentos com autenticação
- Documentação automática da API
- Integração com casos de uso do domínio

Endpoints iniciais:

```text
GET /health
GET /version
```

---

### Atlas Data Mining

Responsável por coleta de dados e inteligência web.

Tópicos planejados:

- Web scraping
- Coleta via APIs
- Scraping assíncrono
- Parsing de HTML
- Automação de navegador
- Monitoramento de mudanças em páginas
- Boas práticas de scraping responsável
- Coleta de dados públicos

Possíveis casos de uso:

- Monitoramento de concursos e editais públicos
- Dados governamentais
- Inteligência de notícias
- Radar de tendências tecnológicas
- Inteligência de mídias sociais

---

### Atlas ETL

Responsável por transformar dados brutos em dados utilizáveis.

Tópicos planejados:

- Extração
- Limpeza
- Validação
- Transformação
- Carga no PostgreSQL
- Verificação de qualidade dos dados
- Cargas incrementais
- Logs de pipeline
- Experimentos com versionamento de dados

Fluxo geral:

```text
Fonte Externa
    ↓
Extrator
    ↓
Dados Brutos
    ↓
Validador
    ↓
Transformador
    ↓
PostgreSQL / DuckDB
    ↓
Analytics / ML / RAG
    ↓
API / Dashboard / Relatório
```

---

### Atlas Statistical Lab

Módulo focado em conectar Estatística acadêmica com software real.

Tópicos planejados:

- Estatística descritiva
- Distribuições de probabilidade
- Amostragem
- Simulação Monte Carlo
- Bootstrap
- Intervalos de confiança
- Testes de hipótese
- Regressão linear
- Diagnóstico de regressão
- Experimentos com séries temporais
- Métodos numéricos
- Fundamentos de cálculo aplicados à otimização

O objetivo é implementar conceitos estatísticos em Python antes de esconder tudo atrás de bibliotecas de alto nível.

---

### Atlas Machine Learning Lab

Módulo para aprendizado de máquina clássico e experimentação supervisionada/não supervisionada.

Tópicos planejados:

- Regressão linear
- Regressão logística
- KNN
- Árvores de decisão
- Random Forest
- Gradient Boosting
- Clusterização
- PCA
- Validação cruzada
- Métricas de avaliação
- Engenharia de atributos
- Experimentos reprodutíveis
- Comparação entre implementação manual e bibliotecas consolidadas

---

### Atlas Deep Learning Lab

Módulo dedicado ao estudo e implementação de redes neurais profundas, conectando fundamentos matemáticos, estatística, otimização e aplicações modernas de IA.

Tópicos planejados:

- Redes neurais artificiais do zero
- Perceptron e multilayer perceptron, ou MLP
- Funções de ativação
- Funções de perda
- Gradiente descendente
- Backpropagation
- Regularização
- Dropout
- Batch normalization
- Otimizadores como SGD, RMSProp e Adam
- Redes neurais convolucionais, ou CNNs
- Redes recorrentes, LSTM e GRU
- Autoencoders
- Embeddings
- Modelos para NLP
- Mecanismo de atenção
- Transformers
- Fine-tuning de modelos pré-treinados
- Experimentos com PyTorch
- Experimentos futuros com TensorFlow e Keras

Possíveis aplicações:

- Classificação de textos
- Análise de sentimentos
- Classificação de imagens
- Detecção de padrões em séries temporais
- Embeddings para busca semântica
- Comparação entre modelos clássicos e modelos neurais

Este módulo deve evitar o uso de redes neurais como caixa-preta. A ideia é estudar primeiro os fundamentos, implementar versões simples e depois usar frameworks modernos com mais consciência técnica e menos culto religioso ao `fit()`.

---

### Atlas AI Lab

Módulo para IA generativa e sistemas baseados em agentes.

Tópicos planejados:

- Integrações com LLMs
- Ollama para modelos locais
- Replicate e modelos em nuvem
- Embeddings
- Pipelines RAG
- Busca vetorial
- Agentes de IA
- Fluxos multiagentes
- Avaliação de prompts
- Guardrails
- Tool calling
- Estratégias de fallback entre modelos

Possível fluxo futuro:

```text
Usuário
 ↓
Chat / API / WhatsApp
 ↓
Roteador de Agentes
 ↓
Retriever
 ↓
Executor de Ferramentas
 ↓
Provedor de LLM
 ↓
Validador de Resposta
 ↓
Resposta + Logs + Métricas
```

---

### Atlas Automation

Módulo para automação de workflows e integrações externas.

Tópicos planejados:

- Workflows com n8n
- Alertas por e-mail
- Integração com WhatsApp
- Automação de mídias sociais
- Relatórios automáticos
- Tarefas agendadas
- Workflows baseados em eventos

Exemplo de fluxo:

```text
Novo dado coletado
    ↓
Pipeline processa os dados
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

### Atlas Web

Futura interface em React para dashboards, storytelling e apresentação do portfólio.

Funcionalidades planejadas:

- Landing page
- Mapa interativo do projeto
- Dashboards de dados
- Visualizações estatísticas
- Monitoramento de pipelines
- Histórico de experimentos
- Playground de RAG
- Interface gamificada de aprendizado

---

### Atlas Mobile

Futuro aplicativo Android em Kotlin.

Funcionalidades planejadas:

- Acesso offline-first
- Cache local com Room/SQLite
- Sincronização com API
- Notificações
- Dashboards simplificados
- Acesso a chatbot
- Experimentos de coleta de dados pelo celular

---

### Atlas Infrastructure

Base operacional do projeto.

Tópicos planejados:

- Docker
- Docker Compose
- PostgreSQL
- Experimentos com Redis
- GitHub Actions
- Deploy em cloud
- Logs
- Health checks
- Monitoramento
- Backups
- Experimentos com zero-downtime deployment

---

### Atlas Systems Lab

Módulo para conhecimentos de mais baixo nível em sistemas.

Tópicos planejados:

- Fundamentos de Linux
- Processos e threads
- Programação assíncrona
- Sockets
- Experimentos com TCP/UDP
- Comunicação P2P
- Noções de criptografia
- Problemas de concorrência
- Tolerância a falhas
- Testes de carga

---

### Atlas Legacy Lab

Módulo futuro para praticar manutenção e modernização de sistemas legados.

Tópicos planejados:

- Scripts legados bagunçados
- Testes de caracterização
- Refatoração
- Adapters
- Strangler Fig Pattern
- Documentação de dívida técnica

Esse módulo existe porque software real quase nunca chega limpo, documentado e emocionalmente disponível.

---

## Stack Tecnológica

### Atual / Inicial

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ou SQLModel
- Pydantic
- Docker
- Docker Compose
- pytest
- Git e GitHub

### Planejada / Experimental

- Pandas
- NumPy
- scikit-learn
- PyTorch
- TensorFlow / Keras
- DuckDB
- Redis
- React
- TypeScript
- Kotlin Android
- Room / SQLite
- n8n
- LangChain / LangGraph
- Flowise
- Ollama
- Replicate
- PGVector ou outro banco vetorial
- Grafana / Prometheus
- GitHub Actions

---

## Roadmap

### Fase 0: Fundação

- [ ] Organizar a estrutura do backend
- [ ] Criar endpoint `/health`
- [ ] Criar endpoint `/version`
- [ ] Conectar FastAPI ao PostgreSQL
- [ ] Adicionar testes básicos
- [ ] Adicionar documentação inicial
- [ ] Criar o primeiro ADR

### Fase 1: Atlas Core

- [ ] Criar entidades de domínio
- [ ] Criar casos de uso
- [ ] Criar interfaces de repositório
- [ ] Adicionar testes unitários
- [ ] Documentar decisões de domínio

### Fase 2: Data Mining e ETL

- [ ] Criar primeira fonte de dados
- [ ] Construir primeiro scraper
- [ ] Armazenar dados brutos
- [ ] Validar dados coletados
- [ ] Transformar e carregar no PostgreSQL
- [ ] Expor dados pela API

### Fase 3: Statistical Lab

- [ ] Adicionar módulo de estatística descritiva
- [ ] Adicionar simulações de probabilidade
- [ ] Adicionar experimentos de amostragem
- [ ] Adicionar exemplos de intervalo de confiança
- [ ] Adicionar exemplos de testes de hipótese
- [ ] Adicionar experimentos de regressão

### Fase 4: Machine Learning

- [ ] Adicionar experimentos iniciais de ML
- [ ] Adicionar métricas de avaliação de modelos
- [ ] Adicionar rastreio simples de experimentos reprodutíveis
- [ ] Comparar implementações manuais com modelos de bibliotecas

### Fase 5: Deep Learning

- [ ] Implementar uma rede neural simples do zero
- [ ] Implementar gradiente descendente e backpropagation em exemplo didático
- [ ] Criar experimento com MLP usando PyTorch
- [ ] Criar experimento de classificação de texto
- [ ] Criar experimento inicial com embeddings
- [ ] Comparar modelo clássico com rede neural em um mesmo problema

### Fase 6: AI Lab

- [ ] Adicionar embeddings
- [ ] Criar protótipo de RAG
- [ ] Integrar modelo local com Ollama
- [ ] Adicionar ferramentas baseadas em agentes
- [ ] Adicionar avaliação e logging de respostas

### Fase 7: Web e Storytelling

- [ ] Construir dashboard em React
- [ ] Adicionar relatórios visuais
- [ ] Criar mapa visual do portfólio
- [ ] Adicionar visualizações estatísticas

### Fase 8: Automação

- [ ] Adicionar workflows com n8n
- [ ] Adicionar alertas
- [ ] Automatizar relatórios
- [ ] Criar experimentos com WhatsApp ou e-mail

### Fase 9: Infraestrutura e Resiliência

- [ ] Adicionar pipeline de CI/CD
- [ ] Criar ambiente de deploy
- [ ] Adicionar monitoramento
- [ ] Adicionar testes de carga
- [ ] Adicionar experimentos de engenharia do caos

---

## Executando Localmente

Esta seção será expandida conforme a fundação do projeto for implementada.

Fluxo futuro esperado:

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas

docker compose up -d
```

Comando futuro para o backend:

```bash
cd backend
uvicorn main:app --reload
```

Comando futuro para testes:

```bash
pytest
```

---

## Estratégia de Aprendizado

O Atlas foi pensado para crescer em ciclos pequenos e documentados.

Cada ciclo deve gerar:

- Código funcional
- Testes
- Documentação
- Uma decisão arquitetural clara
- Uma explicação aproveitável no portfólio
- Uma conexão com dados, estatística, IA ou engenharia de software

O projeto não deve tentar ficar completo de uma só vez. Ele deve evoluir como software real: incrementalmente, com algum sofrimento inevitável e com menos ilusões a cada semana.

---

## Valor como Portfólio

O Atlas pretende demonstrar capacidade de:

- Projetar sistemas modulares
- Construir APIs
- Trabalhar com bancos de dados
- Coletar e processar dados
- Aplicar estatística em problemas reais
- Construir experimentos de machine learning
- Usar IA generativa de forma responsável
- Automatizar workflows
- Documentar decisões técnicas
- Pensar em escalabilidade, resiliência e manutenibilidade

---

## License

Este projeto está licenciado sob a licença MIT.

---

## Autor

Desenvolvido por **Caio Costa Cavalcante** como um portfólio técnico de longo prazo e laboratório de aprendizado em Dados, IA, Estatística e Engenharia de Software.

