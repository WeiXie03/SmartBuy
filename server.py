from flask import Flask, request, render_template, url_for
import os, json

app = Flask(__name__)
# this file is the root
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url = os.path.join(SITE_ROOT, "data", "full_data.json")
data = json.load(open(json_url))

@app.route('/')
def show_index():
    #form_url = os.path.join(SITE_ROOT, "templates", "form.html")
    return render_template("form.html")

@app.route("/data")
def get_data():
    global data
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
