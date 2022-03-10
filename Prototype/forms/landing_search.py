from flask_wtf import FlaskForm
from wtforms.fields import SearchField
from wtforms.validators import InputRequired


class LandingSearch(FlaskForm):

    search_term = SearchField(
        'This label isnt used, one is coded in the HTML instead',
        validators=[InputRequired()],
        render_kw={
            'class': 'search-results-hero__form-search-box',
            'placeholder': ''
        }
    )