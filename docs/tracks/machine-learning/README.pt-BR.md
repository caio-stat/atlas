# Atlas Machine Learning Lab

> Experimentos reprodutíveis de machine learning clássico e avaliação de modelos.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Machine Learning Lab transforma datasets curados em experimentos preditivos mensurados. Baselines, prevenção de leakage, proveniência de features, validação cruzada e reprodutibilidade importam mais que métricas chamativas.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes que possam integrar o ecossistema sem acoplamento desnecessário.
- Produzir material de portfólio que explique tanto o resultado quanto o raciocínio.

## Escopo técnico

- Classificação e regressão supervisionadas
- Clustering e redução de dimensionalidade
- Engenharia e seleção de features
- Validação cruzada e desenho de métricas
- Desbalanceamento e calibração
- Otimização de hiperparâmetros
- Rastreamento de experimentos e empacotamento de modelos

## Entregáveis de referência

- Um template de experimento orientado a baseline
- Um pipeline de classificação com checagens de leakage
- Um benchmark de regressão com análise de resíduos
- Experimentos rastreados e model cards
- Um adapter de inferência com contrato estável

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis a dependências globais.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`ml.txt`](../../../requirements/ml.txt)
- [`data.txt`](../../../requirements/data.txt)
- [`statistics.txt`](../../../requirements/statistics.txt)
- [`mlops.txt`](../../../requirements/mlops.txt)

## Integração com o Atlas

- Consome datasets analíticos versionados
- Compara resultados com baselines do Statistical Lab
- Expõe inferência aprovada pela Atlas API

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
