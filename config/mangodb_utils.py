from pymongo import MongoClient

client = MongoClient('mongodb://your_mongo_connection_string')
db = client['restaurant']

def save_to_mongodb(collection_name, filter_query, data):
    collection = db[collection_name]
    collection.update_one(filter_query, {'$set': data}, upsert=True)

def delete_from_mongodb(collection_name, filter_query):
    collection = db[collection_name]
    collection.delete_one(filter_query)