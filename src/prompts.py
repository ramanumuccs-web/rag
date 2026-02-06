%%writefile wikipedia-rag-agent/src/prompts.py
"""
This file contains prompts for the AI.
"""

def build_rag_prompt(context, question):
    return f"""
Use ONLY the context below.
If the answer is not present, say:
"I don’t know from the provided text."

Context:
{context}

Question:
{question}

Answer:
"""
