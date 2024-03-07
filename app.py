# imports
import os
from flask import Flask, render_template, redirect, url_for


# paths
project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')


# app
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
application = app


# index page
@app.route('/')
def index():
    return render_template("index.html")


# redirect to index page
@app.route('/a', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
