# Central de documentação do Atlas

> A camada de navegação para arquitetura, trilhas técnicas, módulos executáveis e evidências de portfólio.

[English](README.md) | **Português**

[README do projeto](../README.pt-BR.md) · [Backend](../backend/README.pt-BR.md) · [Dependências](../requirements/README.pt-BR.md)

## Finalidade

A documentação do Atlas faz parte do produto. Ela explica o que existe, o que
está planejado, por que uma decisão foi tomada, como executar uma capacidade e
quais evidências sustentam uma afirmação técnica. Esta pasta separa o material
detalhado do README raiz para manter a apresentação do projeto navegável.

## Mapa da documentação

| Área | Conteúdo | Entrada |
|---|---|---|
| Trilhas técnicas | Missão, escopo, entregáveis, dependências, qualidade e roadmap de 21 domínios | [Catálogo de trilhas](tracks/README.pt-BR.md) |
| Módulos do sistema | Documentação próxima de módulos executáveis ou especificados | [Catálogo de módulos](modules/README.pt-BR.md) |
| Backend | Fundação FastAPI e fronteiras das camadas da aplicação | [README do backend](../backend/README.pt-BR.md) |
| Trilhas de dependências | Conjuntos focados de instalação Python e regras de manutenção | [README de requirements](../requirements/README.pt-BR.md) |
| Decisões arquiteturais | Contexto, decisão, alternativas e consequências | [ADR 0001](../backend/0001-monolito-modular.md) |

## Tipos de documento

### README do projeto

O README raiz é a página pública de entrada. Ele apresenta visão de produto,
estado atual, arquitetura em alto nível, início rápido, mapa da documentação,
roadmap e expectativas de contribuição. Deve apontar para detalhes, em vez de
duplicar cada especificação de módulo.

### README de trilha

Uma trilha descreve uma direção técnica duradoura, como Engenharia de Dados,
Estatística, IA ou Observabilidade. Pode existir antes do código, mas deve
identificar honestamente o trabalho planejado e definir evidências de progresso.

### README de módulo

Um documento de módulo fica próximo de uma implementação ou especificação de
produto concreta. Explica responsabilidades, contratos públicos, dependências,
comportamento em runtime, testes, regras de extensão e limitações atuais.

### Architecture Decision Record

Um ADR registra uma decisão que afeta vários módulos ou custa caro reverter.
Ele contém contexto, opção escolhida, alternativas, consequências e ações de
acompanhamento. ADRs descrevem decisões; READMEs explicam uso e escopo.

### Runbook

Um runbook é operacional: sintomas, verificações, comandos, correção segura,
rollback, escalonamento e evidências a coletar. Sistemas planejados não precisam
de runbooks fictícios; módulos operacionais precisam.

## Regras de fonte da verdade

- O comportamento em runtime é definido por código e testes; a documentação o explica.
- Contratos públicos pertencem à documentação do módulo e aos schemas da API.
- Decisões transversais pertencem aos ADRs.
- Dependências pertencem a `requirements/*.txt` e ao respectivo catálogo.
- Capacidades planejadas devem ser marcadas como **planejadas**.
- Uma afirmação de status deve apontar para código, testes, exemplo ou evidência operacional.

## Política bilíngue

Cada README principal de projeto, trilha e módulo possui duas versões:

- `README.md` para inglês;
- `README.pt-BR.md` para português brasileiro.

As duas versões devem preservar a mesma estrutura de seções e o mesmo sentido
técnico. Uma alteração só está completa quando ambos os documentos forem
atualizados. Nomes de bibliotecas, classes, protocolos e comandos permanecem
em sua forma técnica canônica.

## Padrão de escrita

Uma boa documentação do Atlas deve responder:

1. Qual problema este componente resolve?
2. O que está dentro e fora de sua fronteira?
3. Quais contratos ele expõe ou consome?
4. Como uma pessoa nova executa e verifica o componente?
5. Quais falhas, riscos e limitações importam?
6. O que está implementado e o que está apenas planejado?
7. Quais evidências demonstram qualidade?

Prefira exemplos concretos, links relativos, status explícito e diagramas curtos.
Evite promessas sem evidência, linguagem promocional copiada, siglas sem
explicação e arquiteturas que não correspondam ao repositório.

## Checklist de revisão

- [ ] As versões em inglês e português estão estruturalmente alinhadas.
- [ ] Links relativos resolvem a partir da localização do documento.
- [ ] Comandos correspondem ao layout atual do repositório.
- [ ] Comportamentos planejados e implementados estão claramente separados.
- [ ] Entradas, saídas, erros, segurança e privacidade são cobertos quando relevantes.
- [ ] Testes ou evidências são ligados aos comportamentos implementados.
- [ ] Nenhum secret, credencial, dado pessoal ou endpoint privado aparece.
- [ ] A trilha responsável e os módulos integrados estão conectados.

## Como adicionar documentação

1. Coloque conteúdo de visão geral no README do módulo mais próximo.
2. Adicione uma trilha apenas para uma direção técnica duradoura.
3. Crie um ADR quando uma decisão atravessar módulos ou for cara de reverter.
4. Adicione as duas versões de idioma na mesma alteração.
5. Conecte o novo documento a esta central ou ao catálogo apropriado.
6. Valide links Markdown e compare os headings entre idiomas.

## Estado atual da documentação

A arquitetura de documentação está estabelecida. A maioria das trilhas técnicas
está planejada; o backend FastAPI possui endpoints executáveis iniciais; o
PostgreSQL está disponível por Docker Compose; e o Mobile Lab possui uma
especificação detalhada de stack, mas ainda não tem código de aplicação.
