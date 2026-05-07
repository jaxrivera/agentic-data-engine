# Agentic Data Engine 🚀
### Autonomous Pipeline Monitoring & AI-Driven Root Cause Analysis (RCA)

A professional-grade data observability engine built to detect "Data Silence" in Cloud Data Warehouses and autonomously diagnose technical failures using Generative AI.

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Core Features](#-core-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [How it Works](#-how-it-works)
- [Interview & Strategy Notes](#-interview--strategy-notes)

---

## 🌟 Project Overview
Modern data teams are often overwhelmed by "pipeline fatigue"—receiving alerts for failures without context. The **Agentic Data Engine** solves this by moving from passive alerting to active diagnosis. 

Instead of just alerting that a table is empty, this system:
1. Proactively checks Snowflake metadata for anomalies.
2. Extracts logs from failed integration points.
3. Consults a **LLM-based Senior Data Engineer Agent** to provide a human-readable Root Cause Analysis (RCA).

---

## 🏗 System Architecture
The engine follows a modular, agentic feedback loop:

1. **Snowflake Utility Layer**: Manages infrastructure provisioning and metadata polling.
2. **Logic Orchestrator**: Evaluates data health and determines if an AI consultation is required.
3. **AI Reasoning Layer**: A LangChain-powered agent that uses GPT-4o-mini to interpret logs and suggest SQL/IAM remediations.



---

## 🚀 Core Features
- **Idempotent Infrastructure**: Automatically provisions Snowflake Databases, Schemas, and Tables if they are missing.
- **Data Silence Detection**: Specifically triggers when row counts drop to zero or expected updates fail.
- **Model Agnostic AI**: Utilizes LangChain to support multiple LLM providers (OpenAI, GitHub Models, Azure).
- **Actionable RCA**: Outputs are formatted to include the specific **Root Cause** and the **Recommended Action** (including code snippets).

---

## 🛠 Tech Stack
- **Languages**: Python 3.10+
- **Data Warehouse**: Snowflake
- **AI Framework**: LangChain
- **LLM**: GPT-4o-mini (Inference via GitHub Models)
- **Environment**: Virtual Environments (venv), Dotenv for Secret Management

---

## 🏁 Getting Started

### 1. Prerequisites
- A Snowflake Account
- A GitHub Personal Access Token (for Model Inference)

### 2. Installation
```bash
git clone [https://github.com/jonatanax/agentic-data-engine.git](https://github.com/jonatanax/agentic-data-engine.git)
cd agentic-data-engine
python3 -m venv venv
source venv/bin/activate
pip install snowflake-connector-python langchain-openai python-dotenv
