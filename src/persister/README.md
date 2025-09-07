# muezzin/persister
receives metadata reports from kafka to topic `IMPORT_TOPIC` env, 
adds report to MongoDB and ElasticSearch

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
`kafka-python`,`pymongo`, `os`, `datetime`,`elasticsearch`.


## Elastic Mapping
```python
POST <index_name>/_mapping

{
"properties": {
"birthday": {
"type": "datetime",
"format": "yyyy-MM-dd”
},
"name": {
"properties": {
"first": {
"type": "keyword"
},
"last": {
"type": "keyword"
}
}
},
"bio": {
"type": "text"
}
}
}
```