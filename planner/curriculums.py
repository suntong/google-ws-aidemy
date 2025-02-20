import os
import base64
import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes
import pg8000


project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
location = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
instance_name = os.environ.get("INSTANCE_NAME") 
instance_connection_name = f"{project_id}:{location}:{instance_name}"
print(f"--------------------------->Instance connection name: {instance_connection_name}")



