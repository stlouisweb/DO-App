#!flask/bin/python
from flask import Flask, jsonify
from index import list_droplets
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/droplets', methods=['GET'])
def get_droplets():
    droplets = list_droplets()
    return jsonify(droplets)

if __name__ == '__main__':
    app.run(debug=True)
