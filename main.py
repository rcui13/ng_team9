from review import Review
from review_scraper import ReviewScraper
from review_classifier import reviewQuality

def main(url):
    scraper = ReviewScraper()
    reviews = []

    for page in scraper.pages(scraper.get_product_reviews_url(url)):
        review_html = page.find_all(class_="a-section celwidget")

        for s in review_html: 
            reviews.append(
                Review(s.find(class_="a-profile-name"), 
                       s.find("a", attrs={"data-hook":"review-title"}).find("span"),
                       s.find("span", attrs={"data-hook":"review-body"}),
                       s.find("i", attrs={"data-hook":"review-star-rating"}).find("span"),
                       s.find("a")['href'],
                       True))
        
    arr = reviewQuality(scraper.get_title(), reviews)
    print(arr)

if "__main__" == __name__:
    product_url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Pe\
        rformance/dp/B09FH4K5J1/ref=cm_cr_arp_d_product_top?ie=UTF8"
    main(product_url)
