# Atlas Observability Lab

> Logs, métricas, traces, sinais de saúde e compreensão operacional.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Observability Lab torna o comportamento do sistema explicável antes dos incidentes. A telemetria deve responder perguntas operacionais concretas, preservar contexto entre fronteiras e evitar exposição de secrets ou dados pessoais.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Logging estruturado de aplicações
- Métricas e indicadores de nível de serviço
- Tracing distribuído e correlação
- Checagens de saúde, prontidão e dependências
- Dashboards e alertas acionáveis
- Relato de erros e contexto de incidentes
- Resiliência, injeção de falhas e evidência de recuperação

## Entregáveis de referência

- Logs estruturados da API com correlation IDs
- Um endpoint de métricas Prometheus
- Um dashboard de saúde de serviços
- Um alerta associado a um runbook
- Um relatório de injeção de falha e recuperação

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`observability.txt`](../../../requirements/observability.txt)
- [`resilience.txt`](../../../requirements/resilience.txt)
- [`self_healing.txt`](../../../requirements/self_healing.txt)
- [`safety_testing.txt`](../../../requirements/safety_testing.txt)

## Integração com o Atlas

- Recebe telemetria de todos os módulos em execução
- Apoia diagnóstico de incidentes pelo Support Lab
- Orienta confiabilidade nas trilhas Cloud e Tempo Real

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
