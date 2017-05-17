# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:27:50 2017

@author: mac
"""

# mongo_hello_world.py
# Author: Bruce Elgort
# Date: March 18, 2014
# Purpose: To demonstrate how to use Python to
# 1) Connect to a MongoDB document collection
# 2) Insert a document
# 3) Display all of the documents in a collection</code>
 
from pymongo import MongoClient
 
client=MongoClient()


# connect to the students database and the ctec121 collection
db = client.vigdb
from datetime import datetime
#creating collection and inserting document in Mongodb
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
) 
#fetching value from collection and printing in console
collection =db['mycol']


cursor = collection.find({})
for document in cursor: 
    print(document)

 
# close the connection to MongoDB
client.close()