# Trilhas técnicas do Atlas

> Guias detalhados de execução para os domínios de aprendizagem e implementação que compõem o Atlas.

[English](README.md) | **Português**

[Central de documentação](../README.pt-BR.md) · [README do projeto](../../README.pt-BR.md) · [Catálogo de dependências](../../requirements/README.pt-BR.md)

## Como usar este catálogo

Cada README de trilha define missão, escopo técnico, entregáveis de referência,
arquivos de dependências, fronteiras de integração, evidências de qualidade,
roadmap incremental e definição de pronto. Uma trilha é uma direção de produto,
não uma afirmação de que todas as capacidades listadas já existem.

Use o catálogo nesta ordem:

1. Escolha uma trilha e um entregável pequeno.
2. Instale somente os arquivos de dependências declarados.
3. Construa uma fatia vertical com testes e documentação.
4. Integre por contratos explícitos com outro módulo do Atlas.
5. Atualize status e evidências quando a implementação mudar.

## Fundação e interfaces

| Trilha | Responsabilidade | Estado atual |
|---|---|---|
| [Atlas Core](core/README.pt-BR.md) | Linguagem de domínio, casos de uso e contratos compartilhados | Scaffold de fundação |
| [Atlas API](api/README.pt-BR.md) | Contratos HTTP e composição da aplicação | Endpoints iniciais disponíveis |
| [Legado e Refatoração](legacy-refactoring/README.pt-BR.md) | Modernização segura e evidência de dívida técnica | Planejada |

## Dados, matemática e inteligência

| Trilha | Responsabilidade | Estado atual |
|---|---|---|
| [Data Mining](data-mining/README.pt-BR.md) | Coleta responsável, scraping, OCR e documentos | Planejada |
| [ETL e Engenharia de Dados](data-engineering/README.pt-BR.md) | Ingestão, armazenamento, linhagem e qualidade | Scaffold de fundação |
| [Statistical Lab](statistics/README.pt-BR.md) | Inferência, incerteza, regressão e previsão | Planejada |
| [Cálculo e Métodos Numéricos](numerical-methods/README.pt-BR.md) | Confiabilidade numérica, otimização e simulação | Planejada |
| [Machine Learning](machine-learning/README.pt-BR.md) | ML clássico e avaliação reprodutível | Planejada |
| [Deep Learning](deep-learning/README.pt-BR.md) | Modelos neurais e treinamento responsável | Planejada |
| [AI Lab](ai/README.pt-BR.md) | RAG, LLMs, agentes, ferramentas e políticas | Planejada |
| [BI e Storytelling](bi-storytelling/README.pt-BR.md) | Métricas, dashboards, relatórios e comunicação | Planejada |

## Operações e sistemas em execução

| Trilha | Responsabilidade | Estado atual |
|---|---|---|
| [Automação](automation/README.pt-BR.md) | Workflows agendados, orientados a eventos e operacionais | Planejada |
| [Suporte](support/README.pt-BR.md) | Diagnóstico, inventário e evidência de helpdesk | Planejada |
| [Redes](networking/README.pt-BR.md) | Diagnóstico de conectividade e experimentos de protocolos | Planejada |
| [Mensageria e Tempo Real](messaging-real-time/README.pt-BR.md) | Filas, streams, workers e interfaces ao vivo | Planejada |
| [Cloud e DevOps](cloud-devops/README.pt-BR.md) | Ambientes, entrega, cloud e infraestrutura | Fundação local com Compose |
| [Observabilidade](observability/README.pt-BR.md) | Logs, métricas, traces e entendimento operacional | Planejada |
| [Sistemas](systems/README.pt-BR.md) | Concorrência, distribuição, segurança e resiliência | Planejada |

## Dispositivos e aplicações interativas

| Trilha | Responsabilidade | Estado atual |
|---|---|---|
| [Mobile](mobile/README.pt-BR.md) | Atlas Pocket, clientes offline-first e IA mobile | Stack especificada |
| [Embarcados, IoT e Sistemas Autônomos](embedded-iot-autonomous/README.pt-BR.md) | Dispositivos, protocolos, controle e edge | Planejada |
| [Jogos e Simulação](games-simulation/README.pt-BR.md) | Simulações interativas, agentes e telemetria | Planejada |

## Vocabulário de status

- **Planejada:** o escopo está documentado, mas não existe implementação representativa.
- **Scaffold de fundação:** há código ou estrutura de apoio, mas a primeira fatia completa está incompleta.
- **Protótipo:** uma fatia vertical executável demonstra a trilha.
- **Integrada:** a trilha se comunica com outro módulo por contrato testado.
- **Operacional:** existem runbooks, telemetria, checagens de confiabilidade e responsabilidade de manutenção.

## Regra de documentação

Os documentos devem permanecer honestos. Arquiteturas planejadas precisam ser
identificadas como planejadas; comportamentos implementados devem apontar para
código, testes, exemplos ou evidências operacionais. Quando uma trilha ganhar
código, coloque o README do módulo perto da implementação e conecte-o a este catálogo.
