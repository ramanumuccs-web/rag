%%writefile wikipedia-rag-agent/src/router.py
"""
This file decides if a question is clear or not.
"""

def route_question(question):
    if len(question.split()) < 4:
        return "CLARIFY"
    return "RETRIEVE"
