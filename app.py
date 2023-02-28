from flask import Flask, render_template, request, redirect
import time
import json
import plot
import main

app = Flask(__name__)

@app.route('/')
def mainpage():
    print("asdjfkl")
    return render_template('description.html')

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    print("get reviews")
    return render_template('loading.html')

@app.route('/load_reviews', methods=['POST'])
def load_reviews():
    url = request.form["url"]
    print(url)

    review = main.main(url)

    # return render_template('reviews_flask.html', dict=review)
    # return render_template('description.html')
    return redirect('/')