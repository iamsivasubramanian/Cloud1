from pymongo import MongoClient

uri = "mongodb+srv://siva:1234@cluster0.zapzteh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["myDB"]           
collection = db["users"]      

user1 = {"name": "Siva", "age": 25, "role": "Developer"}
insert_result1 = collection.insert_one(user1)
print("Inserted ID:", insert_result1.inserted_id)

users = [
    {"name": "Subu", "age": 30, "role": "Designer"},
    {"name": "Kumar", "age": 28, "role": "Manager"},
    {"name": "Mani", "age": 22, "role": "Intern"}
]

insert_result2 = collection.insert_many(users)
print("Inserted IDs:", insert_result2.inserted_ids)

found_user = collection.find_one({"name": "Siva"})
print("Found User:", found_user)


update_result = collection.update_one(
    {"name": "Siva"},
    {"$set": {"age": 26}}
)
print("Modified Count:", update_result.modified_count)

delete_result = collection.delete_one({"name": "Kumar"})
print("Deleted Count:", delete_result.deleted_count)

client.close()
