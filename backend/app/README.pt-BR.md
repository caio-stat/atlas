# Pacote da aplicação backend Atlas

> Fronteira de composição do processo FastAPI e de seus módulos arquiteturais.

[English](README.md) | **Português**

[Backend](../README.pt-BR.md) · [Catálogo de módulos](../../docs/modules/README.pt-BR.md)

## Status atual

Parcialmente implementado. `main.py` e `database.py` contêm código executável; os pacotes de API, core, domínio e casos de uso são principalmente scaffolds vazios.

## Responsabilidades

- Criar e configurar a aplicação FastAPI
- Conectar adapters de interface a casos de uso
- Controlar wiring de inicialização e encerramento do processo
- Expor factories de infraestrutura na raiz de composição
- Manter visível a direção das dependências
- Preservar comportamento previsível, transparente e orientado por consentimento para usuários e clientes

## Fora do escopo

- Implementar regras de negócio diretamente nas rotas
- Transformar helpers compartilhados em camada utilitária sem limites
- Permitir que o domínio importe FastAPI ou SQLAlchemy
- Esconder configuração de ambiente em globais

## Contratos e fronteiras

- Aplicação ASGI `app.main:app`
- Endpoints HTTP atualmente declarados em `main.py`
- `engine` e `SessionLocal` do SQLAlchemy em `database.py`

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
- Inclua casos felizes, validação, falhas conhecidas, segurança e fluxos de recuperação.
- Mantenha fixtures pequenas, determinísticas e sem dados sensíveis.
- Verifique clareza para o usuário, mensagens de erro e acessibilidade das saídas quando relevante.

## Regras de evolução

- Implemente uma fatia vertical antes de generalizar.
- Não adicione abstração sem ao menos um consumidor concreto.
- Atualize as duas versões do README junto com mudanças de contrato.
- Registre decisões transversais ou caras de reverter em ADR.

## Próximos passos

1. Mover rotas para o pacote de API
2. Mover configuração para settings tipados no core
3. Implementar uma entidade e um caso de uso
4. Adicionar fronteiras de repository e transação

## Definição de pronto

- A responsabilidade do módulo está refletida no código.
- Contratos públicos e erros estão documentados.
- Testes proporcionais ao risco executam por comando documentado.
- Configuração e secrets não estão acoplados ao código.
- O status deste documento corresponde ao repositório.
