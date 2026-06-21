# Módulos do sistema Atlas

> Documentação dos módulos executáveis e das especificações concretas de produto.

[English](README.md) | **Português**

[Central de documentação](../README.pt-BR.md) · [Trilhas técnicas](../tracks/README.pt-BR.md) · [README do projeto](../../README.pt-BR.md)

## Catálogo

| Módulo | Papel | Estado da implementação | Documentação |
|---|---|---|---|
| Backend Atlas | Aplicação FastAPI e fundação PostgreSQL | Endpoints iniciais e scaffold de conexão | [Backend](../../backend/README.pt-BR.md) |
| Pacote da aplicação | Composição de API, core, domínio e casos de uso | Scaffold parcial | [Aplicação](../../backend/app/README.pt-BR.md) |
| Interface de API | Transporte HTTP e organização de rotas | Rotas iniciais ainda em `main.py` | [API](../../backend/app/api/README.pt-BR.md) |
| Configuração core | Settings e primitivas transversais da aplicação | Scaffold vazio | [Core](../../backend/app/core/README.pt-BR.md) |
| Modelo de domínio | Entidades de negócio e invariantes | Scaffold vazio | [Domínio](../../backend/app/domain/README.pt-BR.md) |
| Casos de uso | Orquestração da aplicação | Scaffold vazio | [Casos de uso](../../backend/app/use_cases/README.pt-BR.md) |
| Testes do backend | Checagens executáveis do comportamento da API | Testes de saúde e versão | [Testes](../../backend/tests/README.pt-BR.md) |
| Analytics | Código reutilizável de estatística, avaliação de ML e relatórios | Scaffold vazio | [Analytics](../../analytics/README.pt-BR.md) |
| Aplicações clientes | Contêiner para interfaces implantáveis | Scaffold vazio | [Aplicações](../../apps/README.pt-BR.md) |
| Aplicação Android | Local de implementação do Atlas Pocket | Scaffold vazio | [Aplicação mobile](../../apps/mobile/README.pt-BR.md) |
| Datasets | Amostras, metadados, proveniência e schemas | Scaffold vazio | [Datasets](../../datasets/README.pt-BR.md) |
| Infraestrutura | Ambientes, deploy, telemetria e runbooks | Scaffold vazio | [Infraestrutura](../../infra/README.pt-BR.md) |
| Notebooks | Exploração reprodutível e narrativas analíticas | Scaffold vazio | [Notebooks](../../notebooks/README.pt-BR.md) |
| Coleta de dados | Adapters responsáveis para web, documentos e dados públicos | Scaffold vazio | [Scrapers](../../scrapers/README.pt-BR.md) |
| Scripts operacionais | Entradas enxutas para tarefas repetíveis | Scaffold vazio | [Scripts](../../scripts/README.pt-BR.md) |
| Automação mobile | Helpers ADB, Appium, fixtures, logs e smoke tests | Scaffold vazio | [Scripts mobile](../../scripts/mobile/README.pt-BR.md) |
| Atlas Mobile Lab | Especificação do Atlas Pocket e clientes de campo | Planejado; stack documentada | [Mobile Lab](mobile-lab/README.pt-BR.md) |

## Contrato de documentação de módulos

Cada módulo implementado deve documentar:

- sua responsabilidade e suas não responsabilidades explícitas;
- funções, endpoints, mensagens, arquivos ou schemas públicos;
- dependências e configuração;
- fluxo de execução e comportamento de falha;
- comandos para execução e verificação local;
- estratégia de testes e limites atuais de cobertura;
- aspectos de segurança, privacidade, consentimento, acessibilidade e operação;
- o impacto humano e social esperado do módulo, incluindo justiça, transparência e bem-estar;
- regras de extensão e limitações conhecidas;
- status de implementação apoiado por evidência do repositório.

## Relação com as trilhas

Trilhas definem áreas duradouras de aprendizagem e desenvolvimento de produto.
Módulos são unidades concretas que implementam parte de uma ou mais trilhas. O
backend, por exemplo, implementa partes de Atlas Core, Atlas API, Engenharia de
Dados, Cloud/DevOps e Observabilidade. Um módulo pode servir várias trilhas, mas
deve possuir uma responsabilidade clara em runtime.

## Regra de status

Um pacote vazio é um scaffold, não um módulo implementado. A documentação pode
descrever sua fronteira pretendida, mas o status precisa continuar explícito até
existirem código, testes e um exemplo executável.
