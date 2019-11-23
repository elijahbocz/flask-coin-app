from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    input = StringField('Enter In Coin Name:', validators=[DataRequired()])
    search = SubmitField('Search')