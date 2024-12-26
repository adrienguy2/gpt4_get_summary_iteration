import prompts
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

text = prompts.text
prompt = prompts.build_prompt(text)

messages=[
    {"role": "system", "content": prompt}
]

def get_summary():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )
    return completion.choices[0].message.content

print(get_summary())