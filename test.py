import requests
def test():
    response = requests.post('http://localhost:8000/receipts/process', json='./examples/morning-receipt.json')
    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())
    # print (response.text)



if __name__ == "__main__":
    test()
