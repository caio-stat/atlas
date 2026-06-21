# Módulo de infraestrutura do Atlas

> Ambientes locais versionados, definições de deploy, stacks de telemetria e configuração operacional.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

O módulo de infraestrutura deve tornar ambientes repetíveis e descartáveis. Ele controla configuração de deploy e runtime, não regras de negócio. O Compose PostgreSQL atual permanece na raiz e só deve mudar com migração documentada.

## Dentro da fronteira

- Definições de containers e Compose
- Inicialização de banco e apoio a migrações
- Stacks locais de monitoramento e telemetria
- Experimentos de infraestrutura como código
- Configuração CI/CD e deploy
- Runbooks e procedimentos de teardown

## Fora da fronteira

- Lógica de negócio da aplicação
- Recursos cloud sem controles de custo e limpeza
- Secrets de produção
- Scripts não revisados que alteram infraestrutura compartilhada

## Estrutura proposta

```text
docker/
postgres/
monitoring/
cloud/
ci/
runbooks/
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`devops.txt`](../requirements/devops.txt)
- [`cloud_orchestration.txt`](../requirements/cloud_orchestration.txt)
- [`observability.txt`](../requirements/observability.txt)
- [`security.txt`](../requirements/security.txt)

## Trilhas relacionadas

- [cloud-devops](../docs/tracks/cloud-devops/README.pt-BR.md)
- [observability](../docs/tracks/observability/README.pt-BR.md)
- [systems](../docs/tracks/systems/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Documentar responsabilidade do Compose da raiz
2. Adicionar readiness do banco e fluxo de migração
3. Definir telemetria local depois que a API emitir sinais
4. Adicionar instruções de teardown e retenção de dados

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
