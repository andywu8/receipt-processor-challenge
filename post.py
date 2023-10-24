import requests
import json

def post(json_file):
    f = open(json_file)
    print("json file: ", json_file)
    json_data = json.load(f)
    response = requests.post('http://localhost:8000/receipts/process', json=json_data)
    return response.json()

if __name__ == "__main__":
    morning_receipt = './examples/morning-receipt.json'
    simple_receipt = './examples/simple-receipt.json'
    print("morning receipt id: ", post(morning_receipt))
    print("simple receipt id: ", post(simple_receipt))

