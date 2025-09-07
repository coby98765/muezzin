from pathlib import Path
import os

from model import Podcast
from src.utils.kafka_conn import Kafka

kafka_conn = Kafka("empty")
DIR_PATH = os.getenv("DIR_PATH",r"C:\Users\Yaakov\PycharmProjects\muezzin\data\podcasts")

pathlist = Path(DIR_PATH).glob('**/*.wav')
for path in pathlist:
    path_in_str = str(path)
    file_metadata = path.stat()
    meta = Podcast(str(path),file_metadata)
    meta.printr()
