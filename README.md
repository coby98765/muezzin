# muezzin

`
pip freeze > requirements.txt
`

`
pip install -r requirements.txt
`

pull MongoDB Image

`
docker pull mongodb/mongodb-community-server:latest
`

run MongoDB container

`
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
`

run Kafka container

`
docker run -d --name=kafka -p 9092:9092 apache/kafka
`

get kafka cluster id

`
docker exec -ti kafka /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server :9092
`