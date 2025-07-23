import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This loads the .env file into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model = 'gpt-4o',
    messages =[
        {"role": "system", "content":"You are helpful assistant"},
        {
            "role": "user",
            "content":"Write a limerick about the Python programming language."
        }
    ]

)

response = completion.choices[0].message.content
print(response)