from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents =[
    "New Delhi is the Capital of India",
    "Tokyo is the Capital of Japan",
    "Paris is the Capital of France"
]
results= embedding.embed_documents(documents)
print(str(results))