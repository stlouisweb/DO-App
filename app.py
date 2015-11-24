#!flask/bin/python
from flask import Flask, jsonify, json
from flask.ext.cors import CORS
from index import list_droplets
app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/droplets", methods=["GET"])
def get_droplets():
    do_droplets = list_droplets()
    #return jsonify({'droplets': do_droplets})
    droplets = []
    for i, droplet in enumerate(do_droplets):
        data = {}
        data["id"] = do_droplets[i]["id"]
        data["name"] = do_droplets[i]["name"]
        data["image"] = do_droplets[i]["image"]["slug"]
        data["memory"] = do_droplets[i]["memory"]
        data["disk"] = do_droplets[i]["size"]["disk"]
        data["ip_address"] = do_droplets[i]["networks"]["v4"][0]["ip_address"]
        data["region"] = do_droplets[i]["region"]["name"]
        droplets.append(data)

    return jsonify({'droplets': droplets})

if __name__ == "__main__":
    app.run(debug=True)
