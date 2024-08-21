from pymongo import MongoClient
from measure_object_example import Measure

from credentials import MONGO_CXN_STRING

# Connect to the MongoDB Atlas cluster
client = MongoClient(MONGO_CXN_STRING)

# Access the database and collection
db = client["OPTIMAL_DEV"]
collection = db["MEASURE"]

# Create a Measure object
measure = Measure(name="ES Dehumidifier_Res",
                  end_use="Appliances",
                  sector="R",
                  description="Energy Star Dehumidifier Residential",
                  life_exp=10,
                  primary_fuel="Electricity")

# Create another Measure object
measure_2 = Measure(name="ES Refrigerator_Res",
                    end_use="Appliances",
                    sector="R",
                    description="Energy Star Refrigerator Residential",
                    life_exp=15,
                    primary_fuel="Electricity")


# Insert the Measure object into the collection
result = collection.insert_one(measure.to_dict())
result_2 = collection.insert_one(measure_2.to_dict())

# Print the inserted document's ID
print("Inserted document ID:", result.inserted_id)

# Close the MongoDB connection
client.close()