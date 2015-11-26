#!flask/bin/python
import json
from bson import ObjectId
from flask import Flask, jsonify, json, request, abort
from flask.ext.cors import CORS
from index import list_droplets
from flask_oauthlib.provider import OAuth2Provider
from flask.ext.pymongo import PyMongo
import random
import string

app = Flask(__name__)
oauth = OAuth2Provider(app)
CORS(app)
app.config["MONGO_DBNAME"] = 'do_app'
mongo = PyMongo(app)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/users/create", methods=["POST"])
def create_user():
    if not request.json:
        abort(400)
    user = {
        'id': "".join(random.sample(string.lowercase+string.digits, 16)),
        'username': request.json['username'],
        'email': request.json['email'],
        'password': request.json['password']
    }
    users = mongo.db.users
    users.insert(user)
    user = JSONEncoder().encode(users.find_one())
    #return "user added"
    return user

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
