import requests
from flask import Flask, render_template, url_for
import os, json

app = Flask(__name__)
# this file is the root
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url = os.path.join(SITE_ROOT, "data", "DT_data.json")
data = json.load(open(json_url))
id_json_url = os.path.join(SITE_ROOT, "data", "id_data.json")
id_data = json.load(open(id_json_url))
#data = open(json_url)

@app.route('/')
def index():
    #form_url = os.path.join(SITE_ROOT, "templates", "form.html")
    return render_template("form.html")

@app.route("/models")
def get_data():
    global data
    return json.dumps(data)

@app.route("/models/<string:model_id>")
def get_model_page(model_id):
    print(id_data[model_id])
    # shortcut the data sections needed
    name = id_data[model_id]['0']["model_info"][0]["name"]
    resrcs = id_data[model_id]['0']["model_resources"]

    yt_api_url = "https://www.googleapis.com/youtube/v3/search"
    payload = {
        "part": name,
        "type": "video",
    }
    yt_resp = requests.get(yt_api_url, data=payload)
    return render_template("model.html", model_name=name, img1=resrcs["image_1"], img2=resrcs["image_2"], img3=resrcs["image_3"], official_link=resrcs["official_link"])

if __name__ == "__main__":
    app.run(debug=True)
