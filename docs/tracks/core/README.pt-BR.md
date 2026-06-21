# Atlas Core

> A fundação de domínio e aplicação compartilhada pelo ecossistema Atlas.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Atlas Core concentra os conceitos que devem permanecer estáveis enquanto interfaces, bancos, provedores e experimentos evoluem. É o lugar da linguagem de negócio, dos casos de uso explícitos, dos contratos compartilhados e de pequenas primitivas arquiteturais — não um depósito de helpers genéricos.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes que possam integrar o ecossistema sem acoplamento desnecessário.
- Produzir material de portfólio que explique tanto o resultado quanto o raciocínio.

## Escopo técnico

- Entidades de domínio e objetos de valor
- Casos de uso e portas da aplicação
- Schemas compartilhados e regras de validação
- Fronteiras de configuração e erros tipados
- Contratos de plugins e pontos de extensão
- Identificadores entre módulos e regras de ciclo de vida

## Entregáveis de referência

- Um modelo mínimo de domínio para fontes de dados
- Casos de uso de registro e catálogo
- Portas para persistência e publicação de eventos
- Testes arquiteturais para direção de dependências
- Exemplos que demonstrem o domínio sem infraestrutura

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis a dependências globais.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`core.txt`](../../../requirements/core.txt)
- [`oop.txt`](../../../requirements/oop.txt)
- [`software_design.txt`](../../../requirements/software_design.txt)
- [`plugins.txt`](../../../requirements/plugins.txt)

## Integração com o Atlas

- A Atlas API invoca seus casos de uso
- Engenharia de Dados implementa portas de persistência
- Automação e IA consomem contratos estáveis

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
