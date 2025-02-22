import os
import json
import random
from google.cloud import storage

from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from onramp_workaround import get_next_region

def render_assignment_page():
    return ""
