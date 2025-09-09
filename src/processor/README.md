# muezzin/processor

receives metadata reports with transcripts for podcast that are flagged for being hostile, 
based on th transcripts podcasts need to be analyzed and categorized into danger categories,
incoming reports in Kafka topic `INPORT_TOPIC` (env), and after process will be exported to `EXPORT_TOPIC`(env).
## ENV
```commandline
KAFKA_HOST
GROUP_ID
EXPORT_TOPIC
INPORT_TOPIC
ES_HOST
```

## Kafka
using the Kafka Connection Subscriber and Publisher From file: `src/utils/kafka_conn.py`

## Libraries
`kafka-python`, `os`, `datetime`,`logging`.
