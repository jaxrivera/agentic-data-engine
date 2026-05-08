# Agentic Data Engine 🚀

A modular Analytics Engineering framework that uses LLMs to automate Root Cause Analysis (RCA) for data pipeline failures in the Azure/Snowflake stack.

## 🏗️ Architecture
- **/core**: Logic for LLM interaction (LangChain) and Snowflake connectivity.
- **/azure_functions**: Serverless entry points for triggering AI diagnostics via HTTP.
- **/orchestration**: Airflow DAGs that monitor data health and invoke the agent on failure.

## 🛠️ Tech Stack
- **Language:** Python 3.10
- **Cloud:** Azure (Functions, Monitor)
- **Data:** Snowflake
- **AI:** LangChain + GPT-4o
- **Orchestration:** Airflow

## 🚀 Getting Started
1. Clone the repo.
2. Create a venv and run `pip install -e .`
3. Configure your `.env` with GITHUB_TOKEN and SNOWFLAKE_CREDENTIALS.
4. Run `python3 local_test.py` to simulate a pipeline failure and AI diagnosis.
