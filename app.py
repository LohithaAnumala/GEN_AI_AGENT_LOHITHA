$ cat app.py
from fastapi import FastAPI
from groq import Groq
import os
from dotenv import load_dotenv
from rag import run_query
from agent import run_agent
import time
#load_dotenv()

app=FastAPI()

#import requests

#client=Groq(api_key=os.getenv("GROQ_API_KEY"))
#LOG_FILE = "logs/requests.logs"

@app.get("/")
def home():
        return {"status":"RAG AGent is running"}

@app.get("/ask")
def ask(query:str):
        start = time.time()
        answer = run_agent(query)
        latency = time.time()-start
        return{"query":query,
        "answer":answer,
        "latency_seconds":latency
        }
