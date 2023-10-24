import requests
import json

def test_1():
    f = open('./examples/morning-receipt.json')
    json_data = json.load(f)
    response = requests.post('http://localhost:8000/receipts/process', json=json_data)
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())

def test_2():
    f = open('./examples/simple-receipt.json')
    json_data = json.load(f)
    response = requests.post('http://localhost:8000/receipts/process', json=json_data)
    # print("Status code: ", response.status_code)
    # print("Printing Entire Post Request")
    return response.json()
    print(response.json())



if __name__ == "__main__":
    print("morning receipt: ", test_1())
    print("simple receipt: ", test_2())

