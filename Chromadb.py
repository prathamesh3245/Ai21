import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name="prathmesh_collection")

collection.add(
    ids=["1", "2", "3"],
    documents=["Apple is a fruit", "Python is a programming language", "Football is a sport"]
)

results = collection.query(
    query_texts=["What is Apple?"],
    n_results=1
)

print(results)
# print(client.list_collections())