import os
import openai


openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Classify whether these are real or fake reviews:\n + 1.ewfawefaf\n + 2.The product licks really good.\n + 3.The product taste really good.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)
