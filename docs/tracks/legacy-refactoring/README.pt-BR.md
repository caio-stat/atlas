# Atlas Laboratório de Legado e Refatoração

> Caracterização, modernização segura, recuperação arquitetural e evidência de dívida técnica.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Laboratório de Legado e Refatoração demonstra como sistemas reais melhoram sem reescritas cegas. Ele preserva comportamento observável, cria redes de segurança, mede problemas estruturais e migra responsabilidades em passos revisáveis.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Testes de caracterização e aprovação
- Análise estática e medição de complexidade
- Recuperação de dependências e arquitetura
- Padrões de refatoração incremental
- Adapters e migrações Strangler Fig
- Registros e priorização de dívida técnica
- Compatibilidade, depreciação e rollback

## Entregáveis de referência

- Uma fixture de legado intencionalmente problemática
- Uma rede de segurança com testes de caracterização
- Um estudo de caso mensurado de refatoração
- Uma migração baseada em adapter
- Um relatório arquitetural antes e depois

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`refactoring.txt`](../../../requirements/refactoring.txt)
- [`code_quality.txt`](../../../requirements/code_quality.txt)
- [`advanced_testing.txt`](../../../requirements/advanced_testing.txt)
- [`software_design.txt`](../../../requirements/software_design.txt)
- [`oop.txt`](../../../requirements/oop.txt)

## Integração com o Atlas

- Moderniza módulos sem quebrar contratos
- Alimenta políticas de qualidade no CI/CD
- Produz ADRs e runbooks de migração

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
