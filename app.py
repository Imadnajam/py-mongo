from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["Etablissement"]
collection = db["Stagiaire"]


# query = {"id": 2}
# results = collection.find(query)
# for  result in results:
#     print("Result:", result)

with open("data.json") as f:
    data = json.load(f)

collection.insert_many(data)









# data = {"name": "John", "age": 30, "city": "New York"}
# result = collection.insert_one(data)
# print("Inserted ID:", result.inserted_id)

# Querying data
# query = {"name": "John"}
# result = collection.find_one(query)
# print("Result:", result)

# Close connection
# client.close()
