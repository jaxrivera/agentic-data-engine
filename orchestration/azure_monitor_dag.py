from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json

default_args = {
    'owner': 'analytics_eng',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'azure_data_health_monitor',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2026, 5, 1),
    catchup=False
) as dag:

    def check_snowflake_connection():
        print("Checking Snowflake connectivity on Azure...")

    task_check_conn = PythonOperator(
        task_id='check_connection',
        python_callable=check_snowflake_connection
    )

    # This task calls our AI Function if something fails
    task_ai_rca = SimpleHttpOperator(
        task_id='ai_agent_diagnosis',
        http_conn_id='azure_function_rca',
        endpoint='api/rca_service',
        method='POST',
        data=json.dumps({"pipeline": "PROD_REVENUE_LOAD", "logs": "Access Denied"}),
        trigger_rule='one_failed' 
    )

    task_check_conn >> task_ai_rca
