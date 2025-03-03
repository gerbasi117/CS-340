from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        USER = "aacuser"
        PASS = "password"
        HOST = "nv-desktop-services.apporto.com"
        PORT = 34042
        DB = "aac"
        COL = "animals"

        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/aac?authSource=admin")
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """ Inserts a document into the collection """
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        if query is not None: 
            results = self.database.animals.find(query)
            return list(results) # Converts cursor to list for output
        else:
            raise Exception("Nothing to save, because data parameters empty")

    def update(self, query, new_values):
        """ Updates documents in collection """
        if query and new_values:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count # Returns number of modified documents
        else:
            raise Exception("Query and new values must be provided")
            
    def delete(self, query):
        """ Deletes documents in the collection """
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count # Return number of deleted documents
        else:
            raise Exception("Query must be provided")