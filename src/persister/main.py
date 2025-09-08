from src.utils.logger import Logger
from manager import Manager

# logger setup
logger = Logger.get_logger(index="persister_log",name="persister.main.py")


manager = Manager()

if __name__ == "__main__":
    try:
        print()
        logger.info('main, Services Setup start...')
        manager.setup()
        logger.info('main, Services Setup Complete...')
        logger.info('main, Listening to Kafka ...')
        manager.listener()
    except Exception as e:
        logger.error(f"main, Error: {e}")