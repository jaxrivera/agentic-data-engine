from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime
import json

with DAG(
    'azure_agentic_observability',
    schedule_interval='@daily',
    start_date=datetime(2026, 5, 1),
    catchup=False
) as dag:

    # Trigger the Azure Function RCA Service on Failure
    trigger_azure_rca = SimpleHttpOperator(
        task_id='trigger_ai_diagnostic_service',
        http_conn_id='azure_function_rca',
        endpoint='api/rca_service',
        method='POST',
        data=json.dumps({
            "pipeline": "FCT_REVENUE_REPORT",
            "logs": "Azure Blob Error: Authentication failed for storage account."
        }),
        headers={"Content-Type": "application/json"},
    )
