import openai
import re
# Takes an array of review_texts and returns an array of either Real or Fake
def reviewQuality(product_name, review_texts):
  # This is the key from openai
  openai.api_key = "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"
  
  # This is the prompt that will generate if a review is real or fake
  prompt = "Classify whether these are Real or Fake reviews for an Amazon product called " + product_name + ":\n\n" 

  # Inputs all reviews to be analyzed
  review_number = 1
  for review_text in review_texts:
    prompt += str(review_number) + ". " + "\"" + review_text + "\"" + "\n"
    review_number += 1

  # Sends the review to openai to be analyzed
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  # Takes the returned response from openai and extracts information with regex to 
  # tell if review is real or fake
  text = response["choices"][0]["text"]
  reviewTypeArray = re.findall("Fake|Real", text)

  return reviewTypeArray

# Example of how to use this
# print(reviewQuality("football", ['My son loves this', 'This taste good']))
