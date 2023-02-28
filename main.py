from review import Review
from review_scraper import ReviewScraper
import matplotlib.pyplot as plt
from review_classifier import processQuality
import re
import json

def main(url):
    scraper = ReviewScraper(url)
    reviews = []
    
    product_name = scraper.get_product_name()

    for page in scraper.pages():
        review_html = page.find_all(class_="a-section celwidget")

        for s in review_html:
            reviews.append(
                Review(s.find(class_="a-profile-name"),
                       s.find(["a", "span"], attrs={"data-hook": "review-title"}).find("span"),
                       s.find("span", attrs={"data-hook": "review-body"}), 
                       s.find("i", attrs={
                              "data-hook": re.compile(r'(cmps)?review-star-rating')}).find("span"),
                       s.find("a")['href'],
                       s.find("span", attrs={"data-hook": "review-date"}).text,
                       True))
    
    for r in reviews:
        r.text = r.text.replace("The media could not be loaded.", "").strip()
    processQuality(product_name, reviews, 10)
    # create_graph(reviews)
    return output_json(product_name, reviews)

 #   for r in reviews:
 #       print(r.text)

def output_json(product_name, reviews) -> dict:
    review_output = {}
    for i, review in enumerate(reviews):
        review_output[i] = {"reviewer_name": review.reviewer_name,
                            "review_title": review.review_title,
                            "rating": review.rating,
                            "text": review.text,
                            "reviewer_url": review.reviewer_url,
                            "date": review.date,
                            "is_real": review.is_real}
    # return json.dumps([product_name, review_output])
    return [product_name, review_output]
def create_graph(reviews):
    unreliable = 0
    for review in reviews:
        if not review.is_real:
            unreliable += 1
    
    _, ax = plt.subplots()
    ax.pie([unreliable, len(reviews)-unreliable], 
           labels=["Unreliable", "Reliable"])
    plt.show()

if "__main__" == __name__:
    product_url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Performance/dp/B09FH4K5J1/ref=sr_1_1_sspa?crid=O0KB7A6DOVP8&keywords=soccer+ball&qid=1677566588&sprefix=soccer+ball%2Caps%2C76&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyM1FNTUlQUlZLMzhLJmVuY3J5cHRlZElkPUEwMDAxNTcwM09DT083TEVYU1Q3OSZlbmNyeXB0ZWRBZElkPUEwNTU3MTgyMTczVFA5N0tSVjdRUiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    main(product_url)
