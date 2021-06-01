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


@app.route("/genres_durations")
def get_genres_durations_group():
    query = "select sum(t.Milliseconds/1000), g.name FROM (tracks t INNER JOIN genres g on t.GenreId==g.GenreId) " \
            "GROUP BY g.name; "
    records = execute_query(query)
    return format_records(records)


@app.route("/greatest_hits")
@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=1888,
        validate=[validate.Range(min=1, max=1888)]
    )},
    location="query"
)
def get_greatest_hits(count):
    query = "SELECT t.Name,count(ii.TrackId)*ii.UnitPrice AS Price,count(ii.TrackId) AS Sale FROM invoice_items as ii "\
            f"JOIN tracks as t on ii.TrackId = t.TrackId GROUP BY t.Name ORDER BY Price DESC LIMIT {count};"
    records = execute_query(query)
    return format_records(records)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
