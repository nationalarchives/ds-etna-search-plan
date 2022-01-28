from flask_wtf import FlaskForm
from wtforms.fields import SearchField
from wtforms.validators import InputRequired
class CatalogueSearch(FlaskForm):
    search_term = SearchField(
        'Search term',
        validators=[InputRequired()],
        render_kw={
            'class': 'search-component__search-term-input'
        }
    )