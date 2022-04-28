from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017")

db = client['admin'].lab11

result = db.insert_one({
    "address.building": "1480",
    "address.street": "2 Avenue",
    "address.zipcode": "10075",
    "address.coord": [-73.9557413, 40.7720266],
    "borough": "Manhattan",
    "cuisine": "Italian",
    "grades": [
        {"date": datetime.datetime.strptime("01 Oct, 2014", "%d %b, %Y")},
        {"grade": "A"},
        {"score": 11}],
    "name": "Vella",
    "restaurant_id": "41704620"
})
