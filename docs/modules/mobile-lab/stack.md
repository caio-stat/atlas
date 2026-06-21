# Atlas Mobile Lab — Stack

O **Atlas Mobile Lab** é o módulo do projeto Atlas dedicado ao desenvolvimento mobile, automação mobile, integração com backend, funcionamento offline-first e uso de IA em dispositivos móveis.

O objetivo deste módulo é conectar a experiência prévia com Android/Java, evoluir para Kotlin moderno e criar aplicações móveis que consumam os serviços do Atlas, exibam dados, relatórios, alertas e recursos de inteligência artificial.

---

## 1. Objetivo do módulo

O Atlas Mobile Lab tem como objetivos:

* criar aplicações Android conectadas ao backend FastAPI do Atlas;
* construir apps offline-first com banco local;
* consumir APIs REST;
* exibir indicadores, relatórios e dashboards simplificados;
* receber notificações;
* integrar recursos de câmera, QR Code e sensores;
* testar aplicações móveis de forma automatizada;
* explorar IA embarcada ou integrada via API;
* criar ferramentas móveis úteis para suporte técnico, redes, dados e automação.

---

## 2. Aplicação principal: Atlas Pocket

A aplicação principal planejada para este módulo é o **Atlas Pocket**.

O Atlas Pocket será um aplicativo Android para acompanhar o ecossistema Atlas pelo celular.

Funcionalidades futuras:

* consultar status da API Atlas;
* consultar a versão atual do backend;
* visualizar datasets disponíveis;
* acompanhar pipelines;
* exibir dashboards simplificados;
* receber alertas;
* consultar relatórios;
* conversar com agentes de IA do Atlas;
* funcionar parcialmente offline;
* sincronizar dados locais com o backend;
* usar câmera e QR Code futuramente.

---

## 3. Stack Android principal

### Kotlin

Linguagem principal recomendada para o desenvolvimento Android moderno.

Uso no Atlas:

* desenvolvimento do Atlas Pocket;
* criação de telas;
* integração com APIs;
* lógica de sincronização;
* recursos offline-first.

---

### Jetpack Compose

Framework moderno para criação de interfaces Android declarativas.

Uso no Atlas:

* criação da interface do Atlas Pocket;
* telas de status;
* dashboards simples;
* formulários;
* listas de datasets;
* telas de relatórios;
* chat com agentes de IA.

---

### Room

Biblioteca de persistência local baseada em SQLite.

Uso no Atlas:

* cache local de dados;
* funcionamento offline;
* armazenamento de relatórios;
* armazenamento de configurações;
* sincronização posterior com o backend.

---

### DataStore

Solução moderna para armazenar preferências e configurações locais.

Uso no Atlas:

* salvar URL da API;
* salvar token local futuramente;
* salvar preferências do usuário;
* controlar modo offline/online;
* guardar configurações simples do app.

---

### Retrofit

Cliente HTTP para consumir APIs REST.

Uso no Atlas:

* consumir endpoints do backend FastAPI;
* buscar status da API;
* consultar datasets;
* enviar dados coletados pelo app;
* buscar relatórios e indicadores.

---

### OkHttp

Cliente HTTP usado em conjunto com Retrofit.

Uso no Atlas:

* logs de requisições;
* interceptadores;
* autenticação futura;
* controle de timeout;
* headers personalizados.

---

### WorkManager

Biblioteca para execução de tarefas em segundo plano.

Uso no Atlas:

* sincronizar dados em background;
* enviar registros pendentes;
* atualizar relatórios periodicamente;
* executar tarefas quando houver internet;
* agendar verificações de status.

---

### Hilt

Biblioteca de injeção de dependência.

Uso no Atlas:

* organizar dependências;
* separar camadas;
* facilitar testes;
* injetar repositórios, serviços e clientes HTTP.

---

### Navigation Compose

Biblioteca para navegação entre telas usando Jetpack Compose.

Uso no Atlas:

* tela inicial;
* tela de status;
* tela de datasets;
* tela de relatórios;
* tela de configurações;
* tela de chat;
* tela de suporte.

---

### CameraX

Biblioteca moderna para uso de câmera no Android.

Uso futuro no Atlas:

* leitura de QR Code;
* registro fotográfico de equipamentos;
* captura de documentos;
* apoio ao módulo de suporte;
* integração com OCR e IA visual.

---

### ML Kit

Kit de recursos de machine learning para dispositivos móveis.

Uso futuro no Atlas:

* leitura de texto em imagens;
* leitura de QR Code;
* reconhecimento de elementos visuais;
* recursos de IA embarcada.

---

### Firebase Cloud Messaging

Serviço para notificações push.

Uso futuro no Atlas:

