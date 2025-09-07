from src.utils.kafka_conn import Kafka
from mongoDAL import MongoDAL

kafka_conn = Kafka()
kafka_conn.create_consumer("podcast_meta")

mongoDAL = MongoDAL()


for msg in kafka_conn.sub():
    res = mongoDAL.load_report(msg)
    print("Added to mongoDB:",res)