from review import Review
from review_scraper import ReviewScraper
import matplotlib.pyplot as plt
# from review_classifier import reviewQuality


def main(url):
    scraper = ReviewScraper()
    reviews = []
    
    reviews_url = scraper.get_product_reviews_url(url)

    product_name = scraper.get_product_name(reviews_url)

    for page in scraper.pages(reviews_url):
        review_html = page.find_all(class_="a-section celwidget")

        for s in review_html:
            reviews.append(
                Review(s.find(class_="a-profile-name"),
                       s.find("a", attrs={
                              "data-hook": "review-title"}).find("span"),
                       s.find("span", attrs={"data-hook": "review-body"}),
                       s.find("i", attrs={
                              "data-hook": "review-star-rating"}).find("span"),
                       s.find("a")['href'],
                       s.find("span", attrs={"data-hook": "review-date"}).text,
                       True))


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
        if review.is_real:
            unreliable += 1
    
    _, ax = plt.subplots()
    ax.pie([unreliable, len(reviews)-unreliable], 
           labels=["Unreliable", "Reliable"])
    plt.show()


if "__main__" == __name__:
    product_url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Pe\
        rformance/dp/B09FH4K5J1/ref=cm_cr_arp_d_product_top?ie=UTF8"
    main(product_url)
