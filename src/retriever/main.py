from model import Podcast
from src.utils.kafka_conn import Kafka
from pathlib import Path
import os

DIR_PATH = os.getenv("DIR_PATH",r"C:\Users\Yaakov\PycharmProjects\muezzin\data\podcasts")
EXPORT_TOPIC = os.getenv("EXPORT_TOPIC","podcast_meta")

kafka_conn = Kafka()
kafka_conn.create_producer()

pathlist = Path(DIR_PATH).glob('**/*.wav')
for path in pathlist:
    path_in_str = str(path)
    file_metadata = path.stat()
    meta = Podcast(str(path),file_metadata)
    kafka_conn.pub(meta.__dict__(),"podcast_meta")
