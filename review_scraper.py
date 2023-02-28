from bs4 import BeautifulSoup
import requests
import re
import time

class ReviewScraper:


    def get_website_html(self, url: str) -> str:
        return requests.get(url, 
                            headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)\
                                      AppleWebKit/537.36 (KHTML, like Gecko)Chrome/\
                                      44.0.2403.157 Safari/537.36','Accept-Language\
                                      ': 'en-US, en;q=0.5'})).text

    def get_product_reviews_url(self, url: str) -> str:
        return f"https://www.amazon.com/product-reviews/{self.extract_product_code(url)}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="

    def pages(self) -> BeautifulSoup:
        i = 1
        soup = BeautifulSoup(self.get_website_html(self.reviews_url + str(i)), features="html.parser")
        while soup.find(class_="a-section review aok-relative"):
            yield soup
            i += 1
            soup = BeautifulSoup(self.get_website_html(self.reviews_url + str(i)), features="html.parser")
    
    # Extracts the product code in order to navigate into review page
    def extract_product_code(self, url: str) -> str:
        splitted_url = url.split("/")
        return splitted_url[5] if splitted_url[4] == "dp" else print("URL format changed") 

    def get_product_name(self):
        return re.search(r'^What do you want to know about (.*)\?$', self.big_soup.find("textarea", attrs={"name":"askQuestionText"})['placeholder']).group(1)
    def __init__(self, url):
        self.reviews_url = self.get_product_reviews_url(url)
        self.big_soup = BeautifulSoup(self.get_website_html(self.reviews_url), features="lxml")
        while re.search(r'An error occurred while processing your request.', self.big_soup.text) != None:
            print("Retrying...")
            self.big_soup = BeautifulSoup(self.get_website_html(self.reviews_url), features="lxml")
            time.sleep(3)
            
