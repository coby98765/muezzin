from src.utils.logger import Logger
from manager import Manager
import os

# logger setup
logger = Logger.get_logger(index="persister_log",name="persister.main.py")

SUB_TOPIC = os.getenv("IMPORT_TOPIC","podcast_enriched")
GROUP_ID = os.getenv("GROUP_ID", "persister")


manager = Manager(SUB_TOPIC)

if __name__ == "__main__":
    try:
        logger.info('main, Services Setup start...')
        manager.setup(GROUP_ID)
        logger.info('main, Services Setup Complete...')
        logger.info('main, Listening to Kafka ...')
        manager.listener()
    except Exception as e:
        logger.error(f"main, Error: {e}")