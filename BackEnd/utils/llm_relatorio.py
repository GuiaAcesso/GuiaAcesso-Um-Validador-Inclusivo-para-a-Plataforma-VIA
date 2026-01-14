import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def gerar_relatorio_llm(prompt: str) -> str:
    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=prompt,
    )
    return response.output_text
