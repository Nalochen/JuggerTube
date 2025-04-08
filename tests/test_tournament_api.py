import requests
import json
from datetime import datetime, timedelta

def test_create_tournament():
    """Test cases for tournament creation endpoint"""
    base_url = "http://localhost:5000/api/tournament-frontend/create-tournament"
    headers = {"Content-Type": "application/json"}

    # Test case 1: Valid data
    valid_data = {
        "name": "Test Tournament 2024",
        "city": "Hamburg",
        "startDate": "2024-08-15T09:00:00",
        "endDate": "2024-08-16T18:00:00",
        "address": "Sportplatz Hamburg, Teststraße 1, 20095 Hamburg",
        "jtrLink": "https://turniere.jugger.org/tournament.php?id=999"
    }
    
    print("\nTest Case 1: Valid data")
    response = requests.post(base_url, headers=headers, json=valid_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test case 2: Missing required field
    invalid_data = valid_data.copy()
    del invalid_data["name"]
    
    print("\nTest Case 2: Missing required field (name)")
    response = requests.post(base_url, headers=headers, json=invalid_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test case 3: Invalid date format
    invalid_date_data = valid_data.copy()
    invalid_date_data["startDate"] = "2024-08-15" # Wrong format
    
    print("\nTest Case 3: Invalid date format")
    response = requests.post(base_url, headers=headers, json=invalid_date_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test case 4: End date before start date
    invalid_dates_data = valid_data.copy()
    invalid_dates_data["endDate"] = "2024-08-14T18:00:00"
    
    print("\nTest Case 4: End date before start date")
    response = requests.post(base_url, headers=headers, json=invalid_dates_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test case 5: Invalid URL format
    invalid_url_data = valid_data.copy()
    invalid_url_data["jtrLink"] = "not-a-url"
    
    print("\nTest Case 5: Invalid URL format")
    response = requests.post(base_url, headers=headers, json=invalid_url_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Test case 6: Invalid content type
    print("\nTest Case 6: Invalid content type")
    response = requests.post(base_url, headers={"Content-Type": "text/plain"}, data="invalid data")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    test_create_tournament() 