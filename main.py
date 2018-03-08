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
    d = calcDistance(r["a"], r["b"])
    res = {
        "distance": d
    }
    return jsonify(res)


def calcDistance(a, b):
    distance = sqrt(square(a[0] - b[0]) + square(a[1] - b[1]))
    return distance


if __name__ == "__main__":
    app.run(host="127.0.0.1")