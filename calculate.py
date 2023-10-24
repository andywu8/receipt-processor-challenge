import json

'''
Calculates points from a JSON object using given rules:
One point for every alphanumeric character in the retailer name.
50 points if the total is a round dollar amount with no cents.
25 points if the total is a multiple of 0.25.
5 points for every two items on the receipt.
If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
6 points if the day in the purchase date is odd.
10 points if the time of purchase is after 2:00pm and before 4:00pm.
'''
def calculate_points(data):
    points = 0 
    retailer = data["retailer"]
    purchase_date = data["purchaseDate"]
    purchase_time = data["purchaseTime"]
    total = data["total"]
    items = data["items"]

    # One point for every alphanumeric character in the retailer name.
    for char in retailer:
        if char.isalnum():
            points += 1

    # Get cents from total
    print("total substr", total[len(total)-2: len(total)])
    str_cents = total[len(total)-2: len(total)]

    # 50 points if the total is a round dollar amount with no cents.
    if str_cents == "00":
        print("ends in 00")
        points += 50
        
    # 25 points if the total is a multiple of 0.25.
    if int(str_cents) % 25 == 0:
        print("multiple of 25")
        points += 25

    # 5 points for every two items on the receipt.
    points += 5 * len(items)//2

    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in items:
        if len(item["shortDescription"].strip()) % 3 == 0:
            print("trim check")
            points += int(float(item["price"]) * 0.2) 

    # 6 points if the day in the purchase date is odd.
    if int(purchase_date[8:10]) % 2 != 0:
        print("day check")
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    hour = int(purchase_time[0:2])
    minutes = int(purchase_time[3:5])
    if hour >= 14 and hour < 16:
        if minutes > 0:
            print("time check")
            points += 10
    return points



if __name__ == "__main__":
    f = open('./examples/morning-receipt.json')
    json_data = json.load(f)
    print("json_data", json_data)
    calculate_points(json_data)