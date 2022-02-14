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
        }
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

    collection_WO = BooleanField('WO - War Office, Armed Forces, Judge Advocate General, and related bodies', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_BT = BooleanField('BT - Board of Trade and successors', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_ADM = BooleanField('ADM - Admiralty, Navy, Royal Marines, and Coastguard', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_HO = BooleanField('HO - Home Office', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_C = BooleanField('C - Chancery, the Wardrobe, Royal Household, Exchequer and various commissions', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_PROB = BooleanField('PROB - Prerogative Court of Canterbury', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_AIR = BooleanField('AIR - Air Ministry and Royal Air Force records', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_FO = BooleanField('FO - Foreign Office', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_E = BooleanField('E - Exchequer, Office of First Fruits and Tenths, and the Court of Augmentations', render_kw = {
        'class': 'search-filters__checkbox'
    })
    collection_IR = BooleanField('IR - Boards of Stamps, Taxes, Excise, Stamps and Taxes, and Inland Revenue', render_kw = {
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
        'aria-describedby': 'search_filters__opening-date-help-text'
    },
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
        collections = [
            'collection_WO',
            'collection_BT',
            'collection_ADM',
            'collection_HO',
            'collection_C',
            'collection_PROB',
            'collection_AIR',
            'collection_FO',
            'collection_E',
            'collection_IR',
        ]
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