from flask import Flask, request, render_template, url_for
import os, json

# this file is the root
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url = os.path.join(SITE_ROOT, "data", "full_data.json")
data = json.load(open(json_url))

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def show_index():
        form_url = os.path.join(SITE_ROOT, "templates", "form.html")
        return render_template(form_url)

    @app.route("/data")
    def get_data():
        global data
        return json.dumps(data)

    return app
