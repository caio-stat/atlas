# Atlas Laboratório de Mensageria e Tempo Real

> Filas, eventos, streams, workers em background e interfaces ao vivo.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

Esta trilha estuda acoplamento temporal e garantias de entrega. Escolhas tecnológicas devem seguir necessidades da carga, como ordenação, throughput, latência, durabilidade, replay e complexidade operacional.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Filas de trabalho e workers em background
- Mensageria publish/subscribe
- Streams de eventos e replay
- WebSockets e Server-Sent Events
- Acesso assíncrono a APIs e bancos
- Agendamento e entrega atrasada
- Semântica de entrega, idempotência e backpressure

## Entregáveis de referência

- Um job em background com retry e dead letter
- Um feed de status por pub/sub
- Um endpoint WebSocket ou SSE em FastAPI
- Um pequeno benchmark de streaming de eventos
- Um dashboard ao vivo de monitoramento de pipelines

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`messaging.txt`](../../../requirements/messaging.txt)
- [`real_time.txt`](../../../requirements/real_time.txt)
- [`real_time_dashboard.txt`](../../../requirements/real_time_dashboard.txt)
- [`async_programming.txt`](../../../requirements/async_programming.txt)
- [`concurrency.txt`](../../../requirements/concurrency.txt)

## Integração com o Atlas

- Desacopla cargas de Automação e Engenharia de Dados
- Alimenta atualizações ao vivo da API e de BI
- Exporta métricas de filas e consumidores para Observabilidade

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras externas.
- Dados, seeds e configuração versionados quando necessários.
- Métricas técnicas e de produto adequadas ao experimento.
- README, exemplos e limitações atualizados junto ao código.
- Nenhum segredo ou dado pessoal versionado.

## Roadmap incremental

### 1. Fundação

Definir glossário, caso de uso inicial, contrato e teste mínimo.

### 2. Protótipo aplicado

Executar um caso real com dados ou infraestrutura controlados.

### 3. Integração

Conectar o resultado a outro módulo por contrato explícito.

### 4. Maturidade

Adicionar observabilidade, documentação operacional e avaliação de riscos.

## Definição de pronto

- O caso de uso principal executa a partir de instruções limpas.
- Os comportamentos relevantes possuem testes proporcionais ao risco.
- Entradas, saídas, erros e limitações estão documentados.
- As dependências pertencem às trilhas declaradas.
- A integração respeita as fronteiras do Atlas.
- Existe uma demonstração curta para revisão técnica.

## Status

Trilha planejada. A documentação define o contrato de evolução; a implementação deve avançar incrementalmente e refletir o estado real do repositório.
