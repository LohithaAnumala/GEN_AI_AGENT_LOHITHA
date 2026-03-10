from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_groq import ChatGroq
from tools import tools
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

llm=ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")

)
#print("API_KEY":os.getenv("GROQ_API_KEY"))

agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5
)

def run_agent(query:str):
        response=agent.run(query)
        return response
ubuntu@ip-172-31
