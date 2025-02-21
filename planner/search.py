import os
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from onramp_workaround import get_next_region

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")  # Get project ID from env


