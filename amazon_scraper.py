from bs4 import BeautifulSoup
import requests


def get_website_html(url: str) -> str:
    return requests.get(url).text

# Extracts the product code in order to navigate into review page
def extract_product_code(url: str) -> str:
    splitted_url = url.split("/")
    return splitted_url[5] if splitted_url[4] == "dp" else print("URL format changed") 

def get_product_review_url(product_code: str) -> str:
    return f"https://www.amazon.com/product-reviews/{product_code}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"


if "__main__" == __name__:
    product_url = "https://www.amazon.com/Wilson-Duke-Official-Leather-Football/dp/B09JMBZKB9/ref=sr_1_1_sspa?crid=2UUVVDLI0SF91&keywords=football&qid=1677463592&sprefix=football%2Caps%2C92&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNjdQWVY4SDEzWjVVJmVuY3J5cHRlZElkPUEwNjA1MDY1MVRUVks0NUtZTVc4NSZlbmNyeXB0ZWRBZElkPUEwMjYzMDkxMUVJOTQ0U09TR09HWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    product_code = extract_product_code(product_url)
    review_url = get_product_review_url(product_code)

    # Currently requests are failing to get the correect url

    soup = BeautifulSoup(get_website_html(review_url), features="html.parser")
    reviews = soup.find_all(class_="a-section review aok-relative")

    print(reviews)

    soup = BeautifulSoup(get_website_html("https://www.amazon.com/ref=nav_logo"), features="html.parser")
    print(soup.prettify())
