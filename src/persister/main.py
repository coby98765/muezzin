from src.utils.kafka_conn import Kafka

kafka_conn = Kafka()
kafka_conn.create_consumer("podcast_meta")


for msg in kafka_conn.sub():
    print("received: ",str(msg))