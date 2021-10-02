import pymongo


if __name__ == "__main__":
    print("WC to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['swayam']
    collection = db['MySampleCollectionForSwayam']

    collection.insert_many([
        {
            "School": "Ssvm",
            "Troop": "Ncc",
            "Sex": "Male"
        },
        {
            "School": "Dav",
            "Troop": "Scout",
            "Sex": "Female"
        },
        {
            "School": "Conv",
            "Troop": "Police",
            "Sex": "Male/Female"
        },
        {
            "School": "MeCampus",
            "Troop": "Ncc",
            "Sex": "Male"
        }
    ])
