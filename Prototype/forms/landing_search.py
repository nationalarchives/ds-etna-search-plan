from flask_wtf import FlaskForm
from wtforms.fields import SearchField
from wtforms.validators import InputRequired


class LandingSearch(FlaskForm):

    search_term = SearchField(
        'Search term',
        validators=[InputRequired()],
        render_kw={
            'class': 'search-results-hero__form-search-box',
            'role': 'search',
            'placeholder': 'e.g. Churchill or medal cards'
        }
    )