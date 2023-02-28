from flask import Flask, render_template, request, redirect, url_for, session
import requests
import time
import json
import plot
import main

app = Flask(__name__)
app.secret_key = "asdfjkl;"

@app.route('/')
def mainpage():
    print("asdjfkl")
    return render_template('description.html')

@app.route('/get_reviews', methods=['GET','POST'])
def get_reviews():
    if request.method == 'POST':
        return redirect('/get_reviews')
    return render_template('loading.html')

@app.route('/load_reviews', methods=['GET','POST'])
def load_reviews():
    if request.method == 'POST':
        url = request.data
        print(url)
        session['reviews'] = url
        return redirect('/load_reviews')


    # url = "https://www.amazon.com/Brisko-USA-Regulation-Professional-Performance/dp/B09FH4K5J1/ref=cm_cr_arp_d_product_top?th=1"
    # print(url)
    url = session['reviews']
    review = main.main(url)
    return render_template('reviews_flask.html', dict=review)
