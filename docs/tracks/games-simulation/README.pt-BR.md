# Atlas Laboratório de Jogos e Simulação

> Sistemas interativos, comportamento de agentes, telemetria de jogos e simulação em tempo real.

[English](README.md) | **Português**

[Índice de trilhas](../README.pt-BR.md) · [Documentação](../../README.pt-BR.md) · [Projeto](../../../README.pt-BR.md)

## Missão

O Laboratório de Jogos e Simulação usa ambientes interativos para tornar visíveis algoritmos, probabilidade, agentes e restrições de tempo real. Os projetos devem priorizar comportamento mensurável e valor educacional, não a quantidade de engines.

Um projeto maior e mais completo nessa trilha deve ser um jogo mobile-first que demonstre tanto profundidade de gameplay quanto disciplina de engenharia: regras claras, telemetria legível, testes reprodutíveis e atenção ao desempenho em celulares. O jogo também pode usar referências de psicologia e filosofia para desafiar a atenção, a tomada de decisão, a tolerância à ambiguidade, o autocontrole, a resiliência emocional e a própria noção de identidade do jogador. A ideia é criar um experimento de treinamento mental e reflexão existencial em que o usuário precisa pensar rápido, revisar hipóteses, lidar com frustração controlada, adaptar comportamento sob pressão e confrontar diferentes modos de interpretar a realidade.

## Resultados esperados

- Transformar estudo em software executável, testado e demonstrável.
- Registrar premissas, decisões, limitações e evidências de forma reproduzível.
- Entregar componentes integráveis sem acoplamento desnecessário.
- Produzir material de portfólio que explique resultado e raciocínio.

## Escopo técnico

- Protótipos 2D e 3D leves
- Controles touch e layouts responsivos para celular
- Game loops, temporização e análise de budget de frames
- Física e simulação discreta
- Pathfinding e comportamento de agentes
- Sistemas de progressão, economia e persistência
- Psicologia comportamental e design de atenção
- Teorias cognitivistas, humanistas, psicanalíticas, existencialistas e neurocientíficas
- Carga cognitiva, incerteza, estresse controlado e tomada de decisão
- Loops de recompensa, hábito, motivação e feedback adaptativo
- Filosofias da percepção, da liberdade, da ética e da consequência
- Ambientes de reinforcement learning
- Telemetria e analytics de jogos
- Visualização interativa de probabilidade

## Conceito principal proposto

Uma direção forte para o portfólio é um jogo mobile-ready como **Atlas Run**: uma experiência 2D de ação/arcade com sessões curtas, desafios procedurais, escolhas de upgrades, oponentes com IA leve e cenários que forçam o jogador a interpretar sinais ambíguos, dilemas morais e padrões de comportamento. O projeto deve priorizar:

- um loop principal claro que funcione bem com toque;
- regras determinísticas e fáceis de testar;
- mecanismos de pressão psicológica controlada, como incerteza, timing apertado, decisões com trade-offs, estímulos que exigem leitura rápida de contexto e escolhas que revelam preferências pessoais;
- telemetria para retenção, duração da sessão, taxa de erro, hesitação, padrões de pausa, variação de estratégia e equilíbrio de dificuldade;
- progressão compatível com uso offline ou salvamento incremental;
- um desenho de feedback que estimule atenção, memória operativa, autocorreção, revisão de escolhas, aprendizagem por tentativa e reflexão sobre padrões de comportamento;
- uma separação limpa entre lógica de jogo, interface, analytics e experimentos comportamentais.

## Componente psicológico do projeto

O jogo pode usar referências de psicologia e filosofia para provocar reflexão e aprendizagem, por exemplo:

- o clássico problema entre estímulo e resposta, com variações de reforço e recompensa;
- a influência da atenção, da memória e da percepção na escolha do jogador;
- a tensão entre liberdade, determinismo e responsabilidade;
- a distinção entre dor útil, frustração construtiva e bloqueio emocional;
- a comparação entre perspectivas behaviorista, cognitivista, humanista, existencialista, psicanalítica e neurocientífica;
- a forma como narrativas, símbolos e dilemas morais moldam interpretação e decisão.

## Mapa de referências históricas

O projeto pode ser estruturado para dialogar com grandes tradições ao longo da história intelectual:

- Psicologia: estruturalismo, funcionalismo, behaviorismo, Gestalt, psicanálise, cognitivismo, humanismo, psicologia social, psicologia evolutiva, positiva e neurociência.
- Filosofia: Sócrates, Platão e Aristóteles; estoicismo, ceticismo e epicurismo; racionalismo e empirismo; Kant; pragmatismo; fenomenologia; existencialismo; utilitarismo; ética da virtude; filosofia analítica e continental.
- Temas cruzados: mente e corpo, percepção e realidade, moralidade, intenção, hábito, medo, culpa, liberdade, sofrimento e propósito.

Esses mecanismos devem ser usados com transparência, controle e propósito educativo, não como enganação arbitrária ou coercão escondida.

## Entregáveis de referência

- Uma simulação determinística de agentes
- Um visualizador de pathfinding
- Um protótipo de jogo mobile-first com controles touch
- Um pipeline de análise de telemetria de jogos
- Um experimento interativo de probabilidade
- Um benchmark de reinforcement learning com baselines

## Abordagem arquitetural

- Começar por uma fatia vertical pequena, com entrada, regra, saída e teste.
- Separar lógica de domínio de frameworks, armazenamento e interfaces externas.
- Preferir contratos explícitos e adapters substituíveis.
- Adicionar infraestrutura somente quando um caso de uso concreto exigir.
- Documentar decisões irreversíveis ou de alto impacto em ADRs.

## Trilhas de dependências

- [`games.txt`](../../../requirements/games.txt)
- [`games_engines.txt`](../../../requirements/games_engines.txt)
- [`games_ai.txt`](../../../requirements/games_ai.txt)
- [`game_data.txt`](../../../requirements/game_data.txt)
- [`simulation.txt`](../../../requirements/simulation.txt)
- [`realtime_programming.txt`](../../../requirements/realtime_programming.txt)
- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Integração com o Atlas

- Usa métodos estatísticos e numéricos
- Transmite telemetria pela infraestrutura de Tempo Real
- Fornece ambientes controlados para experimentos de IA

## Qualidade e evidências

- Testes unitários para regras e transformações determinísticas.
- Testes de integração nas fronteiras externas.
- Dados, seeds e configuração versionados quando necessários.
- Métricas técnicas e de produto adequadas ao experimento.
- Métricas comportamentais sobre foco, erro, revisão, pausa, recuperação e mudança de estratégia.
- Registro explícito das referências psicológicas e filosóficas usadas na arte, na narrativa e nos sistemas de jogo.
- README, exemplos e limitações atualizados junto ao código.
- Nenhum segredo ou dado pessoal versionado.
- Design ético: o jogador deve poder reconhecer, entender e, quando aplicável, controlar os estímulos usados.

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
