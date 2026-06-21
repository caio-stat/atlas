# Entidades de domínio do Atlas

> Objetos de domínio com identidade que protegem regras de ciclo de vida e invariantes.

[English](README.md) | **Português**

[Backend](../../../README.pt-BR.md) · [Catálogo de módulos](../../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold vazio. `data_source.py` existe, mas não contém classe ou comportamento.

## Responsabilidades

- Representar identidade e transições de ciclo de vida
- Validar invariantes na construção ou mutação
- Usar tipos de domínio precisos no lugar de primitivas soltas
- Expor métodos orientados a comportamento
- Permanecer serializável por mappers externos quando possível

## Fora do escopo

- Espelhar tabelas do banco mecanicamente
- Conter schemas HTTP de request ou response
- Abrir sessões ou chamar serviços externos
- Acumular helpers de formatação e apresentação

## Contratos e fronteiras

- Identidade planejada de `DataSource`
- Nome, localização/tipo e status de ciclo de vida planejados
- Erros de validação explícitos para construção inválida

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
- Não adicione abstração sem consumidor concreto.
- Atualize as duas versões do README com mudanças de contrato.
- Registre decisões transversais ou caras de reverter em ADR.

## Próximos passos

1. Decidir campos mínimos a partir do caso real de registro
2. Modelar identidade e invariantes
3. Adicionar testes de igualdade e ciclo de vida
4. Manter mapeamento de persistência fora da entidade

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
