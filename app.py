from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('description.html')

@app.route('/get_reviews')
def get_reviews():
    return render_template('loading.html')

@app.route('/load_reviews')
def load_reviews():
    return render_template('reviews.html')