import pymongo


if __name__ == "__main__":
    print("WC to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['swayam']
    collection = db['MySampleCollectionForSwayam']

    allDocs = collection.find({'Name': 'Anish'}, {'_id': 0})
    for doc in allDocs:
        print(doc)
