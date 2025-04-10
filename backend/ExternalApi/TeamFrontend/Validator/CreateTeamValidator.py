from typing import Dict, Optional, Tuple

class CreateTeamValidator:
    """Validator for team creation input data"""

    @staticmethod
    def validate(data: Dict) -> Tuple[bool, Optional[Dict[str, str]]]:
        """
        Validate team creation input data
        
        Args:
            data (Dict): Input data to validate
            
        Returns:
            Tuple[bool, Optional[Dict[str, str]]]: (is_valid, error_messages)
        """
        errors = {}

        # Required string fields validation
        required_string_fields = {
            'name': (1, 100),
            'country': (2, 2),  # ISO country code
            'city': (1, 50)
        }

        for field, (min_len, max_len) in required_string_fields.items():
            if field not in data or not isinstance(data[field], str):
                errors[field] = f"{field} is required and must be a string"
            elif not min_len <= len(data[field].strip()) <= max_len:
                errors[field] = f"{field} must be between {min_len} and {max_len} characters"

        return len(errors) == 0, errors if errors else None 