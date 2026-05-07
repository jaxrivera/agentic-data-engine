import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Use the explicit model path
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest")

response = llm.invoke("Say 'System Ready'")
print(response.content)
