import pandas as pd
import requests
from urllib3.exceptions import InsecureRequestWarning
import time
import math
from enums import TARGET_SHEETS, VideoCategoriesEnum
from data_processor import DataProcessor
from helpers import send_data_to_backend


# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Path to the Excel file
excel_file = 'Liste aller Juggervideos _ JuggerTube.xlsx'

# Specify the sheets we want to analyze
target_sheets = ['DATA-Videos', 'DATA-Teams', 'DATA-Channels', 'Output-Tournaments']

# Read all sheets from the Excel file
excel = pd.ExcelFile(excel_file)

# Dictionaries to store channels and teams
channels_dict = {}
teams_dict = {}
videos_dict = {}

# Get valid category values
valid_categories = {category.value for category in VideoCategoriesEnum}

def main():
    # Initialize data processor
    processor = DataProcessor(excel_file)
    
    # Process each sheet
    for sheet_name in TARGET_SHEETS:
        if sheet_name not in processor.excel.sheet_names:
            print(f"Warning: Sheet '{sheet_name}' not found in the Excel file.")
            continue

        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        if sheet_name == 'DATA-Channels':
            processor.process_channels(df)
        elif sheet_name == 'DATA-Teams':
            processor.process_teams(df)
        elif sheet_name == 'DATA-Videos':
            processor.process_videos(df)

    # Prepare and send data to backend
    teams_list, channels_list, videos_list = processor.prepare_data_for_api()

    # Send teams data
    teams_success = send_data_to_backend(
        '/api/team-frontend/create-multiple-teams',
        {"teams": teams_list},
        'teams'
    )

    if teams_success:
        print("Teams data sent successfully")
        
        # Send channels data
        channels_success = send_data_to_backend(
            '/api/channel-frontend/create-multiple-channels',
            {"channels": channels_list},
            'channels'
        )

        if channels_success:
            print("Channels data sent successfully")
            
            # Wait for teams and channels to be processed
            time.sleep(2)
            
            # Send videos data
            videos_success = send_data_to_backend(
                '/api/video-frontend/create-multiple-videos',
                {"videos": videos_list},
                'videos'
            )

            if videos_success:
                print("All data successfully sent to backend!")
            else:
                print("Failed to send videos data")
        else:
            print("Failed to send channels data")
    else:
        print("Failed to send teams data")

if __name__ == "__main__":
    main()

# Function to check if a value is JSON serializable
def clean_value(value):
    if pd.isna(value) or (isinstance(value, float) and (math.isnan(value) or math.isinf(value))):
        return None
    return str(value) if value is not None else None

# Function to send data to backend
def send_data_to_backend(endpoint, data, entity_name):
    try:
        response = requests.post(
            f'https://localhost:8080{endpoint}',
            json=data,
            verify=False  # Since it's localhost, we can skip SSL verification
        )
        response.raise_for_status()
        print(f"\nSuccessfully sent {entity_name} data to backend")
        return True
    except requests.exceptions.RequestException as e:
        print(f"\nError sending {entity_name} data to backend: {str(e)}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"Response content: {e.response.text}")
        return False

print("\nAnalysis complete!") 