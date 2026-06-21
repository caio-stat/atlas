# Atlas Data Mining

> Aquisição responsável de dados públicos, web, imagens e documentos.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

A trilha de Data Mining transforma fontes externas heterogêneas em ativos brutos rastreáveis. Ela prioriza política da fonte, reprodutibilidade, proveniência, limitação de requisições e tratamento de falhas antes do volume de extração.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes que possam integrar o ecossistema sem acoplamento desnecessário.
- Produzir material de portfólio que explique tanto o resultado quanto o raciocínio.

## Escopo técnico

- Coleta HTTP e automação de navegador
- Parsing de HTML e dados estruturados
- Extração de PDF e layout documental
- OCR para imagens digitalizadas
- Proveniência e manifestos de coleta
- Rate limiting, retries e coleta incremental
- Restrições éticas e legais de coleta

## Entregáveis de referência

- Um protocolo para adapters de fonte
- Um coletor reprodutível de dados públicos
- Manifestos de dados brutos com hashes e timestamps
- Comparação entre OCR e extração de PDF
- Fixtures de falha e políticas responsáveis de retry

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis a dependências globais.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`scraping.txt`](../../../requirements/scraping.txt)
- [`ocr.txt`](../../../requirements/ocr.txt)
- [`document_intelligence.txt`](../../../requirements/document_intelligence.txt)
- [`data.txt`](../../../requirements/data.txt)

## Integração com o Atlas

- Alimenta zonas de ingestão do ETL
- Fornece documentos para pipelines de recuperação de IA
- Expõe o status da coleta à Observabilidade

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
