from src.utils.logger import Logger
from manager import Manager
import os

# logger setup
logger = Logger.get_logger(index="transcriber_log",name="transcriber.main.py")

PUB_TOPIC = os.getenv("PUB_TOPIC","metadata_transcription")
SUB_TOPIC = os.getenv("SUB_TOPIC","podcast_meta")

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