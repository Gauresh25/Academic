import requests
import json

# Replace with your deployed Cloud Function URL
FUNCTION_URL = "https://asia-south1-mediflow-433918.cloudfunctions.net/function-1"

# Sample data
test_data = {
    "origin": "40.7128,-74.0060",  # New York City coordinates
    "destinations": [
        "34.0522,-118.2437",  # Los Angeles coordinates
        "41.8781,-87.6298",  # Chicago coordinates
        "29.7604,-95.3698"  # Houston coordinates
    ]
}


def test_distance_function(url, data):
    try:
        # Send POST request to the Cloud Function
        response = requests.post(url, json=data)

        # Check if the request was successful
        response.raise_for_status()

        # Parse and print the JSON response
        result = response.json()
        print("Function Response:")
        print(json.dumps(result, indent=2))

        # Print distances and durations
        for i, destination in enumerate(result):
            print(f"\nDestination {i + 1}:")
            print(f"Distance: {destination['distance']}")
            print(f"Duration: {destination['duration']}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    print("Testing Distance and ETA Calculation Function...")
    test_distance_function(FUNCTION_URL, test_data)