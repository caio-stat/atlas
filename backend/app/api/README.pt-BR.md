# Módulo de interface da Atlas API

> Fronteira de transporte HTTP para validação, roteamento, serialização e status.

[English](README.md) | **Português**

[Backend](../../README.pt-BR.md) · [Catálogo de módulos](../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold. O pacote existe, mas os endpoints atuais ainda estão definidos diretamente em `app/main.py`.

## Responsabilidades

- Organizar routers FastAPI versionados
- Validar schemas de request e response
- Traduzir erros da aplicação em respostas HTTP
- Aplicar aspectos de transporte, como paginação e request IDs
- Publicar metadados OpenAPI corretos

## Fora do escopo

- Conter invariantes de domínio ou queries de persistência
- Abrir sessões de banco sem gerenciamento
- Retornar exceções internas ou configuração secreta
- Acoplar casos de uso a objetos Request do FastAPI

## Contratos e fronteiras

- Router versionado planejado e montado por `app.main`
- Schemas Pydantic de request e response
- Representação consistente de erros
- Interface de saúde, prontidão e versão

## Direção de dependências

```text
HTTP / framework
      ↓
application use cases
      ↓
domain contracts
      ↑
infrastructure adapters
```

O módulo deve depender de contratos mais estáveis e receber detalhes externos pela composição. Imports que invertam essa direção precisam de justificativa arquitetural.

## Estratégia de testes

- Teste o comportamento público, não detalhes do framework.
- Use unit tests para regras puras e contract tests nas fronteiras.
- Inclua casos felizes, validação, falhas conhecidas e segurança.
- Mantenha fixtures pequenas, determinísticas e sem dados sensíveis.

## Regras de evolução

- Implemente uma fatia vertical antes de generalizar.
- Não adicione abstração sem ao menos um consumidor concreto.
- Atualize as duas versões do README junto com mudanças de contrato.
- Registre decisões transversais ou caras de reverter em ADR.

## Próximos passos

1. Extrair endpoints existentes sem mudar comportamento
2. Adicionar testes no nível do router
3. Definir convenções de erro e versionamento
4. Adicionar o primeiro endpoint de fonte de dados

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
