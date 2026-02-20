from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
from wtforms.fields import DateField
from wtforms import SelectField
from wtforms import TextAreaField



# add job app form
class JobForm(FlaskForm):
    company = StringField("Company", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    date_applied = DateField("Date Applied", format="%Y-%m-%d")
    status = SelectField(
    "Status",
    choices=[
        ("Applied", "Applied"),
        ("Interviewing", "Interviewing"),
        ("Offer", "Offer"),
        ("Rejected", "Rejected")
    ],validators=[DataRequired()])
    notes = TextAreaField("Notes")

    submit = SubmitField("Add Job")