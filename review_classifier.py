import openai
import re
from review import Review
import threading

# Takes an array of review_texts and returns an array of either Real or Fake
def _reviewQuality(product_name, reviews: list[Review]):

    # This is the key from openai
    with open("key.txt", "r") as f:
        openai.api_key = str(f.read())
    
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

    # Converts reviewTypeArray to boolean values and updates review
    for i in range(len(reviewTypeArray)):
        if reviewTypeArray[i] == 'Real':
            reviews[i].is_real = True
        else:
            reviews[i].is_real = False

def processQuality(product_name, reviews: list[Review], batch_size: int):
    threads = []
    for i in range(0, len(reviews), batch_size):
        sublist = reviews[i:i+batch_size]
        thread = threading.Thread(target=_reviewQuality, args=(product_name, sublist))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
