from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import generate_password
from flask import jsonify
import requests

app = Flask(__name__)


@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/random")
@use_kwargs({
    "length": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=100)]
    ),
    "specials": fields.Bool(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    ),
    "digits": fields.Bool(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    )},
    location="query"
)
def get_random(length, specials, digits):
    return generate_password(length, specials, digits)


@app.route("/bitcoin_rate")
@use_kwargs({
    "currency": fields.Str(
        required=False,
        missing="USD"
    )},
    location="query"
)
def get_bitcoin_rate(currency):
    r = requests.get('https://bitpay.com/api/rates')
    lst = r.json()
    dct = {}
    for i in lst:
        dct.setdefault(i['code'], i['rate'])
    rate = dct.get(currency)
    return f"Курс BTC к {currency} = " + str(rate)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
