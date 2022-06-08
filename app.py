from setuptools import setup
from models import setup_db, Person 
from forms import BasicForm
from flask import Flask, render_template, request, redirect, url_for,flash

app = Flask(__name__)
app.config['SECRET_KEY']='bahd'
setup_db(app)

@app.route('/forms')
def render_forms():
    form = BasicForm() 
    return render_template('forms.html',form=form)

@app.route('/submissions',methods=['POST'])
def create_form_submission():
    form = BasicForm(request.form)
    person = Person(
        first_name=form.first_name.data,
        last_name = form.last_name.data,
        password  = form.password.data ,
        email     = form.email.data
    )
    if form.validate_on_submit():
        try:
            person.insert()
        except:
            person.reverse()
    return render_template('forms.html',form=form)

if __name__=='__main__':
    app.run(debug=True)