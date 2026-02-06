%%writefile wikipedia-rag-agent/src/load_wikipedia.py
"""
This file downloads Wikipedia text for ONE topic.
"""

import requests
from urllib.parse import quote

def load_wikipedia_text(topic: str) -> str:
    """
    Download plain Wikipedia text using REST API.
    Works in Google Colab.
    """
    title = quote(topic.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/plain/{title}"

    response = requests.get(url)
    response.raise_for_status()

    return response.text
