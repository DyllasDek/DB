from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

db = client['admin']

 result = db.lab11.insert_one({"address": value, key2:
value2 ...})