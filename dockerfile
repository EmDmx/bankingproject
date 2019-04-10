FROM ubuntu

#ubuntu setup
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install wget -y

#INSTALLING JAVA
RUN apt install default-jdk -y
#SETTING JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/

#KAFKA INSTALLATION
RUN wget http://ftp.itu.edu.tr/Mirror/Apache/kafka/2.1.1/kafka_2.12-2.1.1.tgz
RUN tar xzf kafka_2.12-2.1.1.tgz
RUN mv kafka_2.12-2.1.1 /usr/local/kafka

#ELASTICSEARCH INSTALLATION
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.7.1.deb
RUN dpkg -i elasticsearch-6.7.1.deb

#KIBANA INSTALLATION
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-6.7.1-amd64.deb
RUN dpkg -i kibana-6.7.1-amd64.deb

#PYTHON
RUN apt-get install python3.6 -y
RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

#CURL INSTALLATION
RUN apt-get install curl -y

#WORKING DIRECTORY
ADD /App /App
WORKDIR /App

#INSTALLING PYTHON MODULES
RUN pip3 install -r requirements.txt

#CHANGING PROPER YML FILES FOR ELASTICSEARCH AND KIBANA
RUN printf "network.host: 0.0.0.0\n" >> /etc/elasticsearch/elasticsearch.yml
RUN printf "http.port: 9200" >> /etc/elasticsearch/elasticsearch.yml

RUN sed -i '/server.port:/s/^#//' /etc/kibana/kibana.yml
RUN sed -i '/server.host:/s/^#//' /etc/kibana/kibana.yml
RUN sed -i 's/"localhost"/0.0.0.0/' /etc/kibana/kibana.yml

#CHANGING THE MODE OF STARTING FILE
RUN chmod +x start.sh

#KIBANA PORT
EXPOSE 5601
#ELASTICSEARCH PORT
EXPOSE 9200
