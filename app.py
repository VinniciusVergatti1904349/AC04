import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)
@app.route('/')
def fibo():
    px = 1
    ant = 0
    lim = 50
    found = 0
    res = "0,"
    while (found < lim):
        tmp = px
        px += ant
        ant = tmp
        found += 1
        res += str(px)+ ","

    return res

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
