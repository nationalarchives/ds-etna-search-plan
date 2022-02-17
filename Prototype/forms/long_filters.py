from flask_wtf import FlaskForm
from wtforms.fields import SearchField, BooleanField


class LongFilters(FlaskForm):

    search_within = SearchField(
        'Search within filters',
        render_kw={
            'class': 'long-filters__form-search-box',
            'role': 'search',
        }
    )

    filter_1 = BooleanField('Filter example', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    class Meta:
        filters = ['filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', 'filter_1', ]

