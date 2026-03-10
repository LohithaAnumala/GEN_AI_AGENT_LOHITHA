 cat rag.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


#Load documents
with open("data/docs.txt") as f:
        text = f.read()
#CHUNKING
chunk_size=200
chunks=[text[i:i+chunk_size] for i in range(0,len(text),chunk_size)]
docs=chunks
#creat embeddings
dimension=384
embeddings=np.random.rand(len(docs),dimension).astype("float32")
#FAISS index

index=faiss.IndexFlatL2(dimension)
index.add(embeddings)


def run_query(query,top_k=3):
        query_embedding=np.random.rand(1,dimension).astype("float32")
        distance,indices=index.search(query_embedding,top_k)
        results=[]
        for idx in indices[0]:
                results.append(docs[idx])
        return " ".join(results)
        print("Retrieved:",results)
ubuntu@ip-172-31-2-71:~$ 
