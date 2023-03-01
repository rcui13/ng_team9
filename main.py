from review import Review
from review_scraper import ReviewScraper
from review_classifier import processQuality

import re
import json
import threading

def main(url):
    scraper = ReviewScraper(url)
    reviews = []
    threads = []

    product_name = scraper.get_product_name()
    print(product_name)
    product_name = product_name.replace('&#34;', '&quot;')
    for url in scraper.pages():
        thread = threading.Thread(target=_add, args=(scraper, url, reviews))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
 
    for r in reviews:
        r.text = r.text.replace("The media could not be loaded.", "").strip()
        r.text = r.text.replace('"', "&quot;")
        r.text = r.text.replace('&#34;', "&quot;")
        r.review_title = r.review_title.replace('"', "&quot;")
        r.review_title = r.review_title.replace('&#34;', "&quot;")
        r.review_title = r.review_title.replace("The media could not be loaded.", "").strip()
    try:
        processQuality(product_name, reviews, 10)
    except TypeError:
        return "An error occurred."

    print("finished")
    return output_json(product_name, reviews)

def _add(scraper, url, reviews):
    page = scraper.get_soup(url)
    review_html = page.find_all(class_="a-section celwidget")
    for s in review_html:
        name = s.find(class_="a-profile-name")
        body = s.find("span", attrs={"data-hook": "review-body"})
        title = s.find(["a", "span"], attrs={"data-hook": "review-title"}).find("span")
        rating = s.find("i", attrs={"data-hook": re.compile(r'(cmps)?review-star-rating')}).find("span")
        link = s.find("a")['href']
        date = s.find("span", attrs={"data-hook": "review-date"}).text,

        reviews.append(Review(name, title, body, rating, link, date, True))

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
    return json.dumps([product_name, review_output])


if "__main__" == __name__:
    product_url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Performance/dp/B09FH4K5J1/ref=sr_1_1_sspa?crid=O0KB7A6DOVP8&keywords=soccer+ball&qid=1677566588&sprefix=soccer+ball%2Caps%2C76&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyM1FNTUlQUlZLMzhLJmVuY3J5cHRlZElkPUEwMDAxNTcwM09DT083TEVYU1Q3OSZlbmNyeXB0ZWRBZElkPUEwNTU3MTgyMTczVFA5N0tSVjdRUiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    main(product_url)
