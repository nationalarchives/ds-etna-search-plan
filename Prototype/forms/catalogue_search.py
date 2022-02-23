from flask_wtf import FlaskForm
from wtforms.fields import SearchField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class CatalogueSearch(FlaskForm):

    search_term = SearchField(
        'Search term',
        validators=[InputRequired()],
        render_kw={
            'class': 'search-results-hero__form-search-box',
            'role': 'search',
        },
        default='secret agents'
    )

    online_only = BooleanField('Show online records only', 
    render_kw = {
        'class': 'search-filters__checkbox'
    })

    search_within = SearchField(
        'Search within results',
        render_kw={
            'class': 'search-filters__search',
            'role': 'search',
            'default': None
        }
    )

    sort_by = SelectField(u'Sort by:', choices=[('relevance','Relevance'),('date','Date'),('title','Title')],default='relevance',
    render_kw = {
        'class': 'search-sort-view__form-select'
    })
    date_unknown = BooleanField('Dates unknown', render_kw = {
        'class': 'search-filters__checkbox'
    })
    date_1950plus = BooleanField('1950+', render_kw = {
        'class': 'search-filters__checkbox'
    })
    date_1925to1949 = BooleanField('1925 - 1949', render_kw = {
        'class': 'search-filters__checkbox'
    })
    
    date_1900to1924 = BooleanField('1900 - 1924', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1800to1899 = BooleanField('1800 - 1899', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1700to1799 = BooleanField('1700 - 1799', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1600to1699 = BooleanField('1600 - 1699', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1500to1599 = BooleanField('1500 - 1599', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1400to1499 = BooleanField('1400 - 1499', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1300to1399 = BooleanField('1300 - 1399', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1200to1299 = BooleanField('1200 - 1299', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1100to1199 = BooleanField('1100 - 1199', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1000to1099 = BooleanField('1000 - 1099', render_kw = {
        'class': 'search-filters__checkbox'
    })

    date_1to999 = BooleanField('1 - 999', render_kw = {
        'class': 'search-filters__checkbox'
    })

    level_item = BooleanField('Item', render_kw = {
        'class': 'search-filters__checkbox'
    })
    level_piece = BooleanField('Piece', render_kw = {
        'class': 'search-filters__checkbox'
    })
    level_not_stated = BooleanField('Not stated', render_kw = {
        'class': 'search-filters__checkbox'
    })
    level_series = BooleanField('Series', render_kw = {
        'class': 'search-filters__checkbox'
    })
    level_division = BooleanField('Division', render_kw = {
        'class': 'search-filters__checkbox'
    })
    level_department = BooleanField('Department', render_kw = {
        'class': 'search-filters__checkbox'
    })

    closure_open = BooleanField('Open Document', render_kw = {
        'class': 'search-filters__checkbox'
    })
    closure_closed = BooleanField('Closed Document', render_kw = {
        'class': 'search-filters__checkbox'
    })
    closure_retained = BooleanField('Retained Document', render_kw = {
        'class': 'search-filters__checkbox'
    })

    opening_date_from_yy = IntegerField('Opening date (from year)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'YYYY',
        'aria-labelledby': 'record_opening_date opening_date_from',
        'aria-describedby': 'search_filters__opening-date-help-text',
        
    },
    default=None,
    validators=[NumberRange(min=974, max=2022)])

    opening_date_from_mm = IntegerField('Opening date (from month)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'MM',
        'aria-labelledby': 'record_opening_date opening_date_from',
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
    validators=[NumberRange(min=1, max=12)])

    opening_date_from_dd = IntegerField('Opening date (from day)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'DD',
        'aria-labelledby': 'record_opening_date opening_date_from',
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
    validators=[NumberRange(min=1, max=31)])

    opening_date_to_yy = IntegerField('Opening date (to year)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'YYYY',
        'aria-labelledby': 'record_opening_date opening_date_to',
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
    validators=[NumberRange(min=974, max=2022)])

    opening_date_to_mm = IntegerField('Opening date (to month)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'MM',
        'aria-labelledby': 'record_opening_date opening_date_to',
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
    validators=[NumberRange(min=1, max=12)])

    opening_date_to_dd = IntegerField('Opening date (to day)', render_kw = {
        'class': 'search-filters__opening-date',
        'placeholder': 'DD',
        'aria-labelledby': 'record_opening_date opening_date_to',
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
    validators=[NumberRange(min=1, max=31)])

    other_archive_1 = BooleanField('London Metropolitan Archives: City of London (123)', render_kw = {
        'class': 'search-filters__checkbox'
    })

    other_archive_2 = BooleanField('Lancashire Archives (53)', render_kw = {
        'class': 'search-filters__checkbox'
    })

    other_archive_3 = BooleanField('British Library: Asian and African Studies (56)', render_kw = {
        'class': 'search-filters__checkbox'
    })

    class Meta:
        dates = [
            'date_unknown',
            'date_1950plus',
            'date_1925to1949', 
            'date_1900to1924',
            'date_1800to1899',
            'date_1700to1799',
            'date_1600to1699',
            'date_1500to1599',
            'date_1400to1499',
            'date_1300to1399',
            'date_1200to1299',
            'date_1100to1199',
            'date_1000to1099',
            'date_1to999']
        levels = [
            'level_item',
            'level_piece',
            'level_not_stated',
            'level_series',
            'level_division',
            'level_department'
        ]
        closures = [
            'closure_open',
            'closure_closed',
            'closure_retained',
        ]
        held_by = [
            'other_archive_1',
            'other_archive_2',
            'other_archive_3'
        ]