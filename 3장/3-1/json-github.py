import urllib.request as req
import os.path, random
import json

url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, "r", encoding='utf-8'))

for item in items:
    print(item["name"] + " - " + item["owner"]["login"])
