from src.utils.kafka_conn import Kafka
from src.utils.logger import Logger
from model import Podcast
from pathlib import Path
import os

DIR_PATH = os.getenv("DIR_PATH",r"C:\Users\Yaakov\PycharmProjects\muezzin\data\podcasts1")
EXPORT_TOPIC = os.getenv("EXPORT_TOPIC","podcast_meta")
GROUP_ID = os.getenv("GROUP_ID", "retriever")


# logger setup
logger = Logger.get_logger(index="retriever_log",name="retriever.main.py")

kafka_conn = Kafka(GROUP_ID)

def run(kafka):
    pathlist = Path(DIR_PATH).glob('**/*.wav')
    for path in pathlist:
        file_metadata = path.stat()
        meta = Podcast(str(path),file_metadata)
        try:
            kafka.pub(meta.__dict__(),"podcast_meta")
            logger.info(f"Podcast {meta.name} metadata report sent.")
        except Exception as e:
            logger.error(f"Podcast {meta.name} Failed: {e}")
            raise

if __name__ == "__main__":
    try:
        kafka_conn.create_producer()
        logger.info("Kafka Connection Success.")
        run(kafka_conn)
    except Exception as e:
        logger.error(("Kafka Connection Failed:",e))
        raise
    finally:
        # close Kafka Connection
        kafka_conn.producer.flush()
        kafka_conn.producer.close()
        logger.info("metadata reports completed.")
