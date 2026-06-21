# Módulo de analytics do Atlas

> Espaço para código reutilizável de estatística, machine learning e relatórios que amadurece além da exploração.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

O módulo de analytics deve conter componentes analíticos testados e reutilizáveis fora de um único notebook: definições de métricas, rotinas estatísticas, transformações de features, avaliação e construção de relatórios. Não deve virar depósito de arquivos exploratórios.

## Dentro da fronteira

- Métricas e transformações analíticas reutilizáveis
- Utilitários estatísticos e de avaliação de modelos
- Pipelines de features com contratos explícitos
- Construtores de relatórios e visualizações
- Apoio a experimentos independente de dataset

## Fora da fronteira

- Datasets raw ou processed
- Células isoladas de notebooks copiadas sem testes
- Binários de modelos e relatórios grandes gerados
- Transporte de API ou infraestrutura de banco

## Estrutura proposta

```text
statistics/
features/
evaluation/
reporting/
tests/
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`data.txt`](../requirements/data.txt)
- [`statistics.txt`](../requirements/statistics.txt)
- [`ml.txt`](../requirements/ml.txt)
- [`visualization.txt`](../requirements/visualization.txt)

## Trilhas relacionadas

- [statistics](../docs/tracks/statistics/README.pt-BR.md)
- [machine-learning](../docs/tracks/machine-learning/README.pt-BR.md)
- [bi-storytelling](../docs/tracks/bi-storytelling/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Escolher uma métrica ou transformação usada em análise real
2. Definir entradas, saídas e falhas tipadas
3. Adicionar testes unitários determinísticos
4. Usá-la a partir de notebook ou adapter da API

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
