from review import Review
from review_scraper import ReviewScraper
import matplotlib.pyplot as plt
from review_classifier import process10
import re

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
    
    process10(product_name, reviews)
    create_graph(reviews)

    for r in reviews:
        if not r.is_real:
            print(r.text)

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
    return {product_name: review_output}

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
    product_url = "https://www.amazon.com/WAHU-Phlat-Ball-Classic-Green/dp/B09NWCVCGB" 
    main(product_url)
