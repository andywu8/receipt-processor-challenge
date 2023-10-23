import requests
import json
def test():
    f = open('./examples/morning-receipt.json')
    json_data = json.load(f)
    response = requests.post('http://localhost:8000/receipts/process', json=json_data)
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    # print (response.text)



if __name__ == "__main__":
    test()
