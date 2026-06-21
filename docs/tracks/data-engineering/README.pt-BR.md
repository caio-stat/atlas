# Atlas ETL e Engenharia de Dados

> Pipelines reprodutíveis de ingestão, transformação, armazenamento e qualidade de dados.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

Esta trilha cuida do caminho entre ativos brutos e datasets analíticos confiáveis. Os pipelines devem ser reexecutáveis, observáveis, conscientes de schema e explícitos sobre linhagem e expectativas de qualidade.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes que possam integrar o ecossistema sem acoplamento desnecessário.
- Produzir material de portfólio que explique tanto o resultado quanto o raciocínio.

## Escopo técnico

- Ingestão batch e incremental
- Validação e evolução de schemas
- Modelagem SQL e migrações
- Limpeza e normalização de dados
- Linhagem, particionamento e retenção
- Checagens de qualidade e quarentena
- Armazenamento analítico local e padrões de warehouse

## Entregáveis de referência

- Templates de pipeline de raw para processed
- Persistência de fontes de dados em PostgreSQL
- Exemplos analíticos com DuckDB
- Relatórios de qualidade com motivos de rejeição
- Um contrato de dataset documentado

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis a dependências globais.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`data.txt`](../../../requirements/data.txt)
- [`data_engineering.txt`](../../../requirements/data_engineering.txt)
- [`big_data.txt`](../../../requirements/big_data.txt)
- [`cloud.txt`](../../../requirements/cloud.txt)

## Integração com o Atlas

- Consome saídas de Data Mining
- Abastece Estatística, ML, BI e IA
- Publica sinais de execução para Mensageria e Observabilidade

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras com banco, rede, arquivos ou provedores.
- Dados, seeds e configuração versionados quando a reprodução depender deles.
- Métricas técnicas e de produto adequadas ao experimento.
- README, exemplos de uso e registro de limitações atualizados junto ao código.
- Nenhum segredo, dado pessoal ou artefato pesado versionado sem justificativa.

## Roadmap incremental

### 1. Fundação

Definir glossário, caso de uso inicial, contrato e teste mínimo.

### 2. Protótipo aplicado

Executar um caso real com dados ou infraestrutura controlados.

### 3. Integração

Conectar o resultado a pelo menos outro módulo por contrato explícito.

### 4. Maturidade

Adicionar observabilidade, documentação operacional e avaliação de riscos.

## Definição de pronto

- O caso de uso principal pode ser executado a partir de instruções limpas.
- Os comportamentos relevantes possuem testes proporcionais ao risco.
- Entradas, saídas, erros e limitações estão documentados.
- As dependências utilizadas pertencem às trilhas declaradas.
- A integração não viola as fronteiras arquiteturais do Atlas.
- Existe uma demonstração curta e compreensível para revisão técnica.

## Status

Trilha planejada. A documentação define o contrato de evolução; implementações devem ser adicionadas incrementalmente e refletir o estado real do repositório.
