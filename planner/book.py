import os
import requests
from langchain_google_vertexai import VertexAI


# Connect to resourse needed from Google Cloud
llm = VertexAI(model_name="gemini-1.5-flash-002")
BOOK_PROVIDER_URL =  os.environ.get("BOOK_PROVIDER_URL")

