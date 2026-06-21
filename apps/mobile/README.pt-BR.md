# Aplicação mobile do Atlas

> Local de implementação do Atlas Pocket e futuras ferramentas Android de campo.

[English](README.md) | **Português**

[Projeto](../../README.pt-BR.md) · [Módulos](../../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

Esta pasta está reservada para a aplicação Android descrita pelo Mobile Lab. Está vazia; as escolhas de arquitetura e stack estão documentadas, mas ainda não existe projeto Gradle.

## Dentro da fronteira

- Código Kotlin e Jetpack Compose
- Build Gradle e configuração Android
- Fontes de dados remota e local
- Sincronização offline e recursos do dispositivo
- Testes unitários, de integração e UI Android

## Fora da fronteira

- Protótipo mobile Python como cliente principal de produção
- Conexão direta com PostgreSQL
- Endpoints privados ou tokens fixos
- Complexidade de Room, IA ou câmera antes da fatia de saúde

## Estrutura proposta

```text
app/src/main/
app/src/test/
app/src/androidTest/
gradle/
docs/
```

A estrutura é direcional. Crie subdiretórios somente quando uma entrega real precisar deles.

## Fluxo de trabalho

1. Defina um problema e um critério de aceitação pequeno.
2. Escolha entradas, saídas e contrato antes das ferramentas.
3. Implemente uma fatia executável com teste.
4. Registre configuração, riscos e limitações.
5. Conecte o módulo por contrato explícito e atualize o status.

## Dependências relacionadas

- [`mobile.txt`](../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../requirements/mobile_testing.txt)

## Trilhas relacionadas

- [mobile](../../docs/tracks/mobile/README.pt-BR.md)
- [api](../../docs/tracks/api/README.pt-BR.md)
- [observability](../../docs/tracks/observability/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Criar projeto Gradle com SDK suportado explícito
2. Implementar modelos da API de saúde e versão
3. Renderizar loading, sucesso, offline e erro
4. Adicionar testes unitários e smoke tests de UI

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
