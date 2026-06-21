# Módulo de notebooks do Atlas

> Exploração reprodutível, educação e narrativas analíticas.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

Notebooks são interfaces para investigação e comunicação, não o destino final da lógica reutilizável. Cada notebook deve declarar pergunta, entradas, ambiente, ordem de execução, saídas e limitações.

## Dentro da fronteira

- Análise exploratória de dados
- Demonstrações estatísticas e numéricas
- Experimentos e diagnósticos de modelos
- Narrativas de relatórios reprodutíveis
- Explicações visuais e material didático

## Fora da fronteira

- Secrets, dados pessoais ou datasets raw sem controle
- Lógica reutilizável sem testes
- Estado manual oculto necessário à execução
- Outputs grandes versionados sem finalidade

## Estrutura proposta

```text
statistics/
machine_learning/
deep_learning/
numerical_methods/
experiments/
reports/
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`notebooks.txt`](../requirements/notebooks.txt)
- [`data.txt`](../requirements/data.txt)
- [`statistics.txt`](../requirements/statistics.txt)
- [`visualization.txt`](../requirements/visualization.txt)

## Trilhas relacionadas

- [statistics](../docs/tracks/statistics/README.pt-BR.md)
- [machine-learning](../docs/tracks/machine-learning/README.pt-BR.md)
- [deep-learning](../docs/tracks/deep-learning/README.pt-BR.md)
- [bi-storytelling](../docs/tracks/bi-storytelling/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Escolher uma amostra pública e uma pergunta analítica
2. Criar notebook executável após restart-and-run
3. Mover transformações reutilizáveis para `analytics/`
4. Exportar relatório leve sem outputs grandes nas células

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
