# import dependencies
from pykafka import KafkaClient
import json
from datetime import datetime
import uuid

#Read Coordinates from Geojson
input_file = open('data/truman.json')
#Load json array
json_array = json.load(input_file)
#Grab the coordinate data from json_array
coordinates = json_array['features'][0]['geometry']['coordinates']
#print(type(coordinates))
#print(coordinates)

#Generate uuid
def generate_uuid():
    return uuid.uuid4()

#Kafka Producer

client = KafkaClient(hosts="localhost:9092")

topic = (client.topics['busdata'])

producer = topic.get_sync_producer()
 
#Construct Message and send to kafka
#define a dict
data = {}
data['busline'] = '00003'

def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['busline'] +  '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii'))
        
        #if bus reaches last coordinate, start from beginning
        if i == len(coordinates)-1:
            i = 0
        else:
            i += 1
generate_checkpoint(coordinates)

