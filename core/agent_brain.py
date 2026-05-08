import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class DataAgent:
    def __init__(self):
        # Model-agnostic setup
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            base_url="https://models.inference.ai.azure.com", 
            api_key=os.getenv("GITHUB_TOKEN")
        )

    def perform_rca(self, pipeline_name, error_logs):
        template = """
        You are an Expert Analytics Engineer. 
        Analyze the failure in the {pipeline_name} pipeline.
        
        Error Details: {error_logs}
        
        Provide a concise Root Cause Analysis and a recommended fix.
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm
        return chain.invoke({"pipeline_name": pipeline_name, "error_logs": error_logs}).content
