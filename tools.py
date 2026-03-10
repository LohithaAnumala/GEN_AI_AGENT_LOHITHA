cat tools.py
from langchain.tools import Tool
#from langchain_rag import run_query
from rag import run_query

#Tool1 : Rag search for healthcare documents
#def medical_rag_tool(query:str):
#       return run_query(query)

#Tool 2 : Simple symptoms checker 
#def symptom_checker(symptom:str):
#       symptom = symptom.lower()
#
#       if "fever" in symptom and "Headache" in symptom:
#               return "Possible flu or viral infection. Please conslt doctor"
#       if "chest pain" in symptom:
#               return "Chest pain can be serious . seek immediate medical attention"
#       if "cough" in symptom:
#               return "Could be cold or respiratory infection"

#       return "Please consult healthcare professional"
#
#Tool 3 : Calculator 
#def calculator_tool(expression:str):
#       try:
#               return str(eval(expression))
#       except:
#               return "Invalid calculation."

#Register tools

#tools=[
#       Tool(
#               name="Healthcare Rag",
#               func=medical_rag_tool,
#               description="Use this tool to anser medical knowledge questions"
#),
#Tool(
#       name="symptom_Checker",
#       func=symptom_checker,
#       description="Use this tool when user asks about symptoms"
#),
#Tool(
#       name="Calculator",
#       func=calculator_tool,
#3      description="Use this tool for math calculations"
#)
#]
#*/
def calculator(query):
        try:
                return str(eval(query))
        except:
                return "Invalid calculation"

def symptom_checker(query):
        return "Possible cold or infection . please consult a doctor if sympotoms persists"

tools =[
        Tool(
                name="calculator",
                func=calculator,
                description = "useful for mathematical calculations"

                ),
        Tool(
                name="Symptom checker",
                func=symptom_checker,
                description= "Useful when describes health system like fever or cough"

        ),
        Tool(

                name="RAG SEarch",
                func = run_query,
                description ="Useful when answeing questions from healthcare documents"
        )
]
ubuntu@ip-172-31-2-71:~$ 
