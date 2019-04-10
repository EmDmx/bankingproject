#This file takes the messages from kafka consumer and parses it to elasticsearch


from kafka import KafkaConsumer
from  elasticsearch import  Elasticsearch
#fast and easy to use module for timestamp parsing
import ciso8601
import time

#creating elasticsearch instance
es=Elasticsearch([{'host':'localhost', 'port':9200}])
i=0
topic='test'

#creating kafkaconsumer instance, starting from the earliest message
consumer = KafkaConsumer(topic, auto_offset_reset='earliest',bootstrap_servers=['localhost:9092'])

for msg in consumer:
    #I added a sleep time to synchron with reader and also to not use my cpu all the time
    time.sleep(0.5)

    if msg.serialized_value_size != 0:
        #manipulating the log for converting to dict
        Smsg=(str(msg.value))
        Smsg=Smsg.replace("b'",'')
        n=Smsg[:-3]
        Smsg=n
        listed=Smsg.split(" - ")

        #parsing Datetime
        dateTime=ciso8601.parse_datetime(listed[0])


        #converting log to dict
        dicts={'dateTime':dateTime, 'level':listed[-3], 'city':listed[-2],'desc':listed[-1]}


        es.index(index='teblogs',doc_type='cities',body=dicts,id=i)
        #giving an easy to remember id in elasticSearch
        i=i+1

        print(dicts)

#print(newlist)
#str_list = list(filter('', newlist))
#print(str_list)
