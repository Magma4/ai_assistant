import openai

openai.api_key = "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"

response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = "Life is like a box of chocolates."
)

print(response["choices"][0]["text"])
