import pandas as pd
import math
import requests
from typing import Any, Dict, Optional

def clean_value(value: Any) -> Optional[str]:
    """Convert a value to a string, handling NaN and None values."""
    if pd.isna(value) or (isinstance(value, float) and (math.isnan(value) or math.isinf(value))):
        return None
    return str(value) if value is not None else None

def send_data_to_backend(endpoint: str, data: Dict, entity_name: str) -> bool:
    """Send data to the backend API."""
    try:
        response = requests.post(
            f'https://localhost:8080{endpoint}',
            json=data,
            verify=False
        )
        response.raise_for_status()
        print(f"Successfully sent {entity_name} data to backend")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending {entity_name} data to backend: {str(e)}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"Response content: {e.response.text}")
        return False 