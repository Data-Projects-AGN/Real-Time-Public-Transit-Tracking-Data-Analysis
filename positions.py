# import requests
# from google.transit import gtfs_realtime_pb2

# def fetch_gtfs_feed(url):
#     response = requests.get(url)
#     feed = gtfs_realtime_pb2.FeedMessage()
#     feed.ParseFromString(response.content)
#     return feed

# # URLs
# positions_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/position_updates.pb"

# positions = fetch_gtfs_feed(positions_url)
# print(positions)

import requests
import pandas as pd
from google.transit import gtfs_realtime_pb2

def fetch_full_vehicle_data(url):
    response = requests.get(url)
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    data = []
    for entity in feed.entity:
        if entity.HasField("vehicle"):
            v = entity.vehicle
            row = {
                "entity_id": entity.id,
                "trip_id": v.trip.trip_id if v.HasField("trip") else None,
                "route_id": v.trip.route_id if v.trip.HasField("route_id") else None,
                "latitude": v.position.latitude if v.HasField("position") else None,
                "longitude": v.position.longitude if v.HasField("position") else None,
                "bearing": v.position.bearing if v.position.HasField("bearing") else None,
                "odometer": v.position.odometer if v.position.HasField("odometer") else None,
                "speed": v.position.speed if v.position.HasField("speed") else None,
                "current_status": v.current_status if v.HasField("current_status") else None,
                "current_stop_sequence": v.current_stop_sequence if v.HasField("current_stop_sequence") else None,
                "stop_id": v.stop_id if v.HasField("stop_id") else None,
                "timestamp": v.timestamp if v.HasField("timestamp") else None,
                "vehicle_id": v.vehicle.id if v.HasField("vehicle") else None,
                "vehicle_label": v.vehicle.label if v.HasField("vehicle") else None,
                "license_plate": v.vehicle.license_plate if v.vehicle.HasField("license_plate") else None
            }
            data.append(row)

    return pd.DataFrame(data)

# Example usage
positions_url = "https://s3.amazonaws.com/etatransit.gtfs/bloomingtontransit.etaspot.net/position_updates.pb"
df_all_fields = fetch_full_vehicle_data(positions_url)

# Display
import ace_tools as tools; tools.display_dataframe_to_user(name="Full GTFS Vehicle Position Feed", dataframe=df_all_fields)
