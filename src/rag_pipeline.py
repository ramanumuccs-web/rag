%%writefile wikipedia-rag-agent/src/rag_pipeline.py
"""
This file runs the full RAG pipeline.
"""

from retrieval import retrieve_context
from prompts import build_rag_prompt

def answer_question(vectorstore, question, llm_call):
    context = retrieve_context(vectorstore, question)
    prompt = build_rag_prompt(context, question)
    return llm_call(prompt)
