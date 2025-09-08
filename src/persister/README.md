# muezzin/persister
receives metadata reports from kafka to topic `IMPORT_TOPIC` env, 
create a file identifier based on created date like: `podcast1_` adds report to MongoDB and ElasticSearch

## ENV
```commandline
KAFKA_HOST
GROUP_ID
MONGO_HOST
MONGO_NAME
MONGO_COLL
IMPORT_TOPIC
ES_HOST
```

## Kafka
using the Kafka Connection and Subscriber From file: `src/utils/kafka_conn.py`

## Libraries
`kafka-python`,`pymongo`, `os`, `datetime`,`elasticsearch`,`logging`.


## Elastic Mapping
```python
class Podcast:
    _id:str
    name: str
    prev_path: str
    size: int
    last_open: datetime
    last_modified: datetime
    created_time: datetime
```