# Testes do backend Atlas

> Evidência executável dos contratos, comportamento de domínio e fronteiras de integração.

[English](README.md) | **Português**

[Backend](../README.pt-BR.md) · [Catálogo de módulos](../../docs/modules/README.pt-BR.md)

## Status atual

Existe cobertura inicial em `test_health.py` para `/health` e `/version`. O teste chamado `test_root_endpoint` exercita `/health` e deve ser renomeado para maior clareza.

## Responsabilidades

- Verificar comportamento público e contratos de erro
- Proteger invariantes durante refatorações
- Exercitar integração de persistência e migrações
- Fornecer evidência determinística de regressão
- Identificar claramente testes lentos ou externos

## Fora do escopo

- Depender da ordem de execução
- Chamar serviços de produção não controlados
- Esconder flakiness com retries incondicionais
- Validar detalhes privados de implementação sem necessidade

## Contratos e fronteiras

- `python -m pytest` a partir de `backend/`
- `TestClient` do FastAPI para os testes atuais
- Futuras camadas unitária, integração, contrato e arquitetura

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

1. Renomear o teste de saúde para refletir o comportamento
2. Adicionar teste para `GET /`
3. Adicionar smoke tests de path inválido e OpenAPI
4. Criar testes de domínio antes da persistência
5. Introduzir fixtures de integração quando houver migrações

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