* alertas de pipeline;
* alertas de falha no backend;
* alertas de novos relatórios;
* notificações de automações;
* avisos do Atlas Support Lab.

---

## 4. Python para suporte ao Mobile Lab

Embora o desenvolvimento Android principal seja feito em Kotlin, Python será usado no Atlas Mobile Lab para automação, testes, prototipagem e integração.

Bibliotecas planejadas:

* appium-python-client;
* adb-shell;
* uiautomator2;
* pytest;
* pytest-html;
* requests;
* httpx;
* qrcode;
* pillow;
* python-dotenv.

Usos:

* automatizar testes em apps Android;
* executar comandos ADB via Python;
* instalar APKs automaticamente;
* coletar logs;
* tirar screenshots;
* gerar QR Codes;
* validar endpoints consumidos pelo app;
* gerar relatórios de teste.

---

## 5. Mobile AI

O Atlas Mobile Lab também terá espaço para experimentos com IA em dispositivos móveis.

Bibliotecas e tecnologias planejadas:

* TensorFlow Lite;
* ONNX;
* ONNX Runtime;
* ML Kit;
* OpenCV;
* modelos embarcados leves;
* integração com APIs de IA do backend.

Possibilidades:

* classificação simples em dispositivo;
* leitura de imagens;
* OCR;
* reconhecimento de documentos;
* chat com agentes remotos;
* cache de respostas;
* inferência local em modelos pequenos.

---

## 6. Mobile Support Tools

Uma aplicação futura importante será o **Atlas Support Pocket**.

O Atlas Support Pocket será um app mobile voltado para suporte técnico, redes e atendimento em campo.

Funcionalidades possíveis:

* checklist de atendimento;
* cadastro de máquina;
* registro de patrimônio;
* fotos do equipamento;
* teste de conectividade;
* registro de IP, setor e observações;
* geração de relatório final;
* sincronização com backend;
* histórico offline de atendimentos;
* QR Code para identificação de equipamentos.

Esse app conecta diretamente:

* suporte técnico;
* redes;
* automação;
* backend;
* dados;
* documentação;
* portfólio.

---

## 7. Integração com o backend Atlas

Fluxo esperado:

FastAPI Backend
↓
Retrofit / OkHttp
↓
Repository Android
↓
Room / DataStore
↓
ViewModel
↓
Jetpack Compose UI

O app mobile não deve acessar diretamente o banco remoto. Ele deve se comunicar com a API Atlas.

---

## 8. Arquitetura Android recomendada

Camadas recomendadas:

* UI;
* ViewModel;
* Use Cases;
* Repository;
* Local Data Source;
* Remote Data Source;
* Models / DTOs.

Estrutura futura sugerida:

apps/mobile/atlas-pocket/
├── app/
│   ├── data/
│   ├── domain/
│   ├── presentation/
│   ├── di/
│   └── core/

---

## 9. Primeira entrega do Mobile Lab

A primeira entrega deve ser simples:

* criar app Android Kotlin;
* criar tela inicial;
* consumir endpoint `/health`;
* consumir endpoint `/version`;
* exibir status da API;
* exibir versão do backend;
* criar README do módulo mobile.

Resultado esperado:

O usuário abre o app e vê:

* Atlas API: online;
* versão: 0.1.0;
* ambiente: local/dev.

---

## 10. Roadmap

### Fase 1 — Integração básica

* app Android Kotlin;
* tela inicial;
* consumo de `/health`;
* consumo de `/version`.

### Fase 2 — Offline-first

* Room;
* cache local;
* DataStore;
* sincronização básica.

### Fase 3 — Dados e relatórios

* listar datasets;
* visualizar indicadores;
* abrir relatórios;
* salvar relatórios offline.

### Fase 4 — Suporte técnico

* checklist de atendimento;
* cadastro de equipamento;
* fotos;
* relatório de suporte;
* sincronização com backend.

### Fase 5 — IA e agentes

* chat com agente Atlas;
* resumo de relatórios;
* consulta a documentos;
* integração com RAG.

### Fase 6 — Mobile AI

* OCR;
* QR Code;
* ML Kit;
* modelos leves embarcados.

---

## 11. Critérios de qualidade

O módulo mobile deve buscar:

* clareza;
* código organizado;
* arquitetura em camadas;
* integração limpa com API;
* funcionamento offline quando fizer sentido;
* testes automatizados;
* valor real para suporte, dados e IA;
* documentação suficiente;
* valor de portfólio.

---

## 12. Tecnologias principais

Resumo da stack:

* Kotlin;
* Jetpack Compose;
* Room;
* DataStore;
* Retrofit;
* OkHttp;
* WorkManager;
* Hilt;
* Navigation Compose;
* CameraX;
* ML Kit;
* Firebase Cloud Messaging;
* Appium;
* ADB;
* Python para automação e testes.
