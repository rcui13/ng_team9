from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def runapp():  # put application's code here
    return render_template('mainpage.html')

