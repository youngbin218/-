import json
price = {
    "date" : "2021-03-01",
    "price" : {
        "Apple" : 80,
        "Orange" : 55,
        "Banana" : 40
    }
}
s = json.dumps(price)
print(s)
