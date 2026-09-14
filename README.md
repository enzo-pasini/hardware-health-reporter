# Hardware Health Reporter

Programa em Python que gera um relatório do consumo de componentes do computador (CPU, RAM e disco) e emite alertas com base no nível de uso.

## Objetivo

Fiz esse projeto para testar meus conhecimentos de Python e do fluxo Git/GitHub (gestão de commits, criação de README, ambiente virtual e requirements.txt) de forma aplicada.

## Funcionalidades

- Coleta em tempo real de métricas de CPU, RAM e uso de disco via `psutil`
- Classifica cada métrica em três níveis de alerta (Normal, Atenção, Crítico) com base em limites predefinidos
- Exibe um relatório formatado no console a cada execução
- Registra o histórico de cada execução em um arquivo `.csv` para acompanhamento ao longo do tempo

## Estrutura do projeto

hardware_health_reporter/
├── main.py # orquestra a execução do programa
├── snapshot.py # classe Snapshot (representa uma coleta)
├── collector.py # classe HardwareCollector (coleta via psutil)
├── evaluator.py # classe HealthEvaluator (classifica os níveis)
├── reporter.py # exibe o relatório no console
├── historic.py # classe LogWriter (salva histórico em csv)
├── requirements.txt
├── README.md
└── .gitignore


## Como rodar

**1. Clone o repositório**
```bash
git clone <url-do-repo>
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute o programa**
```bash
python main.py
```

## Decisões técnicas

**Por que o projeto foi estruturado em classes:** mesmo o projeto sendo simples, fiz dessa forma para treinar programação orientada a objetos.

**Por que os limites de alerta são fixos:** os limites de Atenção e Crítico são definidos diretamente no código, não configuráveis pelo usuário nesta versão para evitar erros ou alertas equivocados que seriam gerados caso o usuário colocasse um limite de alerta inadequado.

**Por que o histórico é salvo em CSV, e não em um banco de dados:** para manter menor complexidade nessa primeira versão do projeto.

## Possíveis melhorias futuras

- Agendar a execução periódica do programa via agendador nativo do sistema operacional (Agendador de Tarefas no Windows, cron no Linux/Mac)
- Migrar o armazenamento do histórico de `.csv` para um banco de dados, permitindo consultas mais robustas conforme o volume de dados cresce