# Atlas Mobile Lab

> Guia de produto e arquitetura para o Atlas Pocket e futuros clientes de suporte em campo.

[English](README.md) | **Português**

[Catálogo de módulos](../README.pt-BR.md) · [Trilha Mobile](../../tracks/mobile/README.pt-BR.md) · [README do projeto](../../../README.pt-BR.md)

## Estado atual

O Mobile Lab está **especificado, mas não implementado**. O repositório contém
um estudo detalhado da stack em [`stack.md`](stack.md), mas ainda não possui um
diretório de aplicação Android nem configuração de build. A primeira
implementação deve, portanto, permanecer deliberadamente pequena.

## Direção de produto

A aplicação principal planejada é o **Atlas Pocket**, um cliente Android que se
conecta aos serviços do Atlas e continua útil sob conectividade intermitente.
Sua primeira responsabilidade será mostrar saúde e versão do backend. Versões
posteriores poderão adicionar datasets, relatórios, alertas, suporte em campo,
captura de documentos, QR Codes e recursos assistidos por IA.

## Primeira fatia vertical

A primeira entrega deve:

1. criar um projeto Android em Kotlin;
2. renderizar uma tela de status em Jetpack Compose;
3. chamar `GET /health` e `GET /version` por Retrofit/OkHttp;
4. representar estados de carregamento, online, offline, timeout e resposta inválida;
5. expor a URL-base da API por configuração de desenvolvimento;
6. incluir testes unitários e pelo menos um smoke test de integração ou UI;
7. documentar configuração de emulador e dispositivo físico.

Ela não deve adicionar autenticação, Room, sincronização em background, push,
câmera ou ML embarcado antes que essa primeira fatia seja confiável.

## Arquitetura planejada

```text
Compose UI
    ↓
ViewModel
    ↓
Casos de uso
    ↓
Repository
    ├── Remote data source → Atlas API
    └── Local data source  → Room / DataStore
```

A aplicação deve se comunicar com o Atlas por contratos da API. Ela nunca deve
se conectar diretamente ao PostgreSQL remoto.

## Roadmap de capacidades

### Fase 1 — Conexão com a API

- tela de saúde e versão;
- tratamento de estados de rede;
- testes automatizados básicos.

### Fase 2 — Fundação offline-first

- cache Room e preferências DataStore;
- estado explícito de sincronização;
- jobs WorkManager com retry seguro.

### Fase 3 — Dados e relatórios

- resumos de datasets e indicadores;
- relatórios em cache;
- gráficos acessíveis para telas pequenas.

### Fase 4 — Suporte em campo

- checklist de atendimento;
- cadastro e fotografias de equipamentos;
- identificação por QR Code;
- registros offline e sincronização posterior.

### Fase 5 — Capacidades de IA

- chat com agente remoto e estado de conectividade transparente;
- resumos de documentos e respostas com fontes;
- OCR aprovado ou modelos leves no dispositivo.

## Requisitos de qualidade

- O comportamento offline é projetado, não tratado como exceção.
- Conflitos e retries de sincronização possuem estados explícitos.
- Dados sensíveis são minimizados e protegidos em repouso e trânsito.
- Acessibilidade cobre rótulos, contraste, texto escalável e áreas de toque.
- Chamadas de rede possuem timeouts e erros observáveis.
- Testes mobile cobrem domínio, repositories e fluxos críticos de UI.
- Bateria, armazenamento, banda e tamanho de modelo são medidos antes da IA mobile.

## Ferramentas de apoio em Python

Python continua útil para testes Appium, automação ADB, coleta de screenshots,
geração de QR, checagens de contrato da API e relatórios HTML. Essas ferramentas
apoiam o cliente Android; não substituem a arquitetura da aplicação Kotlin.

Arquivos de dependências relevantes:

- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Definição de pronto da primeira entrega

- Um clone limpo consegue compilar e abrir o app pelas instruções documentadas.
- A tela representa corretamente chamadas bem-sucedidas e falhas da API.
- Os testes executam localmente e no ambiente CI escolhido.
- Nenhum secret de produção ou endpoint privado fixo é versionado.
- O README reflete as telas e a arquitetura realmente implementadas.
