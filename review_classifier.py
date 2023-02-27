import openai

def reviewQuality(product_name, review_texts):
  openai.api_key = "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"
  
  prompt = "Classify whether these are Real or Fake reviews for an Amazon product called " + product_name + ":\n\n" 

  review_number = 1
  for review_text in review_texts:
    prompt += str(review_number) + ". " + "\"" + review_text + "\"" + "\n"
    review_number += 1

  print(prompt)

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  print(response)
