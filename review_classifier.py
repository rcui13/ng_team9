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

reviewQuality("football", ["My son loves it", "It taste good", "whefhwefhwue", "Text me", "My uncle loves it", "Don't buy this, it broke in one day"])
