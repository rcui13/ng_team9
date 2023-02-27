import re

PRODUCT_NAME = 

class Review:

    def __init__(self, name, review_title, text, rating, url, is_real) -> None:
        self.name = name.text
        self.review_title = review_title.text
        self.rating = float(re.findall(r'[0-9].[0-9]', str(rating))[0])
        self.text =  text.text.replace("<br/>", "\n")
        self.url = "https://www.amazon.com/" + url 
        self.is_real = is_real
