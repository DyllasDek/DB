from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

db = client['admin']

print("Ex1_1:\n")
cursor_ex1_1 = db.lab11.find({"cuisine": "Indian"}, )
for obj in cursor_ex1_1:
    print("Name: " + obj["name"] + ", cuisine " + obj["cuisine"])

print("\nEx1_2:\n")
cursor_ex1_2 = db.lab11.find({"cuisine": {"$in": ["Indian", "Thai"]}})
for obj in cursor_ex1_2:
    print("Name: " + obj["name"] + ", cuisine " + obj["cuisine"])

print("\nEx1_3:\n")
cursor_ex1_3 = db.lab11.find(
    {"$and": [{"address.building": "1115"}, {"address.street": "Rogers Avenue"}, {"address.zipcode": "11226"}]})
for obj in cursor_ex1_3:
    print("Name: " + obj["name"] + ", cuisine " + obj["cuisine"])
# 1115 Rogers Avenue, 11226
