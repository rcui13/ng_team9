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

@app.route('/load_reviews/<string:url>', methods=['POST'])
def load_reviews():
    link = json.loads(url)

    review = main.main(link)
    # time.sleep(3)
    # f = open('testreview.json')
    # review = json.load(f)
    # print(review)
    # print(review['0']['reviewer_name'])
    # print(len(review))
    # plot.make_pie_chart(review)
    return render_template('reviews_flask.html', dict=review)