from setuptools import setup
from models import setup_db, Form 
from forms import BasicForm
from flask import Flask, render_template, request, redirect, url_for,flash

app = Flask(__name__) 
setup_db(app)

@app.route('/')
def index():
    form = BasicForm()
    return render_template('index.html',form=form)

@app.route('/submissions',methods=['POST'])
def form_submission():
    form = BasicForm(request.form)
    if form.validate_on_submit():
        person = Form(
            first_name=form.first_name.data,
            last_name = form.last_name.data,
            password  = form.password.data, 
            email = form.email.data 
        )
        person.insert()
        flash("Submission was a success")
    else:
        return "<h1>An error occured<h1> "
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)