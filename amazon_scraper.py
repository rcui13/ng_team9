from bs4 import BeautifulSoup
import requests
import re

def get_website_html(url: str) -> str:
    return requests.get(url, headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})).text

# Extracts the product code in order to navigate into review page
def extract_product_code(url: str) -> str:
    splitted_url = url.split("/")
    return splitted_url[5] if splitted_url[4] == "dp" else print("URL format changed") 

def get_product_review_url(product_code: str) -> str:
    return f"https://www.amazon.com/product-reviews/{product_code}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="

def pages(url: str) -> BeautifulSoup:
    i = 1
    while (soup := BeautifulSoup(get_website_html(get_product_review_url(url) + str(i))))\
        .find(class_="a-section review aok-relative"):
        yield soup
        i += 1

if "__main__" == __name__:
    product_url = "https://www.amazon.com/Aoneky-Kids-Soccer-Ball-Size/dp/B01HJ8OOYI/ref=sr_1_6?crid=3RWGUU3M6C8WH&keywords=soccer%2Bball&qid=1677461949&sprefix=soccer%2Bball%2Caps%2C91&sr=8-6&th="
    product_code = extract_product_code(product_url)
    review_url = get_product_review_url(product_code)

    soup = BeautifulSoup(get_website_html(review_url), features="html.parser")
    reviewer_names = [s for s in soup.find_all(class_="a-profile-name")]
    review_text = [s.find("span") for s in soup.find_all("span", attrs={"data-hook":"review-body"})]
    review_rating = [s.find("span") for s in soup.find_all("i", attrs={"data-hook":"review-star-rating"})]
    processed_rating = [float(re.search(r'[0-9].[0-9]', str(e)).group()) for e in review_rating]
    processed_reviews = [str(e).strip("</span>").strip("<span>").replace("<br/>", "\n") for e in review_text]

    print(processed_rating)
