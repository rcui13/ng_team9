import openai
import re
from review import Review

# Takes an array of review_texts and returns an array of either Real or Fake
def reviewQuality(product_name, reviews: list[Review]):
    # This is the key from openai
    with open("key.txt", "r") as f:
        openai.api_key = f.read()

    # This is the prompt that will generate if a review is real or fake
    prompt = "Classify whether these are Real or Fake reviews for an Amazon product called " + \
        product_name + ":\n\n"

    # Inputs all reviews to be analyzed
    review_number = 1
    for review in reviews:
        review_text = review.text

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

    isReal = []

    # Converts reviewTypeArray to boolean values
    for reviewType in reviewTypeArray:
        if reviewType == 'Real':
            isReal.append(True)
        else:
            isReal.append(False)

    # update all reviews is_real status
    for i in range(len(reviews)):
        reviews[i].is_real = isReal[i]

