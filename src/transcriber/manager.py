from src.utils.logger import Logger
from src.utils.kafka_conn import Kafka
from model import Podcast

# logger setup
logger = Logger.get_logger(index="transcriber_log",name="transcriber.manager.py")

class Manager:
    kafka = None

    def setup(self):
        try:
            self.kafka = Kafka()
            self.kafka.create_consumer("podcast_meta")
            self.kafka.create_producer()
            logger.info(f'Manager.setup, Setup Complete.')
        except Exception as e:
            logger.error(f"Manager.setup, Error: {e}")
            raise


    def listener(self):
        for report in self.kafka.sub():
            try:
                # enter report into Podcast Model
                # transcribe podcast
                # add Transcription to Object
                # send updated report on Kafka Pub
                pass
            except Exception as e:
                logger.error(f"Manager.listener, Error: {e}")
                raise