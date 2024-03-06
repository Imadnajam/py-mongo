from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Etablissement"]
collection = db["Stagiaire"]


# Querying data
query = {"id": 2}
result = collection.find_one(query)
print("Result:", result)

























# Inserting data
# data = {"name": "John", "age": 30, "city": "New York"}
# result = collection.insert_one(data)
# print("Inserted ID:", result.inserted_id)

# Querying data
# query = {"name": "John"}
# result = collection.find_one(query)
# print("Result:", result)

# Close connection
# client.close()