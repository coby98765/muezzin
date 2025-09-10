from src.utils.kafka_conn import Kafka
from src.utils.logger import Logger
from manager import Manager
import os

EXPORT_TOPIC = os.getenv("EXPORT_TOPIC","podcast_meta")

# logger setup
logger = Logger.get_logger(index="enricher_log",name="enricher.main.py")

kafka_conn = Kafka()

PUB_TOPIC = os.getenv("EXPORT_TOPIC","metadata_bds")
SUB_TOPIC = os.getenv("IMPORT_TOPIC","metadata_transcription")

manager = Manager(PUB_TOPIC,SUB_TOPIC)


if __name__ == "__main__":
    try:
        logger.info('main, Services Setup start...')
        manager.setup()
        logger.info('main, Services Setup Complete...')
        logger.info('main, Listening to Kafka ...')
        manager.listener()
    except Exception as e:
        logger.error(f"main, Error: {e}")