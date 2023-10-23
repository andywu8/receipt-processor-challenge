import json
from flask import Flask, jsonify, request
import uuid
app = Flask(__name__)


@app.route("/")
def home():
    return ('Home Page')

@app.route("/receipts/process", methods=['POST'])
def process_receipt():
    data = request.json
    # Call generate id function 
    hash_id = generate_id(data)
    return_data = {
        "id": hash_id
    }
    with open('./data/'+str(hash_id)+'.json', 'w') as f:
        json.dump(data, f)
    return jsonify(return_data)

def generate_id(data):
    # Convert JSON to a string
    str_data = json.dumps(data)
    # Use UUID to generate a hash id from the json data
    hash_id = uuid.uuid5(uuid.NAMESPACE_URL, str_data)
    return hash_id






@app.route("/receipts/<id>/points", methods=['GET'])
def get_points(id):
    return "ID is " + str(id)




if __name__ == "__main__":
    app.run(host='localhost', port=8000)


