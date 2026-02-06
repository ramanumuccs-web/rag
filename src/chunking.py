%%writefile wikipedia-rag-agent/src/chunking.py
"""
This file splits large text into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text: str, chunk_size=800, overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)
