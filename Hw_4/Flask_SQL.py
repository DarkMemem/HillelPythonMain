from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from flask import jsonify
from db import execute_query
from html_formatters import format_records
import requests
import sqlite3
import os


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


@app.route("/unique_names")
def get_unique_names():
    query = 'SELECT DISTINCT(FirstName) FROM customers'
    records = execute_query(query)
    return format_records(records)


@app.route("/tracks_count")
def get_tracks_count():
    query = 'SELECT COUNT(*) FROM Tracks'
    records = execute_query(query)
    return format_records(records)


@app.route("/customers")
@use_kwargs({
    "city": fields.Str(
        required=False
    ),
    "country": fields.Str(
        required=False
    )},
    location="query"
)
def get_customers(city=None, country=None):
    if city:
        query = f"SELECT City,Country FROM customers WHERE City='{city}'"
        records = execute_query(query)
        return format_records(records)

    if country:
        query = f"SELECT City,Country FROM customers WHERE Country='{country}'"
        records = execute_query(query)
        return format_records(records)

    query = "SELECT City,Country FROM customers"
    records = execute_query(query)
    return format_records(records)


@app.route("/sales")
def get_sales():
    query = 'SELECT SUM(UnitPrice * Quantity) FROM invoice_items'
    records = execute_query(query)
    return format_records(records)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
