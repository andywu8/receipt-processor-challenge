import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return ('Home Page')

@app.route("/receipts/process", methods=['POST'])
def process_receipt():
    data = request.json
    print("data", data)
    return_data = {
        "id": 5483
    }
    return jsonify(return_data)


@app.route("/receipts/<id>/points", methods=['GET'])
def get_points(id):
    return "ID is " + str(id)




if __name__ == "__main__":
    app.run(host='localhost', port=8000)


