# Kafka BusData Streaming App
In this app we will stream busdata using kafka, the code is writen in Python (pykafka).
The data streamed here is generated from randomly picking latitudes and longitudes of specific bus lines from geojson.io website. in our case we are using Ride KC routes from the city of Kansas City Missouri.

# setting up kafka
for this project I am running kafka locally in my PC Machine, but you can run it from anywhere using vm or Mac the syntax is almost the same, you might need to use .sh extension while I am using a .bat extension.
to execute this project we need at least one kafka server and one zookeeper.
if you dont have Kafka you can download from https://kafka.apache.org/downloads after that you can unpack to latest version using whatever tool I used winrar for mine. you might also want to create data folder if runnung kafka locally, the folder will contain to more folder one for zookeeper data and the other for kafka data. do not forget to edit zookeeper config to refer to zookeeper properties path and kafka to refer to kafka properties path.
when all done we can start zookeeper: 

>>bin/windows/zookeeper-server-start.bat config/zookeeper.properties

then start kafka:
>>bin/windows/kafka-server-start.bat config/server.properties

if you using mac or vm you do not need windows floders besides your extension will .sh.

#  kafka producer
since we are writing our program in Python you also need to have Python installed in your machine I am using anaconda.
install pykafka:
>>pip install pykafka



