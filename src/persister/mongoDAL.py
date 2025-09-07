from pymongo import MongoClient ,errors
from gridfs import GridFS

import os

class MongoDAL:
    def __init__(self):
        self.DB_HOST = os.getenv("MONGO_HOST","mongodb://localhost:27017/")
        self.DB_NAME = os.getenv("MONGO_NAME","muezzin")
        self.DB_COLL = os.getenv("MONGO_REPORT_COLL", "podcasts_meta")
        self.DB_COLL = os.getenv("MONGO_FILE_COLL", "podcasts_metadata")

    def load_report(self,report):
        try:
            client = MongoClient(self.DB_HOST)
            mydb = client[self.DB_NAME]
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
        finally:
            client.close()

    def load_file(self,file_path,file_name):
        try:
            client = MongoClient(self.DB_HOST)
            fs = GridFS(client[self.DB_NAME])
            # open WAV file
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # store in GridFS
            file_id = fs.put(file_data, _id=file_name, content_type='audio/wav')
            print(f"WAV file '{file_path}' uploaded successfully with GridFS ID: {file_id}")
            return file_id
        except FileNotFoundError:
            print(f"Error: WAV file not found at '{file_path}'")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            client.close()
