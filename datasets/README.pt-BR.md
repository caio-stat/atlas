# Módulo de datasets do Atlas

> Espaço governado para pequenas amostras reprodutíveis e metadados de datasets.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

A pasta datasets define como o Atlas referencia dados sem transformar o Git em data lake. Pequenas amostras públicas e metadados podem ser versionados; datasets grandes, privados, licenciados ou gerados pertencem a storage externo com instruções reprodutíveis.

## Dentro da fronteira

- Dataset cards e proveniência
- Pequenas amostras públicas usadas em testes ou demos
- Schemas, checksums e manifestos de recuperação
- Notas de licença, retenção e sensibilidade
- Fronteiras documentadas de raw para processed

## Fora da fronteira

- Secrets ou dados pessoais
- Binários grandes sem estratégia de artefatos
- Cópias sem licença de dados de terceiros
- Edições manuais sem linhagem
- Saídas de modelos misturadas aos dados-fonte

## Estrutura proposta

```text
raw/ (ignored or external)
processed/ (reproducible)
samples/ (small and public)
schemas/
README cards per dataset
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
- [`data_engineering.txt`](../requirements/data_engineering.txt)

## Trilhas relacionadas

- [data-mining](../docs/tracks/data-mining/README.pt-BR.md)
- [data-engineering](../docs/tracks/data-engineering/README.pt-BR.md)
- [statistics](../docs/tracks/statistics/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Selecionar um dataset público legalmente reutilizável
2. Escrever dataset card e URL de origem
3. Adicionar checksum e procedimento de recuperação
4. Criar pequena amostra de teste e schema

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
