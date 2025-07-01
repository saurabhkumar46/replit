import json
from datetime import datetime

# Convert ISO8601 timestamp to milliseconds since epoch
def iso_to_millis(iso_string):
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# Function to unify data from data-1.json
def unify_data_1(data):
    return {
        "id": int(data["id"]),
        "user": data["user"],
        "timestamp_ms": iso_to_millis(data["timestamp"]),
        "value": data["reading"],
        "sensor_type": data["type"]
    }

# Function to unify data from data-2.json
def unify_data_2(data):
    return {
        "id": data["uid"],
        "user": data["username"],
        "timestamp_ms": data["time_ms"],
        "value": data["value"],
        "sensor_type": data["sensor"]
    }

if __name__ == "__main__":
    with open("data-1.json") as f1:
        data1 = json.load(f1)
    with open("data-2.json") as f2:
        data2 = json.load(f2)

    unified1 = unify_data_1(data1)
    unified2 = unify_data_2(data2)

    print("Unified data from data-1.json:")
    print(json.dumps(unified1, indent=2))
    print("Unified data from data-2.json:")
    print(json.dumps(unified2, indent=2))
