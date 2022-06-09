from flask_wtf import FlaskForm as Form
from traitlets import validate 
from wtforms import StringField,PasswordField,EmailField,IntegerField
from wtforms.validators import DataRequired,InputRequired, Email , EqualTo

class BasicForm(Form):
    phone_number = IntegerField('phone_number',validators=[DataRequired()])
    first_name = StringField('firstname',validators=[DataRequired("This field should not be empty")])
    last_name = StringField('lastname',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm = PasswordField('confirm_password',validators=[EqualTo("password",message="passwords must be the same")])
    email = EmailField('email',validators=[Email(message="This is email is not of the right format ")])