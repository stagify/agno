from fastapi import FastAPI
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os

app = FastAPI()

# inicializa o Agno com modelo OpenAI
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True,
)

@app.get("/")
def root():
    return {"message": "Agno rodando no Railway 🚀"}

@app.get("/ask")
def ask(q: str):
    resposta = agent.run(q)
    return {"resposta": resposta}
