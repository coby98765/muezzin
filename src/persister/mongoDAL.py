from pymongo import MongoClient ,errors
import os

class MongoDAL:
    def __init__(self):
        self.client = None
        self.DB_HOST = os.getenv("MONGO_HOST","mongodb://localhost:27017/")
        self.DB_NAME = os.getenv("MONGO_NAME","muezzin")
        self.DB_COLL = os.getenv("MONGO_COLL", "podcasts")

    def load_report(self,report):
        try:
            self.client = MongoClient(self.DB_HOST)
            mydb = self.client[self.DB_NAME]
            collection = mydb[self.DB_COLL]
            res = collection.insert_one(report)
            return res.inserted_id
        except errors.ServerSelectionTimeoutError as err:
            print(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            print(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            print(f"Configuration error: {err}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise