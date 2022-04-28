from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")


db = client['admin'].lab11

result = db.delete_one({"borough": "Manhattan"})
print(result)
print("\n")
result = db.delete_many({"cuisine": "Thai"})
print(result)
print("\n")