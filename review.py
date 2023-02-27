import re

class Review:

    def __init__(self, reviewer_name, review_rating, review_text, reviewer_url) -> None:
        self.reviewer_name = reviewer_name
        self.review_rating = review_rating
        self.review_text = review_text
        self.reviewer_url = reviewer_url

    def processed_review_name(self):
        return self.reviewer_name.text

    def processed_review_rating(self):
        return float(re.search(r'[0-9].[0-9]', str(self.review_rating)).group())

    def processed_review_text(self):
        return str(self.review_text).strip("</span>").strip("<span>").replace("<br/>", "\n")

    def processed_url(self):
        "https://www.amazon.com/" + self.reviewer_url
