# Backend Atlas

> Fundação FastAPI e PostgreSQL para as primeiras fatias verticais executáveis do Atlas.

[English](README.md) | **Português**

[README do projeto](../README.pt-BR.md) · [Catálogo de módulos](../docs/modules/README.pt-BR.md) · [Trilha da API](../docs/tracks/api/README.pt-BR.md)

## Estado atual

O backend é uma fundação inicial, não um monólito modular completo. Atualmente
ele oferece uma aplicação FastAPI com três endpoints síncronos, uma engine
SQLAlchemy configurada para o container PostgreSQL local e dois testes de API.
Vários pacotes existem como scaffolds vazios para a arquitetura pretendida.

Implementado hoje:

- `GET /` retorna `{"message": "Atlas conectado"}`;
- `GET /health` retorna `{"status": "ok"}`;
- `GET /version` retorna o nome da API e a versão `0.1.0`;
- SQLAlchemy expõe `engine` e `SessionLocal`;
- pytest verifica as respostas de saúde e versão;
- Docker Compose define o serviço PostgreSQL local.

Ainda não implementado:

- rotas com banco ou dependência de sessão;
- settings tipados em `app/core/config.py`;
- entidade de domínio `DataSource`;
- caso de uso `register_data_source`;
- routers versionados em `app/api/routes`;
- migrações, autenticação, logging estruturado, readiness ou métricas;
- ADR completo sobre o monólito modular.

## Mapa de diretórios

```text
backend/
├── app/
│   ├── api/
│   │   └── routes/                 # Módulos planejados de rotas HTTP
│   ├── core/                       # Settings e primitivas transversais planejados
│   ├── domain/
│   │   └── entities/               # Entidades de domínio planejadas
│   ├── use_cases/                  # Casos de uso planejados
│   ├── database.py                 # Engine e factory de sessões atuais
│   └── main.py                     # Aplicação FastAPI e endpoints atuais
├── tests/
│   └── test_health.py              # Testes atuais do comportamento da API
├── 0001-monolito-modular.md        # Placeholder de ADR; atualmente vazio
├── pytest.ini
└── requirements.txt                # Ambiente fixado do backend
```

Documentação detalhada dos módulos:

- [Pacote da aplicação](app/README.pt-BR.md)
- [Interface de API](app/api/README.pt-BR.md)
- [Módulos de rotas](app/api/routes/README.pt-BR.md)
- [Configuração core](app/core/README.pt-BR.md)
- [Domínio](app/domain/README.pt-BR.md)
- [Entidades de domínio](app/domain/entities/README.pt-BR.md)
- [Casos de uso](app/use_cases/README.pt-BR.md)
- [Testes](tests/README.pt-BR.md)

## Configuração local

Execute os comandos a partir da raiz do repositório, exceto quando indicado.

### 1. Criar e ativar o ambiente virtual

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

### 2. Instalar dependências do backend

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

### 3. Iniciar o PostgreSQL

```bash
docker compose up -d postgres
docker compose ps
```

O serviço de desenvolvimento usa banco `atlas_db`, usuário `atlas`, senha
`atlas123` e porta `5432`. Essas credenciais servem apenas ao desenvolvimento
local e não devem ser reutilizadas em ambientes compartilhados ou de produção.

### 4. Iniciar a API

```bash
cd backend
python -m uvicorn app.main:app --reload
```

URLs úteis:

- raiz: `http://127.0.0.1:8000/`
- saúde: `http://127.0.0.1:8000/health`
- versão: `http://127.0.0.1:8000/version`
- OpenAPI UI: `http://127.0.0.1:8000/docs`

### 5. Executar os testes

A partir de `backend/`:

```bash
python -m pytest
```

## Fluxo de requisição atual

```text
Requisição HTTP
    ↓
Aplicação FastAPI em app/main.py
    ↓
Função de rota
    ↓
Resposta JSON estática
```

O módulo de banco é independente e não participa do fluxo atual dos endpoints.
A documentação não deve sugerir que `/health` verifica o PostgreSQL antes da
implementação de uma checagem de readiness.

## Fluxo de requisição pretendido

```text
Requisição HTTP
    ↓
Router da API e validação
    ↓
Caso de uso
    ↓
Regras de domínio
    ↓
Porta
    ↓
Adapter SQLAlchemy ou de serviço externo
```

Esse fluxo é uma direção, não o estado atual. A primeira migração útil é extrair
os endpoints para routers sem adicionar abstração desnecessária e, em seguida,
implementar um caso de uso completo para fontes de dados.

## Configuração

`app/database.py` contém hoje uma URL de desenvolvimento fixa:

```text
postgresql://atlas:atlas123@localhost:5432/atlas_db
```

O próximo passo é movê-la para settings tipados e alimentados por ambiente em
`app/core/config.py`. Os settings esperados incluem ambiente, versão da API,
URL do banco, nível de log e flags opcionais de telemetria. Defaults podem
atender ao ambiente local, mas secrets devem vir do ambiente ou de um gerenciador.

## Estratégia de testes

Os testes existentes usam `TestClient` do FastAPI e validam status e corpo da
resposta. Com o crescimento do comportamento, separe os testes por finalidade:

- testes unitários para entidades e casos de uso sem FastAPI ou PostgreSQL;
- testes de contrato para validação, status e formato de erros;
- testes de integração para repositories SQLAlchemy e migrações;
- testes de readiness para dependências externas;
- testes arquiteturais para direção de dependências.

Os testes devem verificar comportamento observável, não detalhes internos do framework.

## Segurança e operação

- Trate as credenciais do Compose como exclusivamente locais.
- Nunca versione URLs de produção, tokens ou dados pessoais.
- Adicione timeouts e falhas explícitas nas fronteiras externas.
- Mantenha `/health` barato e local ao processo; use `/ready` para dependências.
- Remova credenciais e payloads sensíveis dos logs.
- Adicione correlation IDs antes de atravessar filas ou serviços externos.
- Defina migração e rollback antes da evolução de schemas persistentes.

## Próxima fatia de implementação

1. Adicionar settings tipados por ambiente.
2. Extrair handlers de saúde e versão para um router.
3. Definir uma entidade mínima `DataSource` com invariantes explícitas.
4. Definir uma porta de repository e o caso de uso `register_data_source`.
5. Implementar adapter SQLAlchemy e migração.
6. Expor uma rota versionada com testes unitários e de integração.
7. Completar o ADR 0001 com contexto, decisão, alternativas e consequências.

## Definição de pronto do marco de fundação

- Um clone limpo inicia PostgreSQL e API pelos comandos documentados.
- `/health`, `/version` e a primeira rota de domínio possuem testes.
- A configuração do banco vem de settings tipados.
- Mudanças de schema usam migração reprodutível.
- Testes de domínio e casos de uso não exigem FastAPI ou PostgreSQL.
- Logs possuem correlação sem expor secrets.
- A documentação em inglês e português corresponde ao comportamento implementado.
