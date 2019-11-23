from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    user_input = StringField('Enter in a coin name to get detailed information:',
                             validators=[DataRequired()])
    search = SubmitField('Search')


class HistorySearchForm(FlaskForm):
    date_input = StringField(
        'Enter in date to check the price at that point in time:', validators=[DataRequired()])
    search = SubmitField('Search')
