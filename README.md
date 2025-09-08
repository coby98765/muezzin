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

