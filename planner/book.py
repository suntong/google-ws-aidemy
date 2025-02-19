import os
import requests
from langchain_google_vertexai import VertexAI


# Connect to resourse needed from Google Cloud
llm = VertexAI(model_name="gemini-2.0-flash-001")
BOOK_PROVIDER_URL =  os.environ.get("BOOK_PROVIDER_URL")

