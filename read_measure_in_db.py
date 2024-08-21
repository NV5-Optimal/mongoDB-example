from pymongo import MongoClient

from measure_object_example import Measure

from credentials import MONGO_CXN_STRING

# Connect to the MongoDB server
client = MongoClient(MONGO_CXN_STRING)

# Access the "OPTIMAL_DEV" database
db = client["OPTIMAL_DEV"]

# Access the "measures" collection
collection = db["MEASURE"]

# Query for all documents with "Dehumidifier" in the "name" field
query = {"name": {"$regex": "Dehumidifier"}}

# Execute the query and retrieve the matching documents
results = collection.find(query)

# Print the matching documents
for result in results:
    read_measure = Measure.from_dict(result)
    print(result)