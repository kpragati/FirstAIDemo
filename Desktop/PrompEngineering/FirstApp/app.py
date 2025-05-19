from openai import OpenAI
import os


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) #After Export a key

response = client.chat.completions.create(
    model="gpt-4o",  # or "gpt-4"
    messages=[{"roll":"user", "content": "Hello, ChatGPT!"}],
    max_tokens = 100,
    temperature = 1,
    stop = ["\n"]

)

print(response.choices[0].message["content"])

 
 
