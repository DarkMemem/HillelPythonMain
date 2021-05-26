from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import generate_password, generate_password_specials, generate_password_digits, generate_password_specials_digits
from flask import jsonify
import requests
import string
import random

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
    if digits == 1 & specials == 1:
        return generate_password_specials_digits(length)
    elif specials == 1:
        return generate_password_specials(length)
    elif digits == 1:
        return generate_password_digits(length)
    else:
        return generate_password(length)


# @app.route("/bitcoin_rate")
# @use_kwargs({
#     "currency": fields.Str(
#         required=False,
#         missing="BTC",
#         validate=[validate.ABC]
#     )},
# )
# def get_bitcoin_rate(currency):
#     url = 'https://bitpay.com/api/rates/BTC'
#     query = {"BTC": currency}
#     rate = requests.get(url, params=query)
#     return str(rate)


app.run(debug=True, port=5001)
