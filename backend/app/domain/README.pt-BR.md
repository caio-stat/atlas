# Módulo de domínio do Atlas

> Linguagem de negócio, invariantes e contratos estáveis independentes de frameworks.

[English](README.md) | **Português**

[Backend](../../README.pt-BR.md) · [Catálogo de módulos](../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold vazio. A árvore de pacotes existe, mas nenhum comportamento de domínio foi implementado.

## Responsabilidades

- Modelar explicitamente os conceitos de negócio do Atlas
- Proteger invariantes por entidades e objetos de valor
- Definir erros de domínio e contratos estáveis de repository
- Expressar comportamento sem aspectos de transporte ou persistência
- Fornecer terminologia compartilhada entre módulos

## Fora do escopo

- Importar FastAPI, SQLAlchemy ou SDKs de provedores
- Validar detalhes específicos de payload HTTP
- Controlar configuração de ambiente
- Executar I/O de rede, arquivo ou banco

## Contratos e fronteiras

- Agregado ou entidade `DataSource` planejado
- Portas de repository definidas no domínio ou aplicação
- Erros de domínio tipados sem conhecimento de status HTTP

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

1. Escrever um glossário de domínio
2. Definir o menor modelo útil de `DataSource`
3. Adicionar testes unitários focados em invariantes
4. Introduzir protocolo de repository somente quando o caso exigir

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
