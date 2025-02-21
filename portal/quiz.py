import json
import os
from langchain_google_vertexai import VertexAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class QuizQuestion(BaseModel):
    question: str = Field(description="The question itself")
    options: list[str] = Field(description="List of options", min_items=4, max_items=4)
    answer: str = Field(description="The correct answer letter (A, B, C, or D)")


# ENV SETUP
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")  # Get project ID from env




