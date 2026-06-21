# Scripts de automação mobile do Atlas

> Helpers Python e ADB para build, testes, inspeção e demonstração dos clientes mobile.

[English](README.md) | **Português**

[Projeto](../../README.pt-BR.md) · [Módulos](../../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

Este módulo apoia a aplicação Android com automação repetível. Pode orquestrar emuladores, ADB, Appium, screenshots, logs, fixtures QR e checagens da API, permanecendo separado do comportamento implementado em Kotlin.

## Dentro da fronteira

- Inspeção de dispositivos e emuladores via ADB
- Instalação de APK e entradas para smoke tests
- Appium e automação de UI
- Coleta de screenshots e logs
- Geração de QR e fixtures de teste
- Checagens de contrato da API mobile

## Fora da fronteira

- Lógica principal da aplicação Android
- Evasão de autorização ou bloqueios do dispositivo
- Seriais de devices e endpoints privados fixos
- Comandos destrutivos sem confirmação
- Dados pessoais sem redação em artefatos

## Estrutura proposta

```text
adb/
appium/
fixtures/
reports/
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

- [`mobile_testing.txt`](../../requirements/mobile_testing.txt)
- [`mobile.txt`](../../requirements/mobile.txt)
- [`scripting.txt`](../../requirements/scripting.txt)

## Trilhas relacionadas

- [mobile](../../docs/tracks/mobile/README.pt-BR.md)
- [automation](../../docs/tracks/automation/README.pt-BR.md)
- [support](../../docs/tracks/support/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Adicionar comando de descoberta sem mutação
2. Definir pré-requisitos de emulador e dispositivo físico
3. Criar smoke test da tela de saúde após o app existir
4. Armazenar artefatos em diretórios ignorados e datados

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
