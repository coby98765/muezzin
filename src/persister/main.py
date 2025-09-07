from src.utils.kafka_conn import Kafka
from mongoDAL import MongoDAL
from model import Podcast

kafka_conn = Kafka()
kafka_conn.create_consumer("podcast_meta")

mongoDAL = MongoDAL()

counter = 2
for report in kafka_conn.sub():
    try:
        _id = f"podcast{counter}_{report["created_time"][:9]}"
        # upload podcast file to mongoDB
        file_location = mongoDAL.load_file(report['file_path'],_id)
        report_model = Podcast(report,_id)
        res = mongoDAL.load_report(report_model.__dict__())
        print("Added report to mongoDB:",res)
        counter += 1
    except Exception as e:
        print(e)

