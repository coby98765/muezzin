from src.utils.kafka_conn import Kafka
from src.utils.logger import Logger
from manager import Manager
import os

EXPORT_TOPIC = os.getenv("EXPORT_TOPIC","podcast_meta")

# logger setup
logger = Logger.get_logger(index="enricher_log",name="enricher.main.py")



PUB_TOPIC = os.getenv("EXPORT_TOPIC","podcast_enriched")
SUB_TOPIC = os.getenv("IMPORT_TOPIC","podcast_transcription")
GROUP_ID = os.getenv("GROUP_ID", "enricher")

manager = Manager(PUB_TOPIC,SUB_TOPIC)


if __name__ == "__main__":
    try:
        logger.info('main, Services Setup start...')
        manager.setup(GROUP_ID)
        logger.info('main, Services Setup Complete...')
        logger.info('main, Listening to Kafka ...')
        manager.listener()
    except Exception as e:
        logger.error(f"main, Error: {e}")