from flask import Flask, render_template, request
from forms.catalogue_search import CatalogueSearch
from forms.featured_results import FeaturedResults
from forms.landing_search import LandingSearch
from forms.long_filters import LongFilters

import os, json
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    return """<p>
    <a href='/search'>Go to /search</a>
    </p>"""

@app.route("/search")
def search():
    form = LandingSearch(request.args, meta = {'csrf': False})
    return render_template("search_landing.html", form=form,
    collection_buckets = [
        ('Collection #1', '(n)', False),
        ('Collection #2', '(n)', False),
        ('Collection #3', '(n)', False),
    ],
    catalogue_buckets = [
        ('All records from The National Archives', '(12m)', False),
        ('Online records from The National Archives', '(9m)', False),
        ('All records from other UK archives', '(10m)', False),
        ('Record creators', '(270k)', False),
        ('Directory of archives in the UK and beyond', '(3k)', False)
    ],
    website_buckets = [
        ('Highlights', '(n)', False),
        ('Insights', '(n)', False),
        ('Blogs', '(1740)', False),
        ('Videos and podcasts', '(1050)', False),
        ('Research guides', '(360)', False)
    ]
    );

@app.route("/search/catalogue")
def catalogue_results():
    form = CatalogueSearch(request.args, meta = {'csrf': False})
    return render_template("catalogue_results.html", form=form, search_type="Catalogue results", search_term="Churchill", selected_tab={'catalogue': True},
    buckets = [
        ('All records from The National Archives', '(42,403)', True),
        ('Online records from The National Archives', '(5,151)', False),
        ('All records from other UK archives', '(42,403)', False),
        ('Record creators', '(83)', False),
        ('Directory of archives in the UK and beyond', '(12)', False)
    ]);

@app.route("/search/featured")
def featured_results():
    form = FeaturedResults(request.args, meta = {'csrf': False})
    return render_template("featured_results.html", form=form, search_type="Catalogue results", search_term="Churchill", selected_tab={'featured': True});

@app.route("/search/long-filters")
def long_filters():
    form = LongFilters(request.args, meta = {'csrf': False})
    return render_template("long_filters.html", form=form)