from src.utils.kafka_conn import Kafka
from speech2text import Speech2Text
from src.utils.logger import Logger
from model import Podcast
import os

# logger setup
logger = Logger.get_logger(index="transcriber_log",name="transcriber.manager.py")

class Manager:
    def __init__(self,pub_topic:str,sub_topic:str):
        self.pub_topic = pub_topic
        self.sup_topic = sub_topic
        self.kafka = None
        self.t2s = None

    def setup(self,group_id):
        try:
            self.kafka = Kafka(group_id)
            self.kafka.create_consumer(self.sup_topic)
            self.kafka.create_producer()
            self.t2s = Speech2Text()
        except Exception as e:
            logger.error(f"Manager.setup, Error: {e}")
            raise


    def listener(self):
        for r in self.kafka.sub():
            try:
                # enter report into Podcast Model
                report = Podcast(r)
                # transcribe podcast
                transcription = self.transcribe(report.file_path)
                # transcription = ""
                # add Transcription to Object
                report.add_transcript(transcription)
                # send updated report on Kafka Pub
                self.kafka.pub(report.__dict__(),self.pub_topic)
                pass
            except Exception as e:
                logger.error(f"Manager.listener, Error: {e}")
                raise

    def transcribe(self,file_path):
        chunks = self.t2s.load_and_split(file_path)
        chunks_file_list = self.t2s.export_chunks(chunks)
        full_transcription = self.t2s.transcribe_all(chunks_file_list)
        return full_transcription

# t2s = Speech2Text()
# chunky = t2s.load_and_split(r"C:\Users\Yaakov\PycharmProjects\muezzin\data\podcasts\download (2).wav")
# print("chunky:",chunky)
# chunky_file_list = t2s.export_chunks(chunky)
# print("chunky_file_list:",chunky_file_list)
# full_transcription = t2s.transcribe_all(chunky_file_list)
# print("full_transcription:",full_transcription)
