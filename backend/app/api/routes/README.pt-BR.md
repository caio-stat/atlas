# Módulos de rotas da Atlas API

> Handlers HTTP enxutos, agrupados por recurso e aspecto operacional.

[English](README.md) | **Português**

[Backend](../../../README.pt-BR.md) · [Catálogo de módulos](../../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold vazio. `health.py` existe, mas não contém rota; handlers de saúde e versão permanecem em `app/main.py`.

## Responsabilidades

- Declarar paths, métodos, status e schemas
- Resolver dependências da aplicação
- Chamar um caso de uso por operação quando prático
- Mapear erros conhecidos para respostas documentadas
- Manter handlers pequenos e revisáveis

## Fora do escopo

- Codificar decisões de negócio
- Construir infraestrutura global dentro dos handlers
- Executar SQL ad hoc
- Ocultar silenciosamente falhas da aplicação

## Contratos e fronteiras

- `health.py` deve conter rotas de liveness e readiness
- Futuros arquivos de recurso devem expor objetos `APIRouter`
- Routers devem ser montados centralmente com prefixes e tags explícitos

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

1. Implementar um `APIRouter` para `/health` e `/version`
2. Preservar respostas atuais durante a extração
3. Adicionar contrato `/ready` separado antes de verificar PostgreSQL
4. Testar inclusão do router na factory da aplicação

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
