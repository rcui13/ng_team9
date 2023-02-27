from bs4 import BeautifulSoup
import requests
import re

def get_website_html(url: str) -> str:
    return requests.get(url, 
                        headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)\
                                  AppleWebKit/537.36 (KHTML, like Gecko)Chrome/\
                                  44.0.2403.157 Safari/537.36','Accept-Language\
                                    ': 'en-US, en;q=0.5'})).text

# Extracts the product code in order to navigate into review page
def extract_product_code(url: str) -> str:
    splitted_url = url.split("/")
    return splitted_url[5] if splitted_url[4] == "dp" \
        else print("URL format changed") 

def get_product_reviews_url(product_code: str) -> str:
    return f"https://www.amazon.com/product-reviews/{product_code}/ref=cm_cr_dp\
        _d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="

def pages(url: str) -> BeautifulSoup:
    i = 1
    soup = BeautifulSoup(get_website_html(url + str(i)), features="html.parser")
    while soup.find(class_="a-section review aok-relative"):
        yield soup
        i += 1
        soup = BeautifulSoup(get_website_html(url + str(i)), 
                             features="html.parser")

if "__main__" == __name__:
    product_url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Pe\
        rformance/dp/B09FH4K5J1/ref=cm_cr_arp_d_product_top?ie=UTF8"
    product_code = extract_product_code(product_url)
    
    soup = BeautifulSoup(get_website_html(product_url), features="html.parser")
    title = soup.find("span", attrs={"id":"productTitle"}).text.strip()

    reviewer_names = []
    review_rating = []
    review_text = []
    reviewer_url = []

    for page in pages(get_product_reviews_url(product_code)):
        for s in page.find_all(class_="a-section celwidget"):
            reviewer_names.append(s.find(class_="a-profile-name"))

        for s in page.find_all("span", attrs={"data-hook":"review-body"}):
            review_text.append(s.find("span"))
        
        for s in page.find_all("i", attrs={"data-hook":"review-star-rating"}):
            review_rating.append(s.find("span"))

        for s in page.find_all(class_="a-section celwidget"):
            reviewer_url.append(s.find("a")['href'])
    
    processed_rating = [float(re.search(r'[0-9].[0-9]', str(e)).group()) for e in review_rating]
    processed_review = [str(e).strip("</span>").strip("<span>").replace("<br/>", "\n") for e in review_text]
    processed_url = ["https://www.amazon.com/" + e for e in reviewer_url] 

    print(len(reviewer_names))
    print(len(processed_rating))
    print(len(processed_url))
    