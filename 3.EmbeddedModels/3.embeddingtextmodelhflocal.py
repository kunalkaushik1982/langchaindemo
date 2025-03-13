from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text="Delhi is the Capital of India"

# vector = embedding.embed_query(text)
# print(str(vector))

documents =[
    "New Delhi is the Capital of India",
    "Tokyo is the Capital of Japan",
    "Paris is the Capital of France"
]
vectors= embedding.embed_documents(documents)

print(str(vectors))