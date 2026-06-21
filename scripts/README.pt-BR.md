# Scripts operacionais do Atlas

> Pequenos pontos de entrada para tarefas repetíveis de desenvolvimento, manutenção e suporte.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

Scripts devem facilitar a repetição de uma operação limitada. Não são atalho para ignorar fronteiras, testes, configuração ou segurança. Lógica complexa deve migrar para módulo importável e deixar o script como entrada enxuta.

## Dentro da fronteira

- Comandos de setup e verificação
- Entradas para recuperação de dados e relatórios
- Diagnósticos seguros de suporte
- Wrappers de migração e manutenção
- Helpers de automação mobile e devices

## Fora da fronteira

- Lógica de negócio duradoura
- Credenciais ou paths específicos fixos
- Defaults destrutivos
- Mutações externas sem registro
- Scripts sem responsável ou documentação de uso

## Estrutura proposta

```text
development/
data/
support/
operations/
mobile/
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`scripting.txt`](../requirements/scripting.txt)
- [`automation.txt`](../requirements/automation.txt)
- [`support.txt`](../requirements/support.txt)

## Trilhas relacionadas

- [automation](../docs/tracks/automation/README.pt-BR.md)
- [support](../docs/tracks/support/README.pt-BR.md)
- [cloud-devops](../docs/tracks/cloud-devops/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Escolher uma tarefa manual repetida do repositório
2. Implementar dry-run ou default somente leitura
3. Adicionar `--help`, exit codes e saída estruturada
4. Testar lógica central fora do wrapper CLI

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
