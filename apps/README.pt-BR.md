# Aplicações clientes do Atlas

> Contêiner para produtos web, mobile e futuros clientes desktop.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

A pasta apps hospeda interfaces implantáveis que consomem contratos do Atlas. Cada aplicação controla apresentação e estado do cliente, enquanto usa o backend para capacidades compartilhadas e persistência remota.

## Dentro da fronteira

- Código e configuração de build dos clientes
- Apresentação, navegação e estado local
- Adapters de API e cache no cliente
- Acessibilidade e comportamento específico do dispositivo
- Testes da aplicação e notas de release

## Fora da fronteira

- Acesso direto ao banco remoto
- Implementação compartilhada do domínio backend
- Secrets ou endpoints de produção sem versionamento seguro
- Código copiado entre apps sem responsabilidade definida

## Estrutura proposta

```text
mobile/
web/ (planned)
desktop/ (planned)
shared/ (only after real reuse)
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`mobile.txt`](../requirements/mobile.txt)
- [`mobile_testing.txt`](../requirements/mobile_testing.txt)

## Trilhas relacionadas

- [mobile](../docs/tracks/mobile/README.pt-BR.md)
- [api](../docs/tracks/api/README.pt-BR.md)
- [bi-storytelling](../docs/tracks/bi-storytelling/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Implementar a primeira tela de status do Atlas Pocket
2. Documentar seleção de ambiente da API
3. Adicionar testes de contrato do cliente
4. Criar outros apps apenas quando o trabalho começar

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
