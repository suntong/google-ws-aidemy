import os
import json
import asyncio
import wave 
import time

import functions_framework
import soundfile as sf
from google import genai
from google.cloud import storage  
from google.genai.types import (
    Content,
    LiveConnectConfig,
    SpeechConfig,
    VoiceConfig,
    PrebuiltVoiceConfig,
    Part,
)

MODEL_ID = "gemini-2.0-flash-exp"
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
BUCKET_NAME = os.environ.get("COURSE_BUCKET_NAME", "")





