# Atlas Laboratório de BI e Storytelling

> Dashboards orientados à decisão, relatórios analíticos e comunicação responsável de dados.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Laboratório de BI e Storytelling transforma dados confiáveis em decisões compreensíveis. Deve definir público e perguntas antes dos gráficos, preservar definições de métricas, expor incerteza e manter um caminho rastreável entre afirmações visuais e dados de origem.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Definição de métricas e KPIs
- Visualização exploratória e explicativa
- Dashboards interativos
- Experimentos com Power BI e Microsoft Fabric
- Pipelines de notebook para relatório
- Design acessível de gráficos e cores
- Estrutura narrativa e rastreabilidade de fontes

## Entregáveis de referência

- Um dicionário de métricas
- Um dashboard analítico com filtros documentados
- Um relatório gerado a partir de notebook
- Um experimento de integração com Power BI
- Uma narrativa pública de portfólio apoiada por dados reprodutíveis

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`bi.txt`](../../../requirements/bi.txt)
- [`powerbi.txt`](../../../requirements/powerbi.txt)
- [`visualization.txt`](../../../requirements/visualization.txt)
- [`notebooks.txt`](../../../requirements/notebooks.txt)
- [`data.txt`](../../../requirements/data.txt)

## Integração com o Atlas

- Consome datasets de Engenharia de Dados
- Usa interpretações do Statistical Lab
- Publica resumos por web, mobile ou relatórios automatizados

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
