# Atlas

> Um laboratório modular para dados, estatística, inteligência artificial, automação, infraestrutura e engenharia de software.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-funda%C3%A7%C3%A3o-009688)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-local-336791)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-funda%C3%A7%C3%A3o-yellow)](#estado-atual)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[English](README.md) | **Português**

## Sumário

- [Visão geral](#visão-geral)
- [Estado atual](#estado-atual)
- [Visão e objetivos](#visão-e-objetivos)
- [Arquitetura](#arquitetura)
- [Mapa do repositório](#mapa-do-repositório)
- [Trilhas técnicas](#trilhas-técnicas)
- [Módulos do sistema](#módulos-do-sistema)
- [Estratégia de dependências](#estratégia-de-dependências)
- [Início rápido](#início-rápido)
- [Comportamento da API](#comportamento-da-api)
- [Fluxo de desenvolvimento](#fluxo-de-desenvolvimento)
- [Testes e qualidade](#testes-e-qualidade)
- [Sistema de documentação](#sistema-de-documentação)
- [Roadmap](#roadmap)
- [Uso responsável](#uso-responsável)
- [Evidências de portfólio](#evidências-de-portfólio)
- [Licença](#licença)
- [Autor](#autor)

## Visão geral

O Atlas é um portfólio técnico de longo prazo e um laboratório de aprendizagem
projetado para conectar assuntos frequentemente estudados em separado:
engenharia backend, pipelines de dados, estatística, métodos numéricos, machine
learning, deep learning, IA generativa, automação, suporte técnico, redes,
operações cloud, observabilidade, aplicações mobile, sistemas embarcados e
simulação interativa.

O projeto não pretende se tornar uma pilha de scripts sem relação ou um catálogo
de tecnologias instaladas para aparência. Toda capacidade relevante deve
evoluir para uma pequena fatia de produto com problema claro, contratos
explícitos, código executável, testes, documentação, limitações e evidências.
Além da qualidade técnica, o Atlas também deve apoiar clareza, confiança,
pertencimento e bem-estar humano. O sistema deve ser pensado para ajudar o
usuário a entender, escolher com informação, se sentir respeitado e experienciar
uma sensação de segurança em seu contexto social e cultural.

O Atlas começa como um **monólito modular**. Distribuição, filas, recursos cloud
ou serviços independentes devem surgir somente quando um caso de uso
implementado criar necessidade concreta de isolamento, escala, latência,
confiabilidade ou independência de deploy.

A pergunta central é:

> Como uma pessoa em formação técnica pode evoluir de scripts e notebooks para sistemas manuteníveis, produtos de dados confiáveis e aplicações inteligentes responsáveis que também fortaleçam clareza, autonomia, pertencimento e bem-estar humano?

## Estado atual

O Atlas está na **fase de fundação**. A documentação agora define em detalhes as
trilhas técnicas e as fronteiras dos módulos, enquanto o código executável ainda
é pequeno.

| Capacidade | Status | Evidência |
|---|---|---|
| Processo FastAPI | Implementação inicial | [`backend/app/main.py`](backend/app/main.py) |
| Endpoints raiz, saúde e versão | Implementados | [`backend/tests/test_health.py`](backend/tests/test_health.py) |
| Serviço PostgreSQL local | Configurado | [`docker-compose.yml`](docker-compose.yml) |
| Engine e factory de sessão SQLAlchemy | Scaffold inicial | [`backend/app/database.py`](backend/app/database.py) |
| Entidade e caso de registro | Scaffold vazio | [`backend/app/domain`](backend/app/domain/README.pt-BR.md), [`backend/app/use_cases`](backend/app/use_cases/README.pt-BR.md) |
| Decisão sobre monólito modular | Apenas placeholder de ADR | [`backend/0001-monolito-modular.md`](backend/0001-monolito-modular.md) |
| Trilhas de dependências | 76 conjuntos organizados | [`requirements/README.pt-BR.md`](requirements/README.pt-BR.md) |
| Documentação das trilhas | 21 guias bilíngues | [`docs/tracks/README.pt-BR.md`](docs/tracks/README.pt-BR.md) |
| Atlas Mobile Lab | Stack especificada; aplicação ainda não criada | [`docs/modules/mobile-lab/README.pt-BR.md`](docs/modules/mobile-lab/README.pt-BR.md) |

O marco imediato é uma fatia vertical completa:

```text
settings tipados
    ↓
rota versionada da API
    ↓
caso de uso de registro de fonte
    ↓
entidade e porta de repository
    ↓
adapter SQLAlchemy e migração
    ↓
testes unitários + contrato + integração
```

## Visão e objetivos

O Atlas possui quatro papéis simultâneos.

| Papel | Significado |
|---|---|
| Portfólio técnico | Demonstrar engenharia aplicada por evidências revisáveis, não por listas de habilidades. |
| Laboratório de aprendizagem | Estudar conceitos dentro de módulos e experimentos reais, não em snippets isolados. |
| Plataforma modular | Reutilizar contratos estáveis entre dados, IA, automação, operações e aplicações clientes. |
| Narrativa de engenharia | Registrar como decisões, tradeoffs, qualidade e fronteiras evoluem ao longo do tempo. |

Objetivos do projeto:

- construir aplicações backend Python manuteníveis;
- conectar coleta, ETL, estatística, ML e relatórios;
- estudar fundamentos matemáticos por experimentos executáveis;
- construir RAG e agentes com avaliação e controle de políticas;
- automatizar rotinas operacionais e de suporte com segurança;
- explorar redes, mensageria, concorrência, resiliência e observabilidade;
- criar clientes mobile e edge com restrições explícitas de offline e segurança;
- praticar DDD, TDD, arquitetura, refatoração e documentação de forma pragmática;
- publicar demonstrações que expliquem premissas e limitações com honestidade;
- projetar interfaces, fluxos e políticas com segurança psicológica,
  transparência, justiça e sensibilidade social;
- estudar como percepção, identidade, hábito, ética, comunidade e narrativa
  influenciam comportamento, confiança e bem-estar do usuário.

## Arquitetura

### Princípios

1. Começar com a arquitetura mais simples que atende ao caso de uso atual.
2. Manter regras de domínio independentes de HTTP, SQLAlchemy, SDKs cloud e UI.
3. Usar contratos explícitos nas fronteiras e adapters substituíveis para sistemas externos.
4. Adicionar infraestrutura em resposta a necessidades medidas, não à escala imaginada.
5. Preferir fatias verticais a grandes fundações horizontais sem comportamento visível.
6. Aplicar DDD e TDD quando melhorarem linguagem, feedback e segurança de mudanças.
7. Registrar decisões transversais ou caras por Architecture Decision Records.
8. Tratar telemetria, segurança, privacidade, rollback e documentação como engenharia.
9. Projetar sistemas que respeitem autonomia, dignidade, contexto cultural e segurança psicológica.
10. Preferir ciclos de feedback que reduzam confusão, apoiem reflexão e incentivem comportamentos saudáveis.
11. Instalar dependências por trilha focada, não em um ambiente universal.
12. Separar claramente arquitetura planejada de comportamento implementado.

### Runtime atual

```text
Cliente
  ↓ HTTP
Aplicação FastAPI (`backend/app/main.py`)
  ↓
Função de rota síncrona
  ↓
Resposta JSON estática

Container PostgreSQL ← configurado localmente, ainda não usado por endpoint
```

### Fluxo modular pretendido

```text
Web / Mobile / Automação / Agente
                ↓
          Router da Atlas API
                ↓
          Caso de uso
                ↓
       Modelo de domínio e portas
                ↑
 Adapters SQL / fila / provedores
                ↓
 PostgreSQL / broker / cloud / modelo
```

O fluxo pretendido é orientação de direção. Ele não autoriza criar todas as
camadas antes que o primeiro caso de uso precise delas.

### Regras de fronteira

- Módulos de API traduzem aspectos de transporte; não controlam políticas de negócio.
- Casos de uso coordenam uma intenção da aplicação e permanecem neutros a transporte.
- O domínio protege linguagem e invariantes sem importar frameworks.
- Infraestrutura implementa portas e controla detalhes de I/O externo.
- A raiz de composição conecta dependências e ciclo de vida do processo.
- Comunicação entre módulos usa contratos documentados, não detalhes privados.

## Mapa do repositório

```text
atlas/
├── analytics/                      # Scaffold de código analítico reutilizável
├── apps/
│   └── mobile/                     # Scaffold de implementação do Atlas Pocket
├── backend/
│   ├── app/
│   │   ├── api/                    # Scaffold da interface HTTP
│   │   ├── core/                   # Scaffold de settings tipados
│   │   ├── domain/                 # Scaffold do modelo de domínio
│   │   ├── use_cases/              # Scaffold de casos de uso
│   │   ├── database.py             # Configuração SQLAlchemy de desenvolvimento
│   │   └── main.py                 # Aplicação FastAPI atual
│   ├── tests/                      # Testes atuais da API
│   ├── README.md                   # Guia operacional e arquitetural do backend
│   └── requirements.txt            # Ambiente executável fixado do backend
├── docs/
│   ├── modules/                    # Documentação de módulos concretos
│   ├── tracks/                     # 21 guias técnicos de execução
│   └── README.md                   # Central de documentação
├── datasets/                       # Scaffold de governança de datasets
├── infra/                          # Scaffold de infraestrutura e runbooks
├── notebooks/                      # Scaffold de exploração reprodutível
├── requirements/                   # 76 conjuntos focados de dependências
├── scrapers/                       # Scaffold de coleta responsável
├── scripts/
│   └── mobile/                     # Scaffold de automação mobile
├── docker-compose.yml              # Serviço PostgreSQL local
├── LICENSE
├── README.md
└── README.pt-BR.md
```

Diretórios descritos nos roadmaps são planejados e devem ser criados apenas
quando uma implementação real precisar deles.

## Trilhas técnicas

O Atlas possui 21 trilhas técnicas de longo prazo. Cada guia ligado abaixo
contém missão, escopo, entregáveis, dependências, integrações, evidências de
qualidade, roadmap e definição de pronto.

### Fundação e interfaces

- [Atlas Core](docs/tracks/core/README.pt-BR.md)
- [Atlas API](docs/tracks/api/README.pt-BR.md)
- [Legado e Refatoração](docs/tracks/legacy-refactoring/README.pt-BR.md)

### Dados, matemática e inteligência

- [Data Mining](docs/tracks/data-mining/README.pt-BR.md)
- [ETL e Engenharia de Dados](docs/tracks/data-engineering/README.pt-BR.md)
- [Statistical Lab](docs/tracks/statistics/README.pt-BR.md)
- [Cálculo e Métodos Numéricos](docs/tracks/numerical-methods/README.pt-BR.md)
- [Machine Learning](docs/tracks/machine-learning/README.pt-BR.md)
- [Deep Learning](docs/tracks/deep-learning/README.pt-BR.md)
- [AI Lab](docs/tracks/ai/README.pt-BR.md)
- [BI e Storytelling](docs/tracks/bi-storytelling/README.pt-BR.md)

### Operações e sistemas em execução

- [Automação](docs/tracks/automation/README.pt-BR.md)
- [Suporte](docs/tracks/support/README.pt-BR.md)
- [Redes](docs/tracks/networking/README.pt-BR.md)
- [Mensageria e Tempo Real](docs/tracks/messaging-real-time/README.pt-BR.md)
- [Cloud e DevOps](docs/tracks/cloud-devops/README.pt-BR.md)
- [Observabilidade](docs/tracks/observability/README.pt-BR.md)
- [Sistemas](docs/tracks/systems/README.pt-BR.md)

### Dispositivos e aplicações interativas

- [Mobile](docs/tracks/mobile/README.pt-BR.md)
- [Embarcados, IoT e Sistemas Autônomos](docs/tracks/embedded-iot-autonomous/README.pt-BR.md)
- [Jogos e Simulação](docs/tracks/games-simulation/README.pt-BR.md)

Veja o [catálogo completo](docs/tracks/README.pt-BR.md) para definições de
status e navegação.

## Módulos do sistema

O catálogo de módulos documenta unidades concretas de runtime e especificações
de produto. A documentação atual inclui:

- [Backend Atlas](backend/README.pt-BR.md)
- [Pacote da aplicação](backend/app/README.pt-BR.md)
- [Interface de API](backend/app/api/README.pt-BR.md)
- [Rotas da API](backend/app/api/routes/README.pt-BR.md)
- [Configuração core](backend/app/core/README.pt-BR.md)
- [Modelo de domínio](backend/app/domain/README.pt-BR.md)
- [Entidades de domínio](backend/app/domain/entities/README.pt-BR.md)
- [Casos de uso](backend/app/use_cases/README.pt-BR.md)
- [Testes do backend](backend/tests/README.pt-BR.md)
- [Analytics](analytics/README.pt-BR.md)
- [Aplicações clientes](apps/README.pt-BR.md)
- [Implementação do Atlas Pocket](apps/mobile/README.pt-BR.md)
- [Datasets](datasets/README.pt-BR.md)
- [Infraestrutura](infra/README.pt-BR.md)
- [Notebooks](notebooks/README.pt-BR.md)
- [Coleta de dados](scrapers/README.pt-BR.md)
- [Scripts operacionais](scripts/README.pt-BR.md)
- [Scripts de automação mobile](scripts/mobile/README.pt-BR.md)
- [Atlas Mobile Lab](docs/modules/mobile-lab/README.pt-BR.md)

O [catálogo de módulos](docs/modules/README.pt-BR.md) diferencia módulos
implementados, scaffolds parciais e produtos planejados.

## Estratégia de dependências

O Atlas não usa um único `requirements.txt` experimental gigantesco. A pasta
[`requirements/`](requirements/README.pt-BR.md) contém conjuntos focados e sem
pinagem para exploração técnica, enquanto
[`backend/requirements.txt`](backend/requirements.txt) fixa o ambiente atual do
backend.

Instale somente os conjuntos necessários ao trabalho atual:

```bash
python -m pip install -r requirements/core.txt
python -m pip install -r requirements/dev.txt
```

Combine trilhas explicitamente quando um módulo atravessar domínios:

```bash
python -m pip install \
  -r requirements/data.txt \
  -r requirements/statistics.txt \
  -r requirements/visualization.txt
```

Restrições importantes:

- arquivos de trilha não são lock files;
- stacks experimentais podem conflitar e exigir ambientes separados;
- bibliotecas nativas, cloud, device ou IA podem exigir setup e custos externos;
- listar uma dependência não prova que sua funcionalidade está implementada;
- módulos devem declarar exatamente quais trilhas consomem.

## Início rápido

### Pré-requisitos

- Git;
- Python 3.11 ou mais recente;
- Docker com suporte a Compose;
- PowerShell, Bash ou shell equivalente.

### 1. Clonar e entrar no repositório

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas
```

### 2. Criar e ativar um ambiente virtual

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Bash:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar o ambiente do backend

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

### 4. Iniciar o PostgreSQL

```bash
docker compose up -d postgres
docker compose ps
```

As credenciais do Compose são defaults de desenvolvimento local. Nunca as
reutilize em ambiente compartilhado ou de produção.

### 5. Executar os testes

```bash
cd backend
python -m pytest
```

### 6. Iniciar a API

```bash
python -m uvicorn app.main:app --reload
```

Abra `http://127.0.0.1:8000/docs` para a interface OpenAPI. Consulte o
[guia do backend](backend/README.pt-BR.md) para arquitetura, limitações de
configuração e próximos passos.

## Comportamento da API

| Método | Path | Resposta atual | Significado |
|---|---|---|---|
| `GET` | `/` | `{"message":"Atlas conectado"}` | Resposta básica do processo |
| `GET` | `/health` | `{"status":"ok"}` | Apenas liveness do processo |
| `GET` | `/version` | `{"name":"Atlas API","version":"0.1.0"}` | Identidade atual da API |

`/health` não verifica PostgreSQL ou outras dependências. Um futuro endpoint de
readiness deve representar separadamente a disponibilidade das dependências.

## Fluxo de desenvolvimento

1. Escolha uma trilha documentada e um critério de aceitação pequeno.
2. Confirme o estado real do repositório antes de desenhar abstrações.
3. Adicione ou atualize testes para comportamento observável.
4. Implemente a menor fatia vertical que satisfaça o critério.
5. Mantenha regras de domínio separadas de entrega e infraestrutura.
6. Execute testes focados e depois a suíte relevante mais ampla.
7. Atualize documentação em inglês e português na mesma alteração.
8. Registre ADR quando a decisão atravessar fronteiras ou for cara de reverter.
9. Revise segurança, privacidade, falhas e evidências operacionais.

Definição de pronto para uma mudança de módulo:

- instruções de setup limpo funcionam;
- contratos públicos e erros estão documentados;
- testes são proporcionais ao risco;
- nenhum secret ou dado pessoal é versionado;
- comportamento planejado e implementado estão separados;
- READMEs de trilhas e módulos permanecem alinhados.

## Testes e qualidade

O projeto usa pytest para as checagens atuais do backend. Com o crescimento da
arquitetura, a qualidade deve ser organizada em camadas:

| Camada | Finalidade |
|---|---|
| Unitária | Invariantes, cálculos, transformações e decisões de casos de uso |
| Contrato | Schemas HTTP, status, erros, eventos, arquivos e provedores |
| Integração | PostgreSQL, migrações, filas, arquivos e provedores controlados |
| Ponta a ponta | Poucas jornadas críticas atravessando fronteiras reais |
| Arquitetura | Direção de dependências e imports proibidos de frameworks |
| Operacional | Saúde, readiness, telemetria, rollback e recuperação |

Qualidade não é medida apenas por percentual de cobertura. Testes devem detectar
regressões relevantes, permanecer determinísticos e explicar falhas. Experimentos
de dados e IA também precisam de entradas e seeds versionadas, métricas de
avaliação, comparação com baselines e registro de limitações.

## Sistema de documentação

A [central de documentação](docs/README.pt-BR.md) define tipos de documentos,
regras de fonte da verdade, política bilíngue, padrão de escrita e checklist de
revisão.

A documentação principal é mantida em pares:

- `README.md` — inglês;
- `README.pt-BR.md` — português brasileiro.

As duas versões devem possuir estrutura e sentido técnico equivalentes. Nomes
técnicos permanecem canônicos e as explicações são localizadas. Trabalho
planejado deve ser marcado claramente; afirmações de implementação devem apontar
para código, testes, exemplos ou evidência operacional.

## Roadmap

### Fase 0 — Fundação

- estabilizar setup e testes do backend;
- completar configuração tipada;
- extrair routers versionados;
- completar o ADR 0001;
- implementar a primeira fatia de domínio.

### Fase 1 — Fundação de dados

- registrar e catalogar fontes de dados;
- adicionar migrações e adapters de repository;
- coletar um dataset público de forma responsável;
- criar pipeline reprodutível de raw para processed;
- publicar evidências de qualidade e linhagem.

### Fase 2 — Analytics e estatística

- definir um dicionário de métricas;
- publicar análises exploratórias e inferenciais;
- adicionar regressão, Bayes ou séries temporais;
- produzir relatório e dashboard reprodutíveis.

### Fase 3 — Machine learning

- estabelecer baselines estatísticos e ingênuos;
- construir um pipeline sem leakage;
- rastrear experimentos e produzir model card;
- expor inferência aprovada por adapter estável.

### Fase 4 — IA e documentos

- ingerir documentos com proveniência;
- construir recuperação com citações;
- definir dataset de avaliação;
- adicionar ferramentas controladas por políticas e agentes observáveis.

### Fase 5 — Automação e operações

- adicionar workflows agendados e orientados a eventos;
- introduzir logs estruturados, métricas e correlation IDs;
- escrever runbooks para falhas relevantes;
- testar retry, idempotência, rollback e recuperação.

### Fase 6 — Interfaces e edge

- criar a primeira tela de saúde do Atlas Pocket;
- adicionar comportamento offline-first de forma incremental;
- prototipar clientes de suporte, IoT ou simulação;
- medir restrições de dispositivo, rede e recursos.

### Fase 7 — Distribuição seletiva

- medir gargalos no monólito modular;
- extrair worker ou serviço somente quando justificado;
- preservar contratos, observabilidade e rollback;
- documentar a decisão e as evidências de migração.

## Uso responsável

### Dados e coleta

- respeitar termos da fonte, robots, rate limits e legislação aplicável;
- coletar apenas o mínimo necessário para a finalidade declarada;
- registrar proveniência, timestamps, transformações e regras de exclusão;
- nunca publicar dados privados, pessoais ou sensíveis no portfólio.

### IA e automação

- identificar conteúdo gerado por modelos e preservar rastreabilidade de fontes;
- avaliar recuperação e respostas antes de confiar nelas;
- conceder às ferramentas o menor privilégio necessário;
- exigir aprovação explícita para ações destrutivas ou com efeito externo;
- acompanhar custo, latência, fallback e regras de dados dos provedores.

### Suporte, redes e dispositivos

- usar diagnóstico somente leitura por padrão;
- definir escopo e autorização antes de varredura ou acesso remoto;
- separar evidência, inferência e correção;
- registrar mudanças e oferecer rollback quando houver modificação;
- tratar ações físicas e industriais como sensíveis à segurança.

### Segurança

- nunca versionar secrets ou credenciais de produção;
- validar entrada não confiável nas fronteiras;
- remover dados sensíveis de logs e erros;
- usar menor privilégio e timeouts explícitos;
- manter dependências e procedimentos de deploy revisáveis.

## Evidências de portfólio

Cada fatia concluída do Atlas deve responder:

- Qual problema real foi tratado?
- Quais restrições e tradeoffs orientaram o design?
- Qual contrato a separa de outros módulos?
- Como outra pessoa pode executar e verificar o resultado?
- Quais testes, métricas ou comparações sustentam a conclusão?
- O que falhou, mudou ou continua limitado?
- O que justificaria o próximo passo arquitetural?

Boas evidências incluem código, testes, diagramas, ADRs, dataset cards, model
cards, benchmarks, screenshots, dashboards, runbooks e demos curtas. O objetivo
não é amplitude máxima, mas progressão técnica confiável.

## Licença

O Atlas é licenciado sob a [Licença MIT](LICENSE).

## Autor

**Caio Costa Cavalcante**

Estudante de Estatística, estudante de ciência de dados, desenvolvedor de IA e
Python, desenvolvedor Android e profissional de suporte/helpdesk construindo o
Atlas como portfólio técnico de longo prazo.

GitHub: [caio-stat](https://github.com/caio-stat)
