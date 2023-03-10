import re

class Review:

    def __init__(self, reviewer_name, review_title, text, rating, url, date, is_real):
        self.reviewer_name = reviewer_name.text
        self.review_title = review_title.text
        self.rating = float(re.findall(r'[0-9].[0-9]', str(rating))[0])
        self.text =  text.text.replace("<br>", "\n")
        self.reviewer_url = "https://www.amazon.com/" + url 
        self.date = date
        self.is_real = is_real
