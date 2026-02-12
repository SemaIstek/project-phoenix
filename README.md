# 🔥 Project Phoenix

> Transforming climate data into living intelligence - An AI-powered climate risk analysis and economic strategy platform

[![AI Dev Days Hackathon](https://img.shields.io/badge/AI%20Dev%20Days-Hackathon%202026-blue)](https://github.com/SemaIstek/project-phoenix)
[![Azure](https://img.shields.io/badge/Azure-Deployed-0078D4)](https://azure.microsoft.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB)](https://www.python.org/)

## 🌍 Overview

In a world where climate crisis transforms into economic devastation, **Project Phoenix** turns static data into actionable intelligence. We don't just record past losses - we build roadmaps for the future.

### The Problem

For years, climate data has been trapped in spreadsheets. We only record past losses but have no roadmap to build the future. The gap between emissions, GDP, and climate damage costs trillions - but remains invisible to decision-makers.

### Our Solution

**Project Phoenix** leverages Microsoft's AI platform to create a **Council of Agents** that:
- 📊 Analyzes millions of rows of historical climate & economic data
- 🤖 Generates proactive risk scenarios using AI agents
- 💡 Delivers actionable economic strategies through an interactive dashboard
- 🛡️ Creates a financial shield for governments and institutions

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Power BI Dashboard                      │
│              (Copilot-enabled Interactive UI)               │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Backend                        │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────────┐
│                   Council of Agents                         │
│                   (Azure AutoGen)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Risk Analyst │→ │  Recovery    │→ │  Strategy    │     │
│  │    Agent     │  │  Architect   │  │    Agent     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────────┐
│                   Microsoft Fabric                          │
│              (Data Processing & Analytics)                  │
└─────────────────────────────────────────────────────────────┘
```

### Agent Responsibilities

1. **Risk Analyst Agent** 🔍
   - Processes historical climate damage data
   - Analyzes CO2 emissions vs GDP correlations
   - Identifies high-risk countries and sectors

2. **Recovery Architect Agent** 🏗️
   - Generates climate resilience scenarios
   - Models economic recovery pathways
   - Simulates intervention outcomes

3. **Strategy Agent** 📋
   - Synthesizes insights from other agents
   - Creates actionable policy recommendations
   - Generates financial allocation strategies

---

## 🚀 Tech Stack

### Hero Technologies (Hackathon Requirements)

- **Microsoft Agent Framework**: Azure AutoGen for multi-agent orchestration
- **Azure Services**: 
  - Microsoft Fabric (data processing)
  - Azure OpenAI (GPT-4 for agents)
  - Azure App Service (API hosting)
  - Azure Container Apps (agent runtime)
- **GitHub**: 
  - Repository management
  - GitHub Actions (CI/CD)
  - GitHub Copilot (development acceleration)

### Additional Technologies

- **Backend**: FastAPI (Python 3.11)
- **Data Processing**: Pandas, NumPy, Microsoft Fabric
- **AI/ML**: Azure AutoGen, LangChain, Azure OpenAI
- **Visualization**: Power BI, Plotly
- **Infrastructure**: Azure Bicep, Docker

---

## 📁 Project Structure

```
project-phoenix/
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Continuous Integration
│       └── azure-deploy.yml          # Azure deployment
├── agents/
│   ├── __init__.py
│   ├── risk_analyst.py               # Risk Analyst Agent
│   ├── recovery_architect.py         # Recovery Architect Agent
│   ├── strategy_agent.py             # Strategy Agent
│   ├── council.py                    # Agent orchestration
│   └── config.py                     # Agent configurations
├── api/
│   ├── __init__.py
│   ├── main.py                       # FastAPI application
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analysis.py               # Analysis endpoints
│   │   └── strategy.py               # Strategy endpoints
│   └── models/
│       ├── __init__.py
│       └── schemas.py                # Pydantic models
├── data/
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── climate_data.py           # Climate data processing
│   │   └── economic_data.py          # Economic data processing
│   ├── sample/
│   │   └── climate_damage_sample.csv # Sample dataset
│   └── fabric/
│       └── notebooks/                # Fabric notebooks
├── dashboard/
│   ├── powerbi/
│   │   └── phoenix_dashboard.pbix    # Power BI report
│   └── embedding/
│       └── app.py                    # Dashboard embedding app
├── infrastructure/
│   └── azure/
│       ├── main.bicep                # Main infrastructure
│       ├── app-service.bicep         # App Service config
│       └── parameters.json           # Deployment parameters
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   └── test_api.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   └── API.md
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.11+
- Azure subscription
- GitHub account
- VS Code with GitHub Copilot

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/SemaIstek/project-phoenix.git
cd project-phoenix
```
2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your Azure OpenAI credentials
```
5. **Run the API locally**
```bash
cd api
uvicorn main:app --reload
```
6. **Test the agents**
```bash
python -m agents.council
```

### Azure Deployment

Coming soon - automated deployment via GitHub Actions

---

## 🎯 Hackathon Alignment

### ✅ Core Requirements Met

- [x] **Hero Technology**: Azure AutoGen (Microsoft Agent Framework)
- [x] **Azure Deployment**: App Service + Container Apps + Fabric
- [x] **GitHub Development**: Public repository with Copilot integration
- [x] **Real-world Problem**: Climate risk & economic strategy

### 💡 Innovation Highlights

1. **Multi-Agent Council**: Novel orchestration of specialized AI agents
2. **Proactive Economics**: Shifts from reactive damage recording to predictive strategy
3. **Enterprise-Ready**: Scalable architecture using Microsoft Fabric
4. **Decision Support**: Interactive Copilot-enabled dashboard for policymakers

---

## 📊 Data Sources

- Climate damage data (Loss & Damage Database)
- CO2 emissions (Global Carbon Project)
- GDP & economic indicators (World Bank)
- Country risk indices (Custom aggregation)

---

## 🤝 Contributing

This is a hackathon project built for AI Dev Days Hackathon 2026. Contributions, ideas, and feedback are welcome!

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 👥 Team

Built with ❤️ for AI Dev Days Hackathon 2026

**From the ashes, we rise. Join us in building the future.**

---

## 🔗 Links

- [AI Dev Days Hackathon](https://github.com/topics/ai-dev-days-hackathon)
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/)
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)

---

**🔥 Project Phoenix - Transforming ashes into power, data into defense.**
