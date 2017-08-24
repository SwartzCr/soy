from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def mystery():
    return render_template('mystery.html')




