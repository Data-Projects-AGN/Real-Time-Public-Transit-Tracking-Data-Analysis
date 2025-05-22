import requests
from google.transit import gtfs_realtime_pb2
from kafka import KafkaProducer
import json
import time
from google.protobuf.json_format import MessageToDict


def fetch_gtfs_feed(url):
    response = requests.get(url)
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='10.21.168.19:9092'
    # ,
    # value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


# URLs
# alerts_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/alerts.pb"
positions_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/position_updates.pb"
# trips_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/trip_updates.pb"

try:
    while True:
        print("-----------------------------------------------")
        positions = fetch_gtfs_feed(positions_url)

        header_dict = MessageToDict(positions.header)

        # header_json = json.dumps(header_dict).encode('utf-8')

        for entity in positions.entity:

            entity_dict = MessageToDict(entity)

            # merged_dict = {**header_json, **entity_json}

            for h_key in header_dict.keys():
                entity_dict[h_key] = header_dict[h_key]

            merged_json =  json.dumps(entity_dict).encode('utf-8')

            topic = f"positions"
            producer.send(topic, merged_json).get(timeout=10)

            print(f"Sent to [{topic}]:", header_dict)
        
        time.sleep(120)

finally:
    producer.flush()
    producer.close()