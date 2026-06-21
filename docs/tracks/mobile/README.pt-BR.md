# Atlas Mobile Lab

> Clientes mobile offline-first, ferramentas de suporte em campo e inteligência no dispositivo.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Mobile Lab leva as capacidades do Atlas a dispositivos restritos e com conectividade intermitente. O produto inicial, Atlas Pocket, deve consumir a API existente antes de adicionar persistência local, sincronização, câmera, notificações e inferência mobile, preservando clareza, autonomia, acessibilidade e confiança para usuários em contextos reais.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Clientes Kotlin e Jetpack Compose
- Integração REST com Retrofit e OkHttp
- Persistência com Room e DataStore
- Sincronização offline-first
- Trabalho em background e notificações
- Fluxos de câmera, QR Code e OCR
- Inferência de IA local e remota
- Acessibilidade, redução de carga cognitiva e feedback consistente
- Testes Android automatizados

## Entregáveis de referência

- Tela de saúde e versão no Atlas Pocket
- Um cache local com estados explícitos de sincronização
- Um protótipo de checklist de suporte em campo
- Um fluxo de captura de QR ou documento
- Uma suíte automatizada de smoke tests mobile

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Integração com o Atlas

- Consome a Atlas API, nunca bancos remotos diretamente
- Armazena informações de BI e Suporte para uso em campo
- Chama serviços de IA ou executa modelos leves aprovados

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras externas.
- Dados, seeds e configuração versionados quando necessários.
- Métricas técnicas e de produto adequadas ao experimento.
- Métricas centradas no usuário, como compreensão, recuperação de interrupções e confiança no uso.
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
