import os
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")  # Get project ID from env
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")

