from kafka import KafkaProducer,KafkaConsumer
import os
import json

class Kafka:
    def __init__(self,sub_topic):
        self.bootstrap_servers = os.getenv("KAFKA_HOST","localhost:9092")
        self.group_id = os.getenv("GROUP_ID","GROUP_ID")
        self.producer = self.create_producer()
        self.consumer = self.create_consumer()
        self.sub_topic = sub_topic

    def create_producer(self):
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            print('connected to kafka PUB')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def create_consumer(self):
        try:
            self.consumer = KafkaConsumer(
                self.sub_topic,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                value_deserializer=lambda v: json.loads(v.decode("utf-8"))
            )
            print('connected to kafka SUB')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def pub(self, data, topic):
        try:
            print("sending to topic:", topic, data)
            self.producer.send(topic, value=data)
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def sub(self):
        try:
            for msg in self.consumer:
                print("received: ",msg.value,type(msg))
                yield msg.value
        except Exception as ex:
            print(ex)
            raise Exception(ex)