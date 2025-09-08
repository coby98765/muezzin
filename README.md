# muezzin

`
pip freeze > requirements.txt
`

`
pip install -r requirements.txt
`

create a Docker Volume:
```bash
docker volume create muezzin_volume
```

Create a temporary container and mount the volume, MOve Podcasts Files to volume:

```bash
docker run -d --rm --name my_temp_container -v muezzin_volume:/data alpine tail -f /dev/null

docker cp ./data/podcasts my_temp_container:/data
```
```bash
docker rm my_temp_container
```

pull MongoDB Image
```bash
docker pull mongodb/mongodb-community-server:latest
```

run MongoDB container
```bash
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```

run Kafka container
```bash
docker run -d --name=kafka -p 9092:9092 apache/kafka
```

ElasticSearch:
setup Network:
```bash
docker network create elastic-net
```
run elastic container:
```bash
docker run -d --name elasticsearch `
  --net elastic-net `
  -p 9200:9200 -p 9300:9300 `
  -e "discovery.type=single-node" `
  -e "xpack.security.enabled=false" `
  -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" `
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
  
```
run kinana container:
```bash
docker run -d --name kibana `
  --net elastic-net `
  -p 5601:5601 `
  -e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" `
  docker.elastic.co/kibana/kibana:8.15.0
```

connect existing ES to network:
```bash
docker network connect elastic-net es
```

[//]: # (    docker exec -it elasticsearch /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node)