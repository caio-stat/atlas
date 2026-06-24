# Atlas — Plano de Execução e Guia de Contexto para IA

Este documento registra o estado atual, a direção técnica e a sequência de evolução do projeto **Atlas**.

Ele deve servir como referência para:

* o próprio Caio acompanhar a evolução do projeto;
* ChatGPT/Codex/assistentes de IA entenderem o contexto antes de sugerir mudanças;
* manter o projeto incremental, didático, executável e útil como portfólio;
* evitar que o Atlas vire apenas uma coleção de ideias sem implementação.

---

## 1. Identidade do projeto

O **Atlas** é um laboratório modular de:

* Dados;
* Estatística;
* Inteligência Artificial;
* Engenharia de Software;
* Automação;
* Infraestrutura;
* Suporte técnico;
* Redes;
* Cloud;
* Mobile;
* Document Intelligence;
* Sistemas reais.

Ele funciona ao mesmo tempo como:

* portfólio técnico;
* laboratório de aprendizagem;
* sandbox de arquitetura;
* base de estudos;
* plataforma de experimentação;
* narrativa profissional da jornada de Caio em Estatística, Ciência de Dados, IA e Engenharia de Software.

O objetivo não é criar tutoriais soltos.
O objetivo é construir um ecossistema real, evolutivo e bem documentado.

---

## 2. Filosofia do Atlas

O Atlas deve crescer de forma incremental.

Cada nova entrega precisa gerar pelo menos uma das seguintes coisas:

* código executável;
* teste automatizado;
* documentação;
* aprendizado técnico;
* evidência de portfólio;
* conexão com dados reais;
* conexão com estatística;
* conexão com IA;
* conexão com automação;
* conexão com suporte, redes ou infraestrutura.

O Atlas não deve começar como microsserviços.

A arquitetura inicial deve ser um **monólito modular**, com fronteiras claras entre domínio, casos de uso, API, infraestrutura, dados e experimentos.

Microsserviços, Kubernetes, mensageria complexa, agentes autônomos e cloud avançada só devem entrar quando houver motivo técnico real.

---

## 3. Estado atual resumido

O projeto já possui uma base inicial com:

* repositório público no GitHub;
* README em inglês;
* README em português;
* backend com FastAPI;
* endpoints básicos de saúde e versão;
* configuração inicial de PostgreSQL com Docker Compose;
* testes básicos com pytest;
* estrutura documental ampla;
* diretórios para backend, docs, requirements, notebooks, datasets, analytics, scrapers, infra e apps/mobile;
* entidade `DataSource` já iniciada;
* caso de uso `RegisterDataSource` já iniciado;
* vários arquivos de requirements por área;
* visão expandida de módulos técnicos.

O estado atual ainda é de **fundação**.

Há muita visão documentada, mas o código executável ainda precisa crescer em fatias pequenas.

---

## 4. Regra principal para qualquer IA que ajudar no projeto

Antes de sugerir qualquer coisa, a IA deve respeitar estas regras:

1. Ler o README atual.
2. Ler este documento.
3. Verificar a estrutura real do repositório.
4. Não assumir que os arquivos estão vazios sem verificar.
5. Não tratar arquivos em LF como se estivessem em uma linha só.
6. Não sugerir arquitetura gigante antes da próxima entrega pequena.
7. Priorizar backend funcional, testes e documentação.
8. Sempre separar:

   * o que já existe;
   * o que está parcial;
   * o que ainda falta;
   * o próximo passo real.
9. Sempre propor commits pequenos.
10. Sempre que sugerir um arquivo, explicar o que ele deve conter.

---

## 5. Decisão arquitetural base

A decisão inicial do Atlas é:

> Começar como um monólito modular em Python/FastAPI, com domínio separado, casos de uso testáveis, API versionada, PostgreSQL, Docker Compose, pytest e documentação por ADR.

A arquitetura inicial deve evitar:

* microsserviços prematuros;
* Kubernetes prematuro;
* filas complexas sem necessidade;
* IA antes de dados minimamente organizados;
* frontend sofisticado antes de API útil;
* automação externa sem logs e controle;
* scraping sem responsabilidade;
* cloud antes de deploy local estável.

---

## 6. Estrutura desejada de longo prazo

A estrutura de longo prazo pode evoluir para algo próximo disso:

```text
atlas/
├── apps/
│   ├── web/
│   ├── mobile/
│   └── desktop/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── domain/
│   │   ├── use_cases/
│   │   ├── infrastructure/
│   │   ├── middlewares/
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   ├── contract/
│   │   └── fakes/
│   │
│   ├── alembic/
│   ├── requirements.txt
│   └── README.md
│
├── analytics/
│   ├── statistics/
│   ├── ml/
│   ├── numerical_methods/
│   ├── etl/
│   ├── bi/
│   └── documents/
│
├── scrapers/
│   ├── public_sources/
│   ├── parsers/
│   └── samples/
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   ├── samples/
│   └── README.md
│
├── notebooks/
│   ├── statistics/
│   ├── ml/
│   ├── numerical_methods/
│   ├── data_engineering/
│   └── experiments/
│
├── docs/
│   ├── adr/
│   ├── architecture/
│   ├── roadmap/
│   ├── modules/
│   ├── data-governance/
│   ├── runbooks/
│   └── model-cards/
│
├── requirements/
├── scripts/
├── infra/
├── docker-compose.yml
├── README.md
├── README.pt-BR.md
└── LICENSE
```

Essa estrutura não precisa ser criada toda de uma vez.

Ela deve ser preenchida conforme as entregas forem surgindo.

---

## 7. Módulos principais do Atlas

### 7.1 Atlas Core

Responsável pelo domínio puro.

Deve conter:

* entidades;
* objetos de valor;
* eventos de domínio;
* erros de domínio;
* contratos;
* regras puras;
* invariantes;
* lógica independente de banco, API e frameworks.

Entidades iniciais:

* `DataSource`;
* `Dataset`;
* `Pipeline`;
* `PipelineRun`;
* `Experiment`;
* `ModelRun`;
* `Report`;
* `Document`;
* `Workflow`;
* `SupportReport`.

---

### 7.2 Atlas API

Responsável por expor o sistema via HTTP.

Deve conter:

* rotas versionadas;
* schemas Pydantic;
* tratamento de erros;
* injeção de dependências;
* endpoints de saúde;
* endpoints de prontidão;
* endpoints para cadastro e consulta de dados.

Endpoints iniciais:

```text
GET  /health
GET  /version
GET  /api/v1/health
GET  /api/v1/version
GET  /api/v1/ready
POST /api/v1/data-sources
GET  /api/v1/data-sources
GET  /api/v1/data-sources/{id}
```

---

### 7.3 Atlas Data Mining

Responsável por coleta de dados.

Inclui:

* scraping;
* consumo de APIs públicas;
* coleta de páginas;
* captura de HTML;
* parsers;
* OCR;
* extração de documentos;
* dados governamentais;
* dados acadêmicos;
* dados de saúde;
* dados de vagas;
* dados de tecnologia.

Submódulos:

* Atlas Web Scraping Lab;
* Atlas OCR Lab;
* Atlas Document Intelligence Lab.

---

### 7.4 Atlas ETL / Data Engineering

Responsável por transformar dados brutos em dados úteis.

Deve conter:

* extração;
* limpeza;
* normalização;
* validação;
* carga;
* data quality;
* linhagem;
* versionamento de dados;
* pipelines reprodutíveis;
* PostgreSQL;
* DuckDB;
* arquivos raw e processed.

---

### 7.5 Atlas Statistical Lab

Responsável por conectar o Atlas à formação em Estatística.

Deve conter:

* estatística descritiva;
* probabilidade;
* inferência;
* regressão;
* séries temporais;
* bootstrap;
* Monte Carlo;
* testes de hipótese;
* intervalos de confiança;
* análise exploratória;
* diagnóstico de modelos.

---

### 7.6 Atlas Numerical Methods / Calculus Lab

Responsável por conectar matemática, cálculo e computação.

Deve conter:

* derivadas numéricas;
* limites;
* gradiente;
* otimização;
* bisseção;
* Newton-Raphson;
* integração numérica;
* EDOs futuramente;
* erro numérico;
* visualização de funções.

---

### 7.7 Atlas Machine Learning Lab

Responsável por modelos clássicos de ML.

Deve conter:

* baselines;
* regressão linear;
* regressão logística;
* KNN;
* árvores;
* random forest;
* gradient boosting;
* clustering;
* PCA;
* pipelines sklearn;
* validação cruzada;
* métricas;
* model cards;
* rastreamento de experimentos.

---

### 7.8 Atlas Deep Learning Lab

Responsável por redes neurais.

Deve conter:

* perceptron;
* MLP;
* gradiente descendente;
* backpropagation;
* funções de ativação;
* funções de perda;
* regularização;
* CNNs;
* RNNs;
* LSTM;
* GRU;
* embeddings;
* atenção;
* transformers;
* PyTorch;
* TensorFlow/Keras.

Esse módulo deve vir depois de estatística, ML clássico e bases de dados minimamente organizadas.

---

### 7.9 Atlas AI Lab

Responsável por IA generativa, RAG e agentes.

Deve conter:

* LLMs;
* Ollama;
* Replicate;
* LangChain;
* LangGraph;
* Flowise;
* embeddings;
* banco vetorial;
* RAG;
* agentes;
* ferramentas;
* avaliação de resposta;
* guardrails;
* citação de fontes;
* fallback entre modelos.

Não deve entrar antes de existir base documental ou dados organizados.

---

### 7.10 Atlas Automation Lab

Responsável por automações.

Deve conter:

* n8n;
* webhooks;
* e-mail;
* WhatsApp;
* relatórios automáticos;
* alertas;
* publicação de changelog;
* automações acadêmicas;
* automações de portfólio;
* geração de post a partir de relatório.

Toda automação externa deve ter:

* log;
* limite;
* controle;
* possibilidade de revisão humana;
* rollback quando fizer sentido.

---

### 7.11 Atlas Support Lab

Responsável por automações e diagnósticos de suporte técnico.

Deve conter:

* inventário de máquina;
* diagnóstico de CPU, RAM, disco e rede;
* coleta de informações do Windows;
* relatórios de suporte;
* health check de endpoints;
* scripts de manutenção;
* evidências em Markdown ou HTML.

Esse módulo é muito importante porque conecta o Atlas ao trabalho real em suporte/helpdesk.

---

### 7.12 Atlas Networking Lab

Responsável por redes.

Deve conter:

* ping;
* DNS;
* latência;
* portas;
* sockets;
* scanner autorizado;
* testes de conectividade;
* diagnóstico de internet;
* análise de rede local;
* noções TCP/UDP;
* automações com SSH.

Sempre respeitar autorização e escopo.

---

### 7.13 Atlas Cloud / DevOps Lab

Responsável por infraestrutura, cloud e deploy.

Deve conter:

* Docker;
* Docker Compose;
* PostgreSQL;
* Redis futuramente;
* MinIO futuramente;
* GitHub Actions;
* deploy em VPS;
* AWS;
* GCP;
* Azure;
* logs;
* métricas;
* backups;
* rollback;
* ambientes dev/staging/prod.

---

### 7.14 Atlas Mobile

Responsável pelo app Android.

Ideia inicial:

> Atlas Pocket

O app deve começar simples:

* tela de saúde da API;
* versão da API;
* status do banco;
* lista de fontes de dados;
* cache local;
* offline-first;
* sincronização futura;
* notificações futuras.

---

### 7.15 Atlas Web

Responsável pelo frontend web.

Deve conter:

* landing page;
* dashboard;
* painel de saúde;
* visualização de fontes;
* visualização de pipelines;
* storytelling;
* laboratório estatístico visual.

Esse módulo deve vir depois da API ter dados reais.

---

### 7.16 Atlas Legacy Lab

Responsável por simular código legado e modernizá-lo.

Deve conter:

* código ruim proposital;
* testes de caracterização;
* refatoração incremental;
* adapters;
* Strangler Fig Pattern;
* documentação de dívida técnica.

Esse módulo é bom para mostrar maturidade profissional.

---

## 8. Próxima fatia vertical obrigatória

A próxima entrega real deve ser:

```text
DataSource completo do domínio até a API
```

Essa fatia deve passar por:

```text
DataSource entity
↓
RegisterDataSource use case
↓
Repository Protocol
↓
In-memory repository
↓
API schema
↓
POST /api/v1/data-sources
↓
unit tests
↓
API contract tests
↓
SQLAlchemy repository
↓
Alembic migration
↓
PostgreSQL persistence
```

---

## 9. Ordem recomendada dos próximos commits

### Commit 1 — alinhar documentação

Mensagem sugerida:

```bash
git commit -m "docs: align roadmap with current DataSource implementation"
```

Arquivos:

```text
README.md
README.pt-BR.md
backend/README.md
backend/README.pt-BR.md
docs/roadmap/atlas-plano-execucao-ia.md
```

Objetivo:

* deixar claro que `DataSource` e `RegisterDataSource` já existem parcialmente;
* deixar claro que ainda faltam rota, banco, migration e testes completos.

---

### Commit 2 — testes do domínio

Mensagem sugerida:

```bash
git commit -m "test: add DataSource domain tests"
```

Arquivos:

```text
backend/tests/unit/domain/test_data_source.py
```

Testar:

* criação válida;
* nome vazio;
* localização vazia;
* tipo válido;
* status padrão;
* id UUID.

---

### Commit 3 — testes do caso de uso

Mensagem sugerida:

```bash
git commit -m "test: add RegisterDataSource use case tests"
```

Arquivos:

```text
backend/tests/unit/use_cases/test_register_data_source.py
backend/tests/fakes/fake_data_source_repository.py
```

Testar:

* cadastro com sucesso;
* duplicidade;
* chamada ao repositório;
* retorno da entidade criada.

---

### Commit 4 — API versionada

Mensagem sugerida:

```bash
git commit -m "refactor: add versioned API router"
```

Arquivos:

```text
backend/app/api/router.py
backend/app/api/routes/health.py
backend/app/api/routes/version.py
backend/app/main.py
backend/tests/test_health.py
backend/tests/test_version.py
```

Objetivo:

* criar `/api/v1/health`;
* criar `/api/v1/version`;
* manter endpoints antigos se necessário.

---

### Commit 5 — settings tipado

Mensagem sugerida:

```bash
git commit -m "feat: add typed application settings"
```

Arquivos:

```text
backend/app/core/config.py
backend/app/core/README.md
backend/app/database.py
```

Objetivo:

* parar de deixar configuração fixa espalhada;
* centralizar `DATABASE_URL`, nome da aplicação, versão e ambiente.

---

### Commit 6 — schemas de DataSource

Mensagem sugerida:

```bash
git commit -m "feat: add DataSource API schemas"
```

Arquivos:

```text
backend/app/api/schemas/data_source.py
backend/app/api/schemas/__init__.py
```

Schemas:

```text
RegisterDataSourceRequest
DataSourceResponse
DataSourceErrorResponse
```

---

### Commit 7 — rota POST /data-sources em memória

Mensagem sugerida:

```bash
git commit -m "feat: expose DataSource registration endpoint"
```

Arquivos:

```text
backend/app/api/routes/data_sources.py
backend/app/infrastructure/repositories/in_memory_data_source_repository.py
backend/app/api/router.py
```

Endpoint:

```text
POST /api/v1/data-sources
```

---

### Commit 8 — testes de contrato da API

Mensagem sugerida:

```bash
git commit -m "test: add DataSource API contract tests"
```

Arquivos:

```text
backend/tests/contract/api/test_data_sources_api.py
```

Testar:

* sucesso retorna 201;
* payload inválido retorna 422;
* duplicidade retorna 409;
* erro de domínio retorna 400.

---

### Commit 9 — persistência SQLAlchemy

Mensagem sugerida:

```bash
git commit -m "feat: add SQLAlchemy DataSource repository"
```

Arquivos:

```text
backend/app/infrastructure/database/base.py
backend/app/infrastructure/database/session.py
backend/app/infrastructure/database/models/data_source_model.py
backend/app/infrastructure/repositories/sqlalchemy_data_source_repository.py
backend/app/domain/repositories/data_source_repository.py
```

