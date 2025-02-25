import os
import json
import base64
import random
from google.cloud import storage
import functions_framework

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver

from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from gemini import gen_assignment_gemini,combine_assignments
from deepseek import gen_assignment_deepseek
from typing import TypedDict

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
ASSIGNMENT_BUCKET = os.environ.get("ASSIGNMENT_BUCKET","")


class State(TypedDict):
    teaching_plan: str
    model_one_assignment: str
    model_two_assignment: str
    final_assignment: str
