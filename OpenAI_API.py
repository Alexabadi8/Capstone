import openai

openai.api_key = "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"
prompt = "answer me with a philosophical question"
response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=prompt, max_tokens=6) 
print("response: " + response)