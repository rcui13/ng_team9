from bs4 import BeautifulSoup
import requests
import re
import time
import math

class ReviewScraper:

    def __init__(self, url):
        self.reviews_url = self.get_product_reviews_url(url)
        self.big_soup = self.get_soup(self.reviews_url) 
        
    def get_soup(self, url):
        soup = BeautifulSoup(self.get_website_html(url), features="html.parser")
        while re.search(r'An error occurred while processing your request.', soup.text) != None or re.search(r'Sorry, we just need to make sure', soup.text) != None:
            print("Retrying...")
            soup = BeautifulSoup(self.get_website_html(url), features="html.parser")
            time.sleep(3)            
        return soup
    
    def get_website_html(self, url: str) -> str:
        return requests.get(url, 
                            headers=({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)\
                                      AppleWebKit/537.36 (KHTML, like Gecko)Chrome/\
                                      44.0.2403.157 Safari/537.36','Accept-Language\
                                      ': 'en-US, en;q=0.5'})).text

    def get_product_reviews_url(self, url: str) -> str:
        return f"https://www.amazon.com/product-reviews/{self.extract_product_code(url)}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="

    def pages(self):
        i = 1
        while i <= self.page_count:
            yield self.reviews_url + str(i)
            i += 1
    
    # Extracts the product code in order to navigate into review page
    def extract_product_code(self, url: str) -> str:
        splitted_url = url.split("/")
        return splitted_url[5] if splitted_url[4] == "dp" else print("URL format changed") 

    def get_product_name(self):
        review_num_text = self.big_soup.find("div", attrs={"data-hook":"cr-filter-info-review-rating-count"}).text
        num = eval(re.search(r'([0-9]+) with reviews', review_num_text).group(1))
        self.page_count = int(math.ceil(num/10.0))
        return re.search(r'^What do you want to know about (.*)\?$', self.big_soup.find("textarea", attrs={"name":"askQuestionText"})['placeholder']).group(1)
