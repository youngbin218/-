import yaml

yaml_str = """
Date : 2021-03-02
PriceList :
    -
        item_id : 1000
        name : Banana
        color : yellow
        price : 800
    -
        item_id : 1001
        name : Orange
        color : orange
        price : 1400
    -
        item_id : 1002
        name : Apple
        color : red
        price : 2400
"""

data = yaml.load(yaml_str)

for item in data['PriceList']:
    print(item["name"], item["price"])
