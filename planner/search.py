import os
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")  # Get project ID from env
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

model_id = "gemini-2.0-flash-001"
