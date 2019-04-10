import time


from random import  randint
from random import choice

import logging
from logging.handlers import RotatingFileHandler

#Creating dict to determine content of messages
city={'Istanbul':'Hello-from-Istanbul','Tokyo':'Hello-from-Tokyo','Moscow':'Hello-from-Moscow','Beijing':'Hello-from-Beijing','London':'Hello-from-London'}
#creating contextfilter to add city and hello parts to log message
class ContextFilter(logging.Filter):

    def filter(self,record):
        content=choice(list(city))
        record.city=content
        record.hello=city[content]
        return  True

def main():
#name of the log
    path="./logs/test.log"
#creating contextfilter instance
    f=ContextFilter()
#format of log
    formatter=logging.Formatter('%(asctime)-15s - %(levelname)-8s - %(city)-8s - %(hello)-15s')
#creating instance of logger
    log = logging.getLogger()
#adding filter
    log.addFilter(f)
#creating the handler for limiting log files at 2mb and creating another many log files
    handler = RotatingFileHandler(path,maxBytes=2*1024*1024,backupCount=1000)
    handler.setFormatter(formatter)
#adding the handler to logger
    log.addHandler(handler)

    while True:
#assigning different level for each log output and slowing down the logs
        time.sleep(0.5)
        log.log(randint(0,5)*10,'')

#create_rotating_log(log_file)

if __name__=='__main__':
    main()
