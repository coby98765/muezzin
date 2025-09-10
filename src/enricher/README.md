# muezzin/processor

receives metadata reports with transcripts for podcast that are flagged for being hostile, 
based on th transcripts podcasts need to be analyzed and categorized into danger categories,
incoming reports in Kafka topic `INPORT_TOPIC` (env), and after process will be exported to `EXPORT_TOPIC`(env).

## BDS Classification Guide
point system: 
- bds_percent: bad word points divided by the word count multiply by the sentiment score
- is_bds: if bds_percent > 35%
- bds_threat_level: 0-10 = "none", 11-35 = "medium", 36-100 = "high";

## ENV
```commandline
KAFKA_HOST
GROUP_ID
EXPORT_TOPIC
IMPORT_TOPIC
ES_HOST
```

## Kafka
using the Kafka Connection Subscriber and Publisher From file: `src/utils/kafka_conn.py`

## Libraries
`kafka-python`, `os`, `datetime`,`logging`.
