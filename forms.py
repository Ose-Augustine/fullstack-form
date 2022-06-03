from flask_wtf import FlaskForm as Form 
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import DataRequired,InputRequired

class BasicForm(Form):
    first_name = StringField('firstname',validators=[DataRequired("This field should not be empty")])
    last_name = StringField('lastname',validators=[DataRequired()])
    password = PasswordField('password',validators=[InputRequired()])
    email = EmailField('email')