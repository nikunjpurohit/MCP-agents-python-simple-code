import json
import os

import requests
from openai import OpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

