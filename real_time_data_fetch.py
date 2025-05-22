import requests
from google.transit import gtfs_realtime_pb2

def fetch_gtfs_feed(url):
    response = requests.get(url)
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed

# URLs
alerts_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/alerts.pb"
positions_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/position_updates.pb"
trips_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/trip_updates.pb"

# Example: Fetch Trip Updates
trip_updates = fetch_gtfs_feed(trips_url)
print(trip_updates)

# positions = fetch_gtfs_feed(positions_url)
# print(positions)

# alerts = fetch_gtfs_feed(alerts_url)
# print(alerts)

# for entity in trip_updates.entity:
#     if entity.HasField('trip_update'):
#         print("Trip ID:", entity.trip_update.trip.trip_id)
#         for stop_time_update in entity.trip_update.stop_time_update:
#             print("  Stop ID:", stop_time_update.stop_id)
#             if stop_time_update.HasField("arrival"):
#                 print("    Arrival:", stop_time_update.arrival.time)
#             if stop_time_update.HasField("departure"):
#                 print("    Departure:", stop_time_update.departure.time)