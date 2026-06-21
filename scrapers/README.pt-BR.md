# Módulo de coleta de dados do Atlas

> Adapters responsáveis para aquisição web, documental e de dados públicos.

[English](README.md) | **Português**

[Projeto](../README.pt-BR.md) · [Módulos](../docs/modules/README.pt-BR.md)

## Estado atual

**Scaffold vazio.** O diretório existe, mas não contém implementação além desta documentação.

## Finalidade

O módulo scrapers deve implementar coleta específica por fonte atrás de contratos operacionais comuns. A coleta precisa respeitar autorização, políticas da fonte, rate limits, proveniência e reprodutibilidade.

## Dentro da fronteira

- Adapters HTTP e de navegador
- Extração HTML, JSON, PDF e documentos
- Rate limiting, retries e checkpoints incrementais
- Manifestos de coleta e proveniência
- Fixtures para testes de parser e falha

## Fora da fronteira

- Acesso sem autorização ou evasão de políticas
- Credenciais versionadas com coletores
- Crawling sem limites
- Mudanças de schema silenciosas
- Transformação que pertence ao ETL

## Estrutura proposta

```text
sources/
parsers/
manifests/
fixtures/
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

- [`scraping.txt`](../requirements/scraping.txt)
- [`document_intelligence.txt`](../requirements/document_intelligence.txt)
- [`ocr.txt`](../requirements/ocr.txt)
- [`resilience.txt`](../requirements/resilience.txt)

## Trilhas relacionadas

- [data-mining](../docs/tracks/data-mining/README.pt-BR.md)
- [data-engineering](../docs/tracks/data-engineering/README.pt-BR.md)
- [observability](../docs/tracks/observability/README.pt-BR.md)

## Qualidade, segurança e operação

- Adicione testes proporcionais ao risco antes de integrar.
- Mantenha configuração externa ao código e nunca versione secrets.
- Documente falhas esperadas, retries, rollback e ownership quando aplicável.
- Use dados mínimos, públicos ou anonimizados em exemplos.
- Meça custo e recursos antes de ampliar a solução.

## Próximos passos

1. Selecionar uma fonte pública, estável e permitida
2. Escrever política da fonte e schema esperado
3. Capturar fixtures antes da coleta ao vivo
4. Implementar coleta limitada com proveniência

## Definição de pronto da primeira entrega

- Existe um caso de uso executável e pequeno.
- Setup e verificação funcionam em clone limpo.
- Contratos, erros e limitações estão documentados.
- Testes e evidências demonstram o comportamento.
- Este README foi atualizado para refletir o código real.
