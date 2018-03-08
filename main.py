from flask import Flask, jsonify, request
from numpy import sqrt, square
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def getName():
    data = {
        "name": "Michelle"
    }
    return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def getHello(name):
    data = {
        "message": "Hello there, {0}".format(name)
    }
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def postDistance():
    r = request.get_json()
    d = sqrt(square((r["a"][0]-r["b"][0]))+square((r["a"][1]-r["b"][1])))
    res = {
        "distance": d
    }

    return jsonify(res)


if __name__ == "__main__":
    app.run(host="127.0.0.1")