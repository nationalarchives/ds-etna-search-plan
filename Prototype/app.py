from flask import Flask, render_template, request
from forms.catalogue_search import CatalogueSearch
from forms.featured_results import FeaturedResults
import os, json
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    return """<p>
    <a href='/search/catalogue'>Catalogue search</a>
    <a href='/search/featured'>Featured results</a>
    </p>"""

@app.route("/search")
def search():
    return """<p>
    <a href='/search/catalogue'>Catalogue search</a>
    <a href='/search/featured'>Featured results</a>
    </p>"""   

@app.route("/search/catalogue")
def catalogue_results():
    form = CatalogueSearch(request.args, meta = {'csrf': False})
    return render_template("catalogue_results.html", form=form, search_type="Catalogue results", search_term="Churchill", selected_tab={'catalogue': True});

@app.route("/search/featured")
def featured_results():
    form = FeaturedResults(request.args, meta = {'csrf': False})
    return render_template("featured_results.html", form=form, search_type="Catalogue results", search_term="Churchill", selected_tab={'featured': True});

