from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField
from wtforms.validators import DataRequired

class NewAssessmentForm(FlaskForm):
    moduleCode = StringField("Module Code", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    dateTime = DateTimeField("Date and Time", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])

