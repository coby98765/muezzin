from src.utils.kafka_conn import Kafka
from src.utils.logger import Logger
from processor import Processor
from cleaner import Cleaner
from model import Podcast

# logger setup
logger = Logger.get_logger(index="enricher_log",name="enricher.manager.py")

class Manager:
    def __init__(self,pub_topic:str,sub_topic:str):
        self.pub_topic = pub_topic
        self.sup_topic = sub_topic
        self.kafka = None
        self.processor = None

    def setup(self):
        try:
            self.kafka = Kafka()
            self.kafka.create_consumer(self.sup_topic)
            self.kafka.create_producer()
            self.processor = Processor()
        except Exception as e:
            logger.error(f"Manager.setup, Error: {e}")
            raise


    def listener(self):
        for r in self.kafka.sub():
            try:
                # enter report into Podcast Model
                report = Podcast(r)
                # clean transcribe
                clean_text,text_word_count = Cleaner.run(report.transcript)
                # process transcription
                process_stats = self.processor.run(clean_text,text_word_count)
                # add Transcription to Object
                report.add_bds_stat(process_stats)
                # send updated report on Kafka Pub
                self.kafka.pub(report.__dict__(),self.pub_topic)
            except Exception as e:
                logger.error(f"Manager.listener, Error: {e}")
                raise
