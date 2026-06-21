# Atlas AI Lab

> IA generativa, recuperação, agentes, políticas e integração responsável de modelos.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O AI Lab explora sistemas assistidos por modelos como produtos de engenharia, não como prompts isolados. Cada fluxo deve tornar visíveis fontes de contexto, permissões de ferramentas, validação, fallback, custo e avaliação, preservando julgamento humano, interpretabilidade, confiança e responsabilidade social.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Adapters de provedores LLM e modelos locais
- Embeddings e recuperação vetorial
- Pipelines RAG de ingestão e citação
- Tool calling e orquestração de agentes
- Motores de políticas e ações protegidas
- Avaliação de prompts, recuperação e respostas
- Controles de custo, latência, privacidade e fallback
- Explicabilidade, revisão de viés, supervisão humana e comportamento orientado por consentimento

## Entregáveis de referência

- Um gateway de modelos neutro a provedor
- Um protótipo de perguntas sobre documentos com citações
- Um agente com ferramentas de menor privilégio
- Um dataset de avaliação e suíte de regressão
- Um workflow de ações controlado por políticas

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`generative_ai.txt`](../../../requirements/generative_ai.txt)
- [`agents.txt`](../../../requirements/agents.txt)
- [`policy_agents.txt`](../../../requirements/policy_agents.txt)
- [`decision_system.txt`](../../../requirements/decision_system.txt)
- [`document_intelligence.txt`](../../../requirements/document_intelligence.txt)

## Integração com o Atlas

- Consome documentos curados por Data Mining
- Usa contratos da Atlas API e do Core como ferramentas
- Publica traces e métricas de avaliação para Observabilidade

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras externas.
- Dados, seeds e configuração versionados quando necessários.
- Métricas técnicas e de produto adequadas ao experimento.
- Métricas centradas no usuário, como qualidade da explicação, calibração de confiança, recuperação de erro e revisão de justiça.
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
