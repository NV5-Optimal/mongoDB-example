from pymongo import MongoClient
from measure_object_example import Measure

from credentials import MONGO_CXN_STRING

# Connect to the MongoDB server
client = MongoClient(MONGO_CXN_STRING)


# Access the "OPTIMAL_DEV" database
db = client["OPTIMAL_DEV"]
collection = db["MEASURE"]

# Update a record in the "MEASURE" collection
filter = {"name": "ES Dehumidifier_Res"}  # Replace with the appropriate filter for your record

# change the value of life_exp to whatever value you want
update = {"$set": {"life_exp": 42}} 

collection.update_one(filter, update)

# Close the MongoDB connection
client.close()