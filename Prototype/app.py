from flask import Flask, render_template, request
from forms.catalogue_search import CatalogueSearch
import os, json
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def hello_world():
    return "<p>Go to <a href='/search'>/search</a></p>"

@app.route("/search")
def catalogue_results():
    form = CatalogueSearch(request.args, meta = {'csrf': False})
    return render_template("catalogue_results.html", form=form, search_type="Catalogue results", search_term="Churchill");

