import time

from kafka  import  KafkaProducer

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))




producer=  KafkaProducer(bootstrap_servers=['localhost:9092'])

#producer=SimpleProducer(kafka)


#producer.send_messages("try")

def read(filePath):
    lastLine = None
#reads whole file first
    with open(filePath, 'r') as f:
        while True:
            line = f.readline()
            publish_message(producer,'test','log',line)
            if not line:
                break
            print("1"+line)
            lastLine = line

#then checks if the last line is changed
    while True:
        with open(filePath, 'r') as f:
            lines = f.readlines()
        if lines[-1] != lastLine:
            lastLine = lines[-1]
            publish_message(producer,'test','log',lastLine)
            print(lines[-1]+"2")


filePath = "./logs/test.log"
read(filePath)

