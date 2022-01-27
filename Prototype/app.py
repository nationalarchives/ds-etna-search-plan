from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Go to <a href='/search'>/search</a></p>"

@app.route("/search")
def catalogue_results():
    return render_template("catalogue_results.html");

