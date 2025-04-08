from datetime import datetime
from typing import Dict, Optional, Tuple

class CreateTournamentValidator:
    """Validator for tournament creation input data"""

    @staticmethod
    def validate(data: Dict) -> Tuple[bool, Optional[Dict[str, str]]]:
        """
        Validate tournament creation input data
        
        Args:
            data (Dict): Input data to validate
            
        Returns:
            Tuple[bool, Optional[Dict[str, str]]]: (is_valid, error_messages)
        """
        errors = {}

        # Required string fields validation
        required_string_fields = {
            'name': (1, 100),
            'city': (1, 50),
            'address': (1, 255)
        }

        for field, (min_len, max_len) in required_string_fields.items():
            if field not in data or not isinstance(data[field], str):
                errors[field] = f"{field} is required and must be a string"
            elif not min_len <= len(data[field].strip()) <= max_len:
                errors[field] = f"{field} must be between {min_len} and {max_len} characters"

        # Optional string fields validation
        if 'jtrLink' in data:
            if not isinstance(data['jtrLink'], str):
                errors['jtrLink'] = "jtrLink must be a string"
            elif len(data['jtrLink']) > 255:
                errors['jtrLink'] = "jtrLink must not exceed 255 characters"

        # Date validation
        try:
            if 'startDate' not in data:
                errors['startDate'] = "startDate is required"
            else:
                start_date = datetime.fromisoformat(data['startDate'].replace('Z', '+00:00'))

            if 'endDate' not in data:
                errors['endDate'] = "endDate is required"
            else:
                end_date = datetime.fromisoformat(data['endDate'].replace('Z', '+00:00'))

                # Check if start date is before end date
                if 'startDate' in data and start_date >= end_date:
                    errors['startDate'] = "startDate must be before endDate"

        except ValueError as e:
            if 'startDate' in str(e):
                errors['startDate'] = "Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"
            if 'endDate' in str(e):
                errors['endDate'] = "Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"

        return len(errors) == 0, errors if errors else None 