# Atlas Support Lab

> Diagnóstico prático, inventário, health checks e relatórios de suporte.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Support Lab converte rotinas de helpdesk em ferramentas seguras e explicáveis. Diagnósticos devem coletar apenas dados necessários, distinguir evidência de inferência, evitar correções destrutivas por padrão e gerar relatórios revisáveis por outro técnico.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Diagnóstico de CPU, memória, disco e processos
- Health checks de serviços e endpoints
- Inventário de hardware e software
- Sondas de suporte Windows e Linux
- Diagnóstico de rede e DNS
- Relatórios Markdown, HTML e JSON
- Consentimento, privacidade e correção segura

## Entregáveis de referência

- Uma CLI de diagnóstico de suporte somente leitura
- Um snapshot de inventário da máquina
- Um relatório de saúde de disco e memória
- Um verificador de disponibilidade de serviços
- Um pacote de evidências de incidente com dados sensíveis removidos

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`support.txt`](../../../requirements/support.txt)
- [`automation.txt`](../../../requirements/automation.txt)
- [`scripting.txt`](../../../requirements/scripting.txt)
- [`networking.txt`](../../../requirements/networking.txt)

## Integração com o Atlas

- Fornece evidência operacional à Observabilidade
- Usa sondas de Redes para problemas de conectividade
- Pode expor resumos pela Atlas API e pelo Mobile

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
