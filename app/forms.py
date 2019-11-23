from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    input = StringField('Enter in coin id:', validators=[DataRequired()])
    search = SubmitField('Search')