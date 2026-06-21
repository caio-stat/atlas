# Atlas Laboratório de Cloud e DevOps

> Ambientes repetíveis, experimentos cloud, automação de entrega e operações conscientes de custo.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Laboratório de Cloud e DevOps evolui o Atlas da execução local para entregas repetíveis. A infraestrutura deve ser revisável, de menor privilégio, observável, limitada em custo e removível sem deixar recursos não documentados.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Ambientes Docker e Compose
- Experimentos com SDKs cloud e cloud local
- Infraestrutura como código
- CI/CD e quality gates
- Gestão de secrets e ambientes
- Deploy, rollback e zero downtime
- Tags de custo, orçamentos e limpeza

## Entregáveis de referência

- Uma stack local de desenvolvimento reprodutível
- Um pipeline CI para testes e análise estática
- Um exercício com LocalStack ou sandbox cloud
- Um plano de infraestrutura com passos de teardown
- Um runbook de deploy e rollback

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`cloud.txt`](../../../requirements/cloud.txt)
- [`aws.txt`](../../../requirements/aws.txt)
- [`cloud_orchestration.txt`](../../../requirements/cloud_orchestration.txt)
- [`devops.txt`](../../../requirements/devops.txt)
- [`zero_downtime.txt`](../../../requirements/zero_downtime.txt)
- [`security.txt`](../../../requirements/security.txt)

## Integração com o Atlas

- Hospeda a Atlas API e serviços de dados
- Fornece ambientes para toda trilha executável
- Disponibiliza metadados de deploy à Observabilidade

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
