from flask_wtf import FlaskForm
from wtforms import StringField
                     
from wtforms.validators import InputRequired
from flask_wtf.file import FileField,FileAllowed
from wtforms.widgets import TextArea

class Update(FlaskForm):
    photo = FileField( [InputRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

class CommentForm(FlaskForm):
    message = StringField("Comment", [InputRequired()],widget=TextArea())