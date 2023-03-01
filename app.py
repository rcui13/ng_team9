from flask import Flask, render_template, request, redirect, session
from waitress import serve
import main

app = Flask(__name__)
app.secret_key = "asdfjkl;"

if __name__ == "__main__":
    serve(app, host="localhost", port=8080)

@app.route('/')
def mainpage():
    return render_template('description.html')

@app.route('/get_reviews', methods=['GET','POST'])
def get_reviews():
    if request.method == 'POST':
        return redirect('/get_reviews')
    return render_template('loading.html')

@app.route('/load_reviews', methods=['GET','POST'])
def load_reviews():
    if request.method == 'POST':
        url = request.form['data']
        session['reviews'] = url
        return "success"
    url = session['reviews']
    try:
        review = main.main(url)
        if review == "An error occurred.":
            return render_template('errorpage.html')
        return render_template('reviews_flask.html', dict=review)
    except Exception:
        print("asdf")
        return render_template('invalidpage.html')
