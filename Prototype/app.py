from flask import Flask, render_template, request
from forms.catalogue_search import CatalogueSearch
from forms.featured_results import FeaturedResults
from forms.landing_search import LandingSearch
from forms.long_filters import LongFiltersTopic, LongFiltersCollection

import os, json
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/")
def search():
    form = LandingSearch(request.args, meta = {'csrf': False})
    return render_template("search_landing.html", form=form,
    collection_buckets = [
        ('Collection #1', '(n)', False),
        ('Collection #2', '(n)', False),
        ('Collection #3', '(n)', False),
    ],
    catalogue_buckets = [
        ('Records from The National Archives', '(12m)', False),
        ('Online records from The National Archives', '(9m)', False),
        ('Records from other UK archives', '(10m)', False),
        ('Record creators', '(270k)', False),
        ('Find an archive', '(3k)', False)
    ],
    website_buckets = [
        ('Highlights', '(n)', False),
        ('Insights', '(n)', False),
        ('Blogs', '(1740)', False),
        ('Videos and podcasts', '(1050)', False),
        ('Research guides', '(360)', False)
    ]
    );

@app.route("/search/catalogue/")
def catalogue_results():
    form = CatalogueSearch(request.args, meta = {'csrf': False})
    return render_template("catalogue_results.html", form=form, search_type="Catalogue results", search_term="secret agents", selected_tab={'catalogue': True},
    buckets = [
        ('Records from The National Archives', '(751)', True),
        ('Online records from The National Archives', '(179)', False),
        ('Records from other UK archives', '(836)', False),
        ('Record creators', '(1)', False),
        ('Find an archive', '(0)', False)
    ],
    cards = [
        {
            'title': 'Visa arrangements for secret agents',
            'ref': 'HO 213/2056 ',
            'date': '1943 - 1945',
            'held_by': 'The National Archives, Kew',
            'description': 'Visa arrangements for secret agents',
            'downloadable': False,
            'image': 'https://via.placeholder.com/150x150'
        },
        {
            'title': 'Medal card of Moussabini, P Corps: Secret Service Intelligence Department ...',
            'ref': 'WO 372/14/127377 ',
            'date': '1914 - 1920',
            'held_by': 'The National Archives, Kew',
            'description': 'Medal card of Moussabini, P',
            'downloadable': True,
            'image': '/static/images/records/1.png'
        },
        {
            'title': 'Folio 37: Recommends secret agent.',
            'ref': 'PRO 30/22/20/9',
            'date': '1859 July 17',
            'held_by': 'The National Archives, Kew',
            'description': 'Folio 37: Recommends secret agent.',
            'downloadable': False,
            'image': 'https://via.placeholder.com/150x150'
        },
        {
            'title': 'James MacGIBBON / Jean Margaret MacGIBBON: British. Information from a secret source...',
            'ref': 'KV 2/1670',
            'date': '1950 Jan 01 - 1950 Dec 31 ',
            'held_by': 'The National Archives, Kew',
            'description': """James MacGIBBON / Jean Margaret MacGIBBON: British. Information from a secret source indicated that MACGIBBON had performed 'a service' for the Soviets during the Second World War, for which he was rewarded. He was investigated and eventually interviewed,but denied the allegation. He was never brought to trial""",
            'downloadable': True,
            'image': '/static/images/records/2.png'
        },
        {
            'title': 'Etzdorf Papers: Secret Agent reports',
            'ref': 'GFM 33/128/114',
            'date': ' 1939 - 1940',
            'held_by': 'The National Archives, Kew',
            'description': "Etzdorf Papers: Secret Agent reports ",
            'downloadable': False,
            'image': '/static/images/records/2.png'
        },
        {
            'title': 'Johannes ROERIG: German. As London correspondent of a Cologne newspaper, ROERIG...',
            'ref': 'KV 2/3704',
            'date': '1926 Aug 26 - 1947 Dec 10',
            'held_by': 'The National Archives, Kew',
            'description': """Johannes ROERIG: German. As London correspondent of a Cologne newspaper, ROERIG published a secret British report on the steel industry in 1930 which led to the suspicion that he was working for German Intelligence. He returned to Germany in 1939""",
            'downloadable': True,
            'image': '/static/images/records/3.png'
        },
    ]);

@app.route("/search/featured/")
def featured_results():
    form = FeaturedResults(request.args, meta = {'csrf': False})
    return render_template("featured_results.html", 
    form=form, 
    search_type="Catalogue results", 
    search_term="secret agents", 
    selected_tab={'featured': True},
    cards=[
        {
            'title': 'Visa arrangements for secret agents',
            'ref': 'HO 213/2056 ',
            'date': '1943 - 1945',
            'held_by': 'The National Archives, Kew',
            'description': 'Visa arrangements for secret agents',
            'downloadable': False,
            'image': 'https://via.placeholder.com/150x150'
        },
        {
            'title': 'Medal card of Moussabini, P Corps: Secret Service Intelligence Department ...',
            'ref': 'WO 372/14/127377 ',
            'date': '1914 - 1920',
            'held_by': 'The National Archives, Kew',
            'description': 'Medal card of Moussabini, P',
            'downloadable': True,
            'image': '/static/images/records/1.png'
        },
        {
            'title': 'Folio 37: Recommends secret agent.',
            'ref': 'PRO 30/22/20/9',
            'date': '1859 July 17',
            'held_by': 'The National Archives, Kew',
            'description': 'Folio 37: Recommends secret agent.',
            'downloadable': False,
            'image': 'https://via.placeholder.com/150x150'
        },
    ]);

@app.route("/search/long-filters/")
def long_filters():

    formType = request.args.get('type')

    if formType == 'topics':
        form = LongFiltersTopic(request.args, meta = {'csrf': False})
    else:
        form = LongFiltersCollection(request.args, meta = {'csrf': False})
    return render_template("long_filters.html", form=form)