from flask import Flask, render_template, request, redirect
import time
import json
import plot
import main

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('description.html')

@app.route('/get_reviews')
def get_reviews():
    return render_template('loading.html')

@app.route('/load_reviews', methods=['POST'])
def load_reviews():
    # if request.method == 'POST':
    url = request.form["url"]
    print(type(url))
    print(url)
    # link = json.loads(url)
    # print(link)
    review = main.main(url)
    print(review)

    return render_template('reviews_flask.html', dict=review)