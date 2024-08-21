from pymongo import MongoClient
from credentials import MONGO_CXN_STRING

# Connect to the MongoDB server
client = MongoClient(MONGO_CXN_STRING)

# Access the "OPTIMAL_DEV" database
db = client["OPTIMAL_DEV"]
collection = db["MEASURE"]

# Delete a record in the "MEASURE" collection
filter = {"name": "ES Dehumidifier_Res"}  # Replace with the appropriate filter for your record

collection.delete_one(filter)

# Close the MongoDB connection
client.close()