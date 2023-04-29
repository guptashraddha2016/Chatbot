import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an eassy about AI"}])
print(completion.choices[0].message.content)