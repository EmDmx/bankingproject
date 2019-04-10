#!/bin/bash

service elasticsearch start
service kibana start

/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties &
/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties &
/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic &

sleep 3
python3 logger.py &
sleep 3
python3 reader.py &
sleep 3
python3 consumer.py &
sleep 20 && curl -XPOST 0.0.0.0:5601/api/kibana/dashboards/import -H 'kbn-xsrf:true' -H 'Content-type:application/json' -d @./dashboard.json
