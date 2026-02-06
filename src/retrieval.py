%%writefile wikipedia-rag-agent/src/retrieval.py
"""
This file retrieves the most relevant chunks.
"""

def retrieve_context(vectorstore, question, k=3):
    docs = vectorstore.similarity_search(question, k=k)
    return "\n\n".join(doc.page_content for doc in docs)
