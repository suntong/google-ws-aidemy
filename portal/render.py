import os
import json
import random
from google.cloud import storage

from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage


llm = VertexAI(model_name="gemini-2.0-flash-thinking-exp-01-21")

