import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()  # This loads the .env file into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import os

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --------------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# --------------------------------------------------------------

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

# --------------------------------------------------------------
# Step 2: Call the model
# --------------------------------------------------------------
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

# --------------------------------------------------------------
# Step 3: Parse the response
# --------------------------------------------------------------
event = completion.choices[0].message.parsed
print(event.name)
print(event.date)
print(event.participants)