---

### Commit 10 — migration Alembic

Mensagem sugerida:

```bash
git commit -m "feat: add DataSource database migration"
```

Arquivos:

```text
backend/alembic.ini
backend/alembic/env.py
backend/alembic/versions/0001_create_data_sources.py
```

---

### Commit 11 — readiness

Mensagem sugerida:

```bash
git commit -m "feat: add readiness endpoint"
```

Arquivos:

```text
backend/app/api/routes/readiness.py
backend/tests/integration/test_readiness.py
```

Endpoint:

```text
GET /api/v1/ready
```

Deve verificar se a aplicação consegue falar com o banco.

---

### Commit 12 — CI

Mensagem sugerida:

```bash
git commit -m "ci: add backend test workflow"
```

Arquivos:

```text
.github/workflows/backend-tests.yml
README.md
README.pt-BR.md
```

Objetivo:

* rodar pytest automaticamente no GitHub Actions;
* adicionar badge no README.

---

### Commit 13 — ADR do monólito modular

Mensagem sugerida:

```bash
git commit -m "docs: document modular monolith decision"
```

Arquivos:

```text
docs/adr/0001-modular-monolith.md
```

Conteúdo:

* contexto;
* decisão;
* alternativas;
* consequências;
* quando mudar para serviços.

---

## 10. Arquivos importantes a criar e o que terão

### `backend/app/core/config.py`

Responsável por configurações da aplicação.

Deve conter:

```text
Settings
get_settings()
DATABASE_URL
APP_NAME
APP_VERSION
ENVIRONMENT
LOG_LEVEL
```

---

### `backend/app/api/router.py`

Responsável por agrupar rotas.

Deve conter:

```text
api_router = APIRouter()
api_router.include_router(...)
```

---

### `backend/app/api/routes/health.py`

Responsável por liveness.

Deve conter:

```text
GET /api/v1/health
```

Não deve consultar banco.

---

### `backend/app/api/routes/readiness.py`

Responsável por readiness.

Deve conter:

```text
GET /api/v1/ready
```

Deve consultar banco ou dependências essenciais.

---

### `backend/app/api/routes/version.py`

Responsável por versão.

Deve conter:

```text
GET /api/v1/version
```

---

### `backend/app/api/routes/data_sources.py`

Responsável por rotas de fontes de dados.

Deve conter inicialmente:

```text
POST /api/v1/data-sources
GET  /api/v1/data-sources
```

---

### `backend/app/api/schemas/data_source.py`

Responsável pelos contratos HTTP.

Deve conter:

```text
RegisterDataSourceRequest
DataSourceResponse
```

---

### `backend/app/domain/entities/data_source.py`

Responsável pela entidade de domínio.

Deve conter:

```text
DataSource
DataSourceType
DataSourceStatus
```

Não deve depender de FastAPI, SQLAlchemy nem Pydantic.

---

### `backend/app/domain/errors.py`

Responsável por erros de domínio.

Deve conter:

```text
AtlasDomainError
InvalidDataSourceError
DuplicateDataSourceError
DataSourceNotFoundError
```

---

### `backend/app/domain/repositories/data_source_repository.py`

Responsável pelo contrato do repositório.

Deve conter:

```text
DataSourceRepository Protocol
```

---

### `backend/app/use_cases/register_data_source.py`

Responsável pelo caso de uso.

Deve conter:

```text
RegisterDataSourceInput
RegisterDataSource
```

Não deve saber se os dados vão para memória, PostgreSQL ou outro lugar.

---

### `backend/app/infrastructure/repositories/in_memory_data_source_repository.py`

Responsável por repositório simples para testes e protótipo.

Deve conter:

```text
exists_by_name()
save()
list()
get_by_id()
```

---

### `backend/app/infrastructure/repositories/sqlalchemy_data_source_repository.py`

Responsável por persistência real.

Deve conter:

```text
exists_by_name()
save()
list()
get_by_id()
```

---

### `backend/app/infrastructure/database/models/data_source_model.py`

Responsável pelo modelo SQLAlchemy.

