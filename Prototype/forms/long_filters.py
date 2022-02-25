from flask_wtf import FlaskForm
from wtforms.fields import SearchField, BooleanField


class LongFiltersTopic(FlaskForm):

    search_within = SearchField(
        'Search within filters',
        render_kw={
            'class': 'long-filters__form-search-box',
            'role': 'search',
        }
    )

    filter_1 = BooleanField('Intelligence (214)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_2 = BooleanField('Operations, battles and campaigns (179)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_3 = BooleanField('Conflict (173)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_4 = BooleanField('Europe and Russia (167)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_5 = BooleanField('International (115)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_6 = BooleanField('Americas (88)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_7 = BooleanField('Navy (69)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_8 = BooleanField('Radio and television (69)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_9 = BooleanField('Communications (66)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_10 = BooleanField('Personal and family papers (64)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    class Meta:
        filters = ['filter_1','filter_2','filter_3','filter_4','filter_5','filter_6','filter_7','filter_8','filter_9','filter_10']


class LongFiltersCollection(FlaskForm):

    search_within = SearchField(
        'Search within filters',
        render_kw={
            'class': 'long-filters__form-search-box',
            'role': 'search',
        }
    )

    filter_1 = BooleanField('HO - Home Office (326)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_2 = BooleanField('KV - Security Service (195)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_3 = BooleanField('SP - State Paper Office, including papers of the Secretaries of State up to 1782 (46)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_4 = BooleanField('HW - Government Communications Headquarters (GCHQ) (44)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_5 = BooleanField('FO - Foreign Office (28)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_6 = BooleanField('CO - Colonial Office, Commonwealth and Foreign and Commonwealth Offices (18)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_7 = BooleanField('GFM - Copies of captured records of the German, Italian and Japanese Governments. (14)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_8 = BooleanField('WO - War Office, Armed Forces, Judge Advocate General, and related bodies (13)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_9 = BooleanField('PRO - Domestic Records of the Public Record Office, Gifts, Deposits, Notes and Transcripts (11)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    filter_10 = BooleanField('ADM - Admiralty, Navy, Royal Marines, and Coastguard (8)', render_kw = {
        'class': 'long-filters__form-filters-checkbox'
    })

    class Meta:
        filters = ['filter_1','filter_2','filter_3','filter_4','filter_5','filter_6','filter_7','filter_8','filter_9','filter_10']