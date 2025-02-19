import os
from google import genai
from typing import TypedDict

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
MODEL_ID = "gemini-2.0-flash-001" 

class State(TypedDict):
    teaching_plan: str
    model_one_assignment: str
    model_two_assignment: str
    final_assignment: str

