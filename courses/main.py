import os
import json
import time
import base64
from google.cloud import pubsub_v1, storage
import functions_framework
from audio import breakup_sessions 

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")

