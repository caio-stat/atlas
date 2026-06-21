# Atlas Laboratório de Embarcados, IoT e Sistemas Autônomos

> Dispositivos de borda, protocolos industriais, controle, robótica e comportamento autônomo.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

Esta trilha conecta software a dispositivos físicos e runtimes restritos. Segurança, comportamento determinístico, correção de protocolos, simulação e degradação controlada têm prioridade sobre amplitude de funcionalidades.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Linux embarcado e MicroPython
- Serial, Modbus, CAN, MQTT, BLE e OPC-UA
- Sensores, telemetria e armazenamento na borda
- Malhas de controle e simulação
- Robótica e fronteiras de atuadores
- FPGA e integração com runtimes nativos
- Saúde do dispositivo e recuperação autônoma
- Integração industrial e hard real-time

## Entregáveis de referência

- Um pipeline simulado de telemetria
- Um adapter de protocolo com fixtures gravadas
- Uma simulação PID ou de sistema de controle
- Um monitor de saúde de dispositivo
- Um experimento seguro de inferência na borda

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`embedded.txt`](../../../requirements/embedded.txt)
- [`embedded_linux.txt`](../../../requirements/embedded_linux.txt)
- [`micropython.txt`](../../../requirements/micropython.txt)
- [`fpga.txt`](../../../requirements/fpga.txt)
- [`hardware_protocols.txt`](../../../requirements/hardware_protocols.txt)
- [`iot.txt`](../../../requirements/iot.txt)
- [`industrial.txt`](../../../requirements/industrial.txt)
- [`robotics.txt`](../../../requirements/robotics.txt)
- [`control_system.txt`](../../../requirements/control_system.txt)
- [`hard_realtime_integration.txt`](../../../requirements/hard_realtime_integration.txt)
- [`autonomous_systems.txt`](../../../requirements/autonomous_systems.txt)

## Integração com o Atlas

- Envia telemetria por Mensageria
- Armazena medições por Engenharia de Dados
- Usa Observabilidade para saúde e alertas de dispositivos

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
