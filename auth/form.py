from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
                     
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf.file import FileField,FileAllowed


def validate_password(form, password):
    symbols = ["#","!","@","$","%","&","*","_",".",",",":","ç"]
    error = True
    for i in symbols:
        if i in password.data:
            error = False
            break
    if error == True:
        raise ValidationError('Please, use one of special symbols on your password: "#","!","@","$","%","&","*","_",".",",",":","ç" ')


class Sign_up_form(FlaskForm):
    firstname = StringField("First Name", [InputRequired(), Length(min=3,max=20)])
    lastname = StringField("Last Name", [InputRequired(), Length(min=3,max=20)  ])
    email = StringField("Email", [InputRequired()])
    password = StringField("Password", [InputRequired(), Length(min=8,max=30), validate_password])
    enabled = BooleanField("I accept the Terms of Use & Privacy Policy", [InputRequired()])
    photo = FileField(validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

class Log_in_form(FlaskForm):
    email = StringField("Email", [InputRequired()])
    password = StringField("Password", [InputRequired(), Length(min=8,max=30), validate_password])
    enabled = BooleanField("I accept the Terms of Use & Privacy Policy", [InputRequired()])
