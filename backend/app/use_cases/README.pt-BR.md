# Casos de uso da aplicação Atlas

> Orquestração da aplicação que coordena comportamento de domínio e portas externas.

[English](README.md) | **Português**

[Backend](../../README.pt-BR.md) · [Catálogo de módulos](../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold vazio. `register_data_source.py` existe, mas não possui implementação.

## Responsabilidades

- Representar uma intenção de usuário ou sistema por caso de uso
- Validar pré-condições da aplicação
- Coordenar objetos de domínio e portas de repository
- Definir fronteiras de transação e idempotência
- Retornar resultados neutros a transporte e erros tipados

## Fora do escopo

- Ler objetos Request do FastAPI
- Retornar classes Response do framework
- Embutir queries SQLAlchemy
- Escolher configuração de ambiente dinamicamente

## Contratos e fronteiras

- Entrada e resultado planejados de `register_data_source`
- Dependência de repository fornecida por construção
- Comportamento explícito para duplicidade e validação

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

1. Escrever o contrato do caso antes da rota
2. Injetar um protocolo mínimo de repository
3. Implementar sucesso e duplicidade
4. Testar com fake em memória antes do SQLAlchemy

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