Deve conter:

```text
DataSourceModel
```

Campos:

```text
id
name
type
location
status
created_at
updated_at
```

---

### `backend/tests/unit/domain/test_data_source.py`

Responsável por testar a entidade.

---

### `backend/tests/unit/use_cases/test_register_data_source.py`

Responsável por testar o caso de uso.

---

### `backend/tests/contract/api/test_data_sources_api.py`

Responsável por testar o contrato HTTP.

---

### `docs/adr/0001-modular-monolith.md`

Responsável por documentar a decisão arquitetural.

---

## 11. Critérios de pronto para a primeira grande entrega

A primeira grande entrega estará pronta quando:

* `pytest` passar localmente;
* GitHub Actions passar;
* `/api/v1/health` funcionar;
* `/api/v1/version` funcionar;
* `/api/v1/ready` funcionar;
* `POST /api/v1/data-sources` funcionar;
* `DataSource` for persistido no PostgreSQL;
* migration Alembic criar a tabela;
* README refletir o estado real;
* ADR explicar o monólito modular;
* houver testes unitários, de contrato e integração mínima.

---

## 12. Como a IA deve responder quando Caio pedir “próximo passo”

A resposta deve seguir este formato:

```text
1. Diagnóstico
2. Decisão técnica
3. Arquivos afetados
4. Implementação
5. Testes
6. Comandos
7. Documentação
8. Próximo commit
```

A IA deve evitar respostas genéricas.

Exemplo ruim:

```text
Agora implemente o banco e faça testes.
```

Exemplo bom:

```text
Agora crie o arquivo backend/tests/unit/domain/test_data_source.py com testes para criação válida, nome vazio e localização vazia. Depois rode python -m pytest. O commit sugerido é test: add DataSource domain tests.
```

---

## 13. Como decidir prioridade

A prioridade deve seguir esta ordem:

1. Código executável.
2. Teste.
3. Documentação.
4. Integração com banco.
5. API.
6. Dados reais.
7. Estatística.
8. ML.
9. IA.
10. Automação.
11. Frontend.
12. Mobile.
13. Cloud avançada.
14. Sistemas distribuídos.

Não pular etapas.

---

## 14. O que não fazer agora

Não fazer agora:

* Kubernetes;
* microsserviços;
* mensageria complexa;
* agentes autônomos;
* dashboard sofisticado;
* app mobile completo;
* IA generativa conectada a tudo;
* scraping massivo;
* deploy cloud complexo;
* Power BI antes de dataset organizado;
* ML antes de dados e métrica;
* refatoração gigante sem teste.

---

## 15. O que fazer agora

Fazer agora:

```text
1. Alinhar README com o estado real.
2. Testar DataSource.
3. Testar RegisterDataSource.
4. Criar API versionada.
5. Criar POST /api/v1/data-sources.
6. Criar repositório em memória.
7. Criar testes da API.
8. Conectar PostgreSQL.
9. Criar migration.
10. Criar readiness.
11. Criar CI.
12. Completar ADR.
```

---

## 16. Comandos úteis

Rodar testes:

```bash
cd backend
python -m pytest
```

Rodar API:

```bash
cd backend
python -m uvicorn app.main:app --reload
```

Subir banco:

```bash
docker compose up -d
```

Ver logs do banco:

```bash
docker compose logs -f db
```

Adicionar arquivos:

```bash
git add .
```

Criar commit:

```bash
git commit -m "mensagem do commit"
```

Enviar para o GitHub:

```bash
git push
```

---

## 17. Convenção de commits

Usar mensagens como:

```text
docs: ...
test: ...
feat: ...
fix: ...
refactor: ...
ci: ...
chore: ...
```

Exemplos:

```bash
git commit -m "docs: align Atlas roadmap with current backend state"
git commit -m "test: add DataSource domain tests"
git commit -m "feat: expose DataSource registration endpoint"
git commit -m "refactor: extract versioned API router"
git commit -m "ci: add backend test workflow"
```

---

## 18. Regra de documentação

Sempre que criar um módulo, criar ou atualizar um README próximo.

Exemplos:

```text
backend/app/domain/README.md
backend/app/use_cases/README.md
backend/app/api/README.md
backend/app/infrastructure/README.md
analytics/statistics/README.md
scrapers/README.md
datasets/README.md
docs/modules/support-lab/README.md
```

Cada README deve responder:

```text
O que é este módulo?
Por que ele existe?
O que ele contém?
O que ainda falta?
Como testar?
Como isso se conecta ao Atlas?
```

---

## 19. Regra de testes

Todo módulo estável deve ter teste.

Tipos de teste:

```text
unit: testa domínio e casos de uso isolados
contract: testa contrato da API
integration: testa integração com banco ou serviço externo
e2e: testa fluxo completo
```

Ordem recomendada:

```text
unit
↓
contract
↓
integration
↓
e2e
```

---

## 20. Regra para dados

Todo dataset deve ter:

```text
fonte
data de coleta
licença ou termos de uso
descrição
colunas
tipos
limitações
possíveis vieses
qualidade
linhagem
```

Criar template:

```text
datasets/DATASET_CARD_TEMPLATE.md
```

---

## 21. Regra para modelos de ML

Todo modelo deve ter:

```text
objetivo
dataset usado
features
target
baseline
métrica principal
métricas secundárias
validação
limitações
risco de viés
como reproduzir
```

Criar template:

```text
docs/model-cards/MODEL_CARD_TEMPLATE.md
```

---

## 22. Regra para IA generativa

Toda funcionalidade com LLM deve ter:

```text
fonte dos dados
estratégia de recuperação
citações
limitações
avaliação
logs
guardrails
fallback
política de uso
```

Não criar agente sem:

```text
objetivo claro
ferramentas permitidas
limites
logs
teste
modo de falha
```

---

## 23. Regra para suporte e redes

Todo script de suporte deve ser read-only por padrão.

Antes de qualquer ação que modifique máquina, rede ou configuração:

* pedir confirmação;
* registrar o que será alterado;
* oferecer rollback quando possível;
* separar evidência de inferência.

Exemplo:

```text
Evidência: disco com 92% de uso.
Inferência: pode haver impacto em performance.
Ação sugerida: limpar temporários, revisar arquivos grandes e verificar saúde do disco.
```

---

## 24. Regra para scraping

Todo scraping deve respeitar:

* termos da fonte;
* rate limit;
* robots.txt quando aplicável;
* mínimo necessário;
* identificação da fonte;
* logs de coleta;
* não publicar dados sensíveis;
* salvar raw quando útil;
* parser testável sem internet.

Separar:

```text
collector: acessa a web
parser: transforma HTML/texto em dados
pipeline: coordena coleta, transformação e carga
```

---

## 25. Regra para notebooks

Notebooks são bons para exploração, mas não devem ser o produto final.

Fluxo correto:

```text
notebook exploratório
↓
função Python reutilizável
↓
teste
↓
documentação
↓
relatório ou API
```

---

## 26. Regra para portfólio

Cada entrega importante deve gerar evidência.

Exemplos:

* print do endpoint funcionando;
* teste passando;
* badge do CI;
* notebook com análise;
* relatório em Markdown;
* ADR;
* dataset card;
* model card;
* dashboard;
* changelog.

O Atlas deve contar uma história de evolução técnica, não apenas acumular arquivos.

---

## 27. Próximo pedido ideal para a IA

Depois de criar este arquivo, o próximo pedido recomendado é:

```text
Leia o README atual, o backend e docs/roadmap/atlas-plano-execucao-ia.md. Verifique o estado atual real e me diga exatamente o próximo commit pequeno, com os arquivos e conteúdos.
```

---

## 28. Resumo final

O Atlas está na fase de transformar visão em execução.

O foco imediato é:

```text
DataSource completo
API versionada
Testes
PostgreSQL
Migration
Readiness
CI
ADR
README alinhado
```

Depois disso, o projeto pode avançar para:

```text
Data catalog
Datasets
ETL
Estatística
ML
Document Intelligence
RAG
Automação
Support Lab
Networking
Cloud
Mobile
Web
```

A regra é simples:

> Um passo pequeno, testável, documentado e com valor de portfólio por vez.
