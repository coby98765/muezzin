# muezzin/retriever

builds a metadata report per podcast file in folder, 
and sends report over kafka to topic `EXPORT_TOPIC` env.
## ENV
```commandline
KAFKA_HOST
GROUP_ID
DIR_PATH
EXPORT_TOPIC
```
## Model 

```pyton
Podcast:
    name: str
    path: str
    size: int
    last_open: datetime
    last_modified: datetime
    created_time: datetime
```
Export using `__dict__()` method

## Kafka
using the Kafka Connection and Publisher From file: `src/utils/kafka_conn.py`

## Libraries
`kafka-python`,`pathlib`, `os`, `datetime`.
