import openai

openai.api_key = "API-KEY"

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # or "gpt-4"
    messages=[{"roll":"user", "content": "Hello, ChatGPT!"}],
    max_token = 100,
    temperature = 1,
    top = .5,
    stop = ["\n"]

)

print(response.choices[0].message["content"])

 
 
