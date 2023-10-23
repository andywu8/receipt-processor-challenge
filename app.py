import json
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

def main():
    print("Hello World!")


@app.route("/receipts/<id>/points")
def get_points(id):
    return "ID is " + str(id)


def process_receipt():
    f = open('data.json')
    data = json.load(f)


if __name__ == "__main__":
    main()
