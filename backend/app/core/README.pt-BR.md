# Módulo core do backend Atlas

> Configuração tipada e primitivas transversais de processo com escopo controlado.

[English](README.md) | **Português**

[Backend](../../README.pt-BR.md) · [Catálogo de módulos](../../../docs/modules/README.pt-BR.md)

## Status atual

Scaffold vazio. `config.py` existe, mas ainda não define settings.

## Responsabilidades

- Carregar e validar settings vindos do ambiente
- Definir ambiente da aplicação e feature flags
- Fornecer configuração de logging e telemetria
- Hospedar exceções tipadas estáveis quando realmente transversais
- Manter valores secretos fora do código-fonte

## Fora do escopo

- Conter entidades ou casos de uso
- Criar sessões de banco durante import
- Virar pacote de helpers diversos
- Ler configuração independentemente em cada módulo

## Contratos e fronteiras

- Objeto de settings imutável planejado
- Nomes de variáveis de ambiente e defaults seguros de desenvolvimento
- Um único ponto de entrada de settings para a raiz de composição

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

1. Definir ambiente, versão da API, URL do banco e nível de log
2. Remover a URL fixa de `database.py`
3. Adicionar testes para settings ausentes ou inválidos
4. Documentar um `.env.example` sem secrets

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
