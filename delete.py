import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['swayam']

    collection = db['MySampleCollectionForSwayam']

    rec = {'name': 'Swayam'}
    collection.delete_one(rec)
