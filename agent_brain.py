import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

class DataAgent:
    def __init__(self):
        # We use the OpenAI class but point it to GitHub's Models API
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("GITHUB_TOKEN"),
            base_url="https://models.inference.ai.azure.com",
            temperature=0
        )

    def perform_rca(self, pipeline_status, error_log):
        template = """
        You are a Senior Data Engineer. 
        Analyze the failure and provide a Root Cause and Recommended Action.
        
        PIPELINE STATUS: {pipeline_status}
        ERROR LOG: {error_log}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm
        
        response = chain.invoke({
            "pipeline_status": pipeline_status,
            "error_log": error_log
        })
        return response.content

if __name__ == "__main__":
    agent = DataAgent()
    status = "FAILURE - Table: USER_EVENTS"
    logs = "Error: Snowflake Load failed. Reason: S3 Access Denied."
    
    print("--- AI AGENT ROOT CAUSE ANALYSIS (GITHUB MODELS) ---")
    print(agent.perform_rca(status, logs))
