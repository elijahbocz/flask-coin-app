from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    user_input = StringField('Enter in a coin name to get detailed information:',
                             validators=[DataRequired()])
    search = SubmitField('Search')
