import os

import langchain_community
from langchain_community.document_loaders import DirectoryLoader , TextLoader
from langchain.prompts import ChatPromptTemplate , MessagesPlaceholder

from langchain.chat_models import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOpenAI

import sqlite3
import updateSQL as sql

import openai
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_core.tools import tool
from langchain.agents import create_openai_functions_agent, AgentExecutor

from langchain_community.utilities import SQLDatabase

openai.api_key = open("key","r").read()
CHROMA_PATH = "chroma"
SQL_PATH = "backend.py"
print("backend loaded")
os.environ["OPENAI_API_KEY"] = openai.api_key

#___________________________________open DB_________________________________
embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory = CHROMA_PATH, embedding_function = embedding_function)

def lookup_doc(query):
    k=2
    results = db.similarity_search_with_relevance_scores(query,k=k)
    #print(results)
    if len(results) ==0 or results[0][1] < 0.3:
        print(results[i][1] for i in range(k))
        print("no results found for query: " , query)
        return 0
    else: return results
    
    
    
#____________________________ Prompt Formatting______________________________________
#print(lookup_doc("where can i find a good mountain resort"))

PROMPT_TEMPLATE = """
Answer the question only based on the following context:
{context}
---

Answer the question based on the above decription , do not mention the word context or document in your answer: {query}
"""
def formatQuery(query):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in lookup_doc(query)])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context = context_text, query = query)
    #print(prompt)
    return prompt


#__________________________ Query in case of Document Search__________________________
@tool
def docQuery(query):
    """answer any questions about the  hotels, properties or terms , policies and conditions of the company

    Args:
        query (str): a question about hotels , resorts or any terms and conditions about cancellations or policies etc

    Returns:
        str: THe summary and hotel/resort documents that was asked
    """
    model = ChatOpenAI()
    response_text = model.predict(formatQuery(query))
    print(response_text)
    return response_text

#___________________________________ SQL Query ________________________________________

sqlDB = SQLDatabase.from_uri("sqlite:///ownership.db")

@tool
def sqlQuery(query) ->str:
    """Get any information about existing bookings or timeshare ownership of people by checking the SQL database"""
    
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = create_sql_query_chain(model, sqlDB)
    response = chain.invoke({"question": query})
    print(response)
    return response

#____________________________________ SQL Update_________________________________________

@tool
def sqlUpdate(query) ->str:
    """Create a booking for resort ownership. the bookings added MUST be in the database already"""
    global sqlDB
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = create_sql_query_chain(model, sqlDB)
    response = chain.invoke({"question": query})
    #sql.execute(response)
    print(response, " - Update")
    return response

#______________________________________Tool Description___________________________________



#_______________________________________ Create  Agent __________________________________

tools = [sqlQuery,docQuery,sqlUpdate]
zofLLM = ChatOpenAI(model="gpt-3.5-turbo")
zofPrompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an assistant, zofia, for NyaaSaki Timeshares. you will be asked about resorts , hotels or timeshares and may be asked to book said resorts or timeshares. only use the tools provided and do not answer from other databases",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
zofia = create_openai_functions_agent(zofLLM , tools , zofPrompt )

#__________________ Executor____________________

zofia_bot = AgentExecutor(agent=zofia,tools=tools)



#__________________________________ Request from chatbot __________________________________
def req(query):
    result = zofia_bot.invoke({"input": query})
    return result["output"]
#docQuery("what resort is good in the desert")
