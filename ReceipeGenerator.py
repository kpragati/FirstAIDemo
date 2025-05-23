import openai

openai.api_key = "$API_KEY"

#recepe_generator()
ingredients = []

while True:
    ingradient = input("Please Enter Ingredients. Enter done once its complete.")
    if ingradient.lower() == "done":
        break

    ingredients.append(ingradient)

def recepe_generator(ingradients):
    message = []

    for ingredient in ingredients:
        message.append({"role":"user", "content":ingredient})
     
    message.extend(
          [{"role" : "system", "content" : "direct, point"},
           {"role" : "assistent", "content" : "you are high end chef. You are generate a receipe in given ingredients"}]
      )

    response = openai.ChatCompletion.create(
       model = "gpt-4o",
       message = message,
       max_tokens = 300,
       temperature = 0.9
    )
    return response.choices[0].messages.content

print(recepe_generator(ingredients))
