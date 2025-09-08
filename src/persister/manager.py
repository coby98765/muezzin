from src.utils.kafka_conn import Kafka
from mongoDAL import MongoDAL
from elasticDAL import ElasticDAL
from model import Podcast

class Manager:
    mongoDAL = None
    elasticDAL = None
    kafka = None

    def setup(self):
        try:
            self.mongoDAL = MongoDAL()
            self.elasticDAL = ElasticDAL()
            self.elasticDAL.map_index(Podcast.map())
            self.kafka = Kafka()
            self.kafka.create_consumer("podcast_meta")
        except Exception as e:
            print("Error:",e)
            raise
    def listener(self):
        counter = 1
        for report in self.kafka.sub():
            try:
                _id = f"podcast{counter}_{report["created_time"][:9]}"
                report_model = Podcast(report, _id)
                # upload podcast file to mongoDB
                self.mongoDAL.load_file(report_model.prev_path, _id)
                #send metadata to Elastic & Backup to MongoDB
                self.elasticDAL.insert_data(report_model.__dict__())
                res = self.mongoDAL.load_report(report_model.__dict__())
                print("Task completed for:",_id)
                counter += 1
            except Exception as e:
                print(e)