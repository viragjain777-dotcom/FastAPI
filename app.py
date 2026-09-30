import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT_OLLAMA")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain FastAPI App", 
    version="1.0.0", 
    description="A simple Langchain FastAPI app")

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
 )

model=ChatOpenAI()
## Ollama Model
llm=Ollama(model="gemma3:4b")

prompts1=ChatPromptTemplate.from_template("Write me an essay: {topic} with 100 words")
prompts2=ChatPromptTemplate.from_template("Write me an poem about: {topic} for a 5 year old child")

add_routes(app, prompts1|model, path="/essay")
add_routes(app, prompts2|llm, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)