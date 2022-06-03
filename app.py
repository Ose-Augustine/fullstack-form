from setuptools import setup
from models import setup_db, Form 
from flask import Flask, render_template 

app = Flask(__name__) 
setup_db(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)