import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import TypedDict

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "")


class State(TypedDict):
    teaching_plan: str
    model_one_assignment: str
    model_two_assignment: str
    final_assignment: str
