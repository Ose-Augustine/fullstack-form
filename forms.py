from flask_wtf import FlaskForm as Form
import re 
from traitlets import validate 
from wtforms import StringField,PasswordField,EmailField,TelField
from wtforms.validators import DataRequired,InputRequired, Email , EqualTo, ValidationError

class BasicForm(Form):
    phone_number = TelField('phone_number',validators=[DataRequired()])
    first_name = StringField('firstname',validators=[DataRequired("This field should not be empty")])
    last_name = StringField('lastname',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm = PasswordField('confirm_password',validators=[EqualTo("password",message="passwords must be the same")])
    email = EmailField('email',validators=[Email(message="This is email is not of the right format ")])

    def validate_phone_number(self,phone_number):
        number= phone_number.data
        pattern = re.compile(r'\d{3}?-\d{3}-\d{3}')
        matches = pattern.finditer(number)
        if number != pattern:
            self.phone_number.errors += (ValidationError("Wrong Phone number format"),)
        