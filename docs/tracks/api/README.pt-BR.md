# Atlas API

> A interface HTTP que expõe as capacidades do Atlas por contratos estáveis e observáveis.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

A Atlas API é o principal ponto de entrada para clientes durante a fase de fundação. Ela deve traduzir aspectos HTTP em chamadas da aplicação, manter regras de negócio fora dos handlers, tornar o estado operacional visível por endpoints de saúde, versão e futura prontidão, além de apoiar confiança, transparência e interação informada para todos os usuários e clientes.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes que possam integrar o ecossistema sem acoplamento desnecessário.
- Produzir material de portfólio que explique tanto o resultado quanto o raciocínio.

## Escopo técnico

- Composição da aplicação FastAPI
- Convenções de recursos REST e erros
- Validação de requisições e respostas
- Endpoints de saúde, prontidão e versão
- Documentação OpenAPI e exemplos
- Fronteiras de autenticação e autorização
- Paginação, idempotência e correlation IDs
- Semântica clara de erro, sinais de consentimento e respostas acessíveis

## Entregáveis de referência

- Comportamento documentado de `/`, `/health` e `/version`
- Routers versionados para operações de fontes de dados
- Respostas de erro consistentes no formato problem details
- Testes de contrato e integração da API
- Middleware operacional para logs e IDs de requisição

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis a dependências globais.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`dev.txt`](../../../requirements/dev.txt)
- [`data_engineering.txt`](../../../requirements/data_engineering.txt)
- [`security.txt`](../../../requirements/security.txt)
- [`observability.txt`](../../../requirements/observability.txt)

## Integração com o Atlas

- Chama casos de uso do Atlas Core
- Persiste por adapters de Engenharia de Dados
- Atende clientes web, mobile, automações e agentes

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras com banco, rede, arquivos ou provedores.
- Dados, seeds e configuração versionados quando a reprodução depender deles.
- Métricas técnicas e de produto adequadas ao experimento.
- Métricas de confiança e clareza, como entendimento das respostas, recuperação de falhas e segurança percebida.
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
