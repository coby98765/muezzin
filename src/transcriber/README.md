# muezzin/transcriber
transcription service that receives metadata report for podcasts file over kafka to topic `IMPORT_TOPIC` env, 
transcribes the podcast audio files and adds the transcripts to the report that is sent on Kafka to the next step to topic `EXPORT_TOPIC` env.
## ENV
```commandline
KAFKA_HOST
GROUP_ID
IMPORT_TOPIC
EXPORT_TOPIC
```
## Model 

```pyton
Podcast:
    name: str
    path: str
    size: int
    transcript:str
    last_open: datetime
    last_modified: datetime
    created_time: datetime
```
Export using `__dict__()` method

## Kafka
using the Kafka Connection Subscriber and Publisher From file: `src/utils/kafka_conn.py`

## Libraries
`kafka-python`, `os`, `datetime`,`logging`,`speech_recognition`.
