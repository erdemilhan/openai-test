
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

prompt ="hello!"

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message)