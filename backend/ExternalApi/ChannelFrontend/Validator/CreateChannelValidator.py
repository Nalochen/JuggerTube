from typing import Dict, Optional, Tuple
import re

class CreateChannelValidator:
    """Validator for channel creation input data"""

    @staticmethod
    def _is_valid_url(url: str) -> bool:
        """Validate URL format"""
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return bool(url_pattern.match(url))

    @staticmethod
    def validate(data: Dict) -> Tuple[bool, Optional[Dict[str, str]]]:
        """
        Validate channel creation input data
        
        Args:
            data (Dict): Input data to validate
            
        Returns:
            Tuple[bool, Optional[Dict[str, str]]]: (is_valid, error_messages)
        """
        errors = {}

        # Required string fields validation
        required_string_fields = {
            'name': (1, 100),
            'channel_link': (1, 255)
        }

        for field, (min_len, max_len) in required_string_fields.items():
            if field not in data or not isinstance(data[field], str):
                errors[field] = f"{field} is required and must be a string"
            elif not min_len <= len(data[field].strip()) <= max_len:
                errors[field] = f"{field} must be between {min_len} and {max_len} characters"

        # Validate channel_link URL format
        if 'channel_link' in data and isinstance(data['channel_link'], str):
            if not CreateChannelValidator._is_valid_url(data['channel_link']):
                errors['channel_link'] = "Invalid URL format"

        return len(errors) == 0, errors if errors else None 