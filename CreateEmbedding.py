import os

import langchain_community
from langchain_community.document_loaders import DirectoryLoader , TextLoader

import openai
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

openai.api_key = open("key","r").read()
PATH = "BackendData"
CHROMA_PATH = "chroma"
print("hello")
os.environ["OPENAI_API_KEY"] = openai.api_key
#___________________________________ File Loader ________________________________________

def load_docs():
    loader = DirectoryLoader(PATH , glob = "*.md",loader_cls=TextLoader)
    documents = loader.load()
    return documents

doc = load_docs()
print(len(doc)," documents loaded")

#___________________________________ Embedder ___________________________________________
#if not os.path.exists(CHROMA_PATH):
db = Chroma.from_documents(documents=doc, embedding=OpenAIEmbeddings(),persist_directory = CHROMA_PATH)

print(" Vectors in chroma database")
db.persist()
