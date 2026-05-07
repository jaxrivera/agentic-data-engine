import azure.functions as func
import json
import os
import sys

# Path adjustment for Azure environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from core.agent_brain import DataAgent

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function trigger. 
    Can be called via an Azure Data Factory Web Activity or Airflow.
    """
    try:
        req_body = req.get_json()
        pipeline = req_body.get('pipeline', 'Azure_Data_Pipeline')
        logs = req_body.get('logs', 'No logs captured.')

        agent = DataAgent()
        analysis = agent.perform_rca(pipeline, logs)

        return func.HttpResponse(
            json.dumps({"analysis": analysis, "status": "Success"}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
