from flask import Flask, render_template
import time
import json

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('description.html')

@app.route('/get_reviews')
def get_reviews():
    return render_template('loading.html')

@app.route('/load_reviews')
def load_reviews():
    time.sleep(3)
    valid_link = 'reviews.html'
    # f = open("testreview.json")
    # review = json.load(f)
    # print(len(review))
    # print(review['0'])
    return render_template(valid_link)