from src.utils.kafka_conn import Kafka
from mongoDAL import MongoDAL
from model import Podcast

kafka_conn = Kafka()
kafka_conn.create_consumer("podcast_meta")

mongoDAL = MongoDAL()


for report in kafka_conn.sub():
    # upload podcast file to mongoDB
    file_location = mongoDAL.load_file(report['file_path'],report["file_name"])
    print("Added file to mongoDB:",file_location)
    report_model = Podcast(report,file_location)
    res = mongoDAL.load_report(report_model.__dict__())
    print("Added report to mongoDB:",res)
