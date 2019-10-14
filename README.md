# Bankingproject

Data engineering project based on Elasticsearch, Kibana and Kafka. Creates and collects logs simultaneously and puts them into a streaming graph. 

# How Does It Work ? 

I would like to explain working proces with explaining the duty of the scripts.

"logger.py" in App folder creates log files continuosly in size of 2MB. In a format of "CITYNAME and Hello from CITYNAME".
"reader.py" in App folder reads those created logs in specified folder and sends them to the kafka producer. 
"consumer.py" in App folder gets those kafka messages from kafka consumer and parses them into elasticsearch. 

After this processes you should be seeing the logs in elasticsearch server. For me it was on the localhost.

# How to see logs in graph ? 

To see those logs in graph I used Kibana. 

Kibana is a data visualization plugin for elasticsearch.

"dashboard.json" in App folder is a necessary configuration file for elasticsearch Kibana. Since I used elasticsearch as a NoSQL database, I decided to use Kibana for graph work. 

You can add that dashboard.json file to kibana and automatically you will be seeing logs in a graph. 

# What does dockerfile do ? 

Dockerfile is a file to create this project as a docker image and after you download and run the dockerfile you will have a fully working environment. With all the stuff I mentioned above.
 
All you need to do is run start.sh inside docker image. 

To get docker image of the file, you can use the link below.
https://hub.docker.com/r/dockiron/bankproject

# Note: 
docker image of this project only runs on Unix environments due to memory limitations on windows. I will create and update it with it's docker compose version soon.

# Please don't hesitate to ask any questions. 
