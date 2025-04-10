from datetime import datetime
from typing import Dict, Tuple, Optional

from DataDomain.Database.Enum.GameSystemTypesEnum import GameSystemTypesEnum
from DataDomain.Database.Enum.VideoCategoriesEnum import VideoCategoriesEnum
from DataDomain.Database.Enum.WeaponTypesEnum import WeaponTypesEnum


class CreateVideoValidator:
    """Validator for video creation input data"""

    @staticmethod
    def validate(data: Dict) -> Tuple[bool, Optional[Dict[str, str]]]:
        """
        Validate video creation input data

        Args:
            data (Dict): Input data to validate

        Returns:
            Tuple[bool, Optional[Dict[str, str]]]: Tuple containing validation result and errors if any
        """
        errors = {}

        # Required string fields validation
        required_string_fields = {
            'name': 100,
            'video_link': 255
        }

        for field, max_length in required_string_fields.items():
            if field not in data or not data[field]:
                errors[field] = f"{field} is required"
            elif len(data[field]) > max_length:
                errors[field] = f"{field} cannot exceed {max_length} characters"

        # Channel ID validation
        if 'channel_id' not in data:
            errors['channel_id'] = "channel_id is required"
        elif not isinstance(data['channel_id'], int) or data['channel_id'] <= 0:
            errors['channel_id'] = "channel_id must be a positive integer"

        # Category validation
        if 'category' not in data:
            errors['category'] = "category is required"
        else:
            try:
                VideoCategoriesEnum(data['category'])
            except ValueError:
                errors['category'] = f"Invalid category. Must be one of: {', '.join([e.name for e in VideoCategoriesEnum])}"

        # Date validation
        try:
            if 'upload_date' not in data:
                errors['upload_date'] = "upload_date is required"
            else:
                datetime.fromisoformat(data['upload_date'].replace('Z', '+00:00'))

            if 'date_of_recording' in data and data['date_of_recording']:
                recording_date = datetime.fromisoformat(data['date_of_recording'].replace('Z', '+00:00'))
                upload_date = datetime.fromisoformat(data['upload_date'].replace('Z', '+00:00'))
                
                if recording_date > upload_date:
                    errors['date_of_recording'] = "date_of_recording cannot be after upload_date"

        except ValueError as e:
            if 'upload_date' in str(e):
                errors['upload_date'] = "Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"
            if 'date_of_recording' in str(e):
                errors['date_of_recording'] = "Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"

        # Optional enum validations
        if 'game_system' in data and data['game_system']:
            try:
                GameSystemTypesEnum(data['game_system'])
            except ValueError:
                errors['game_system'] = f"Invalid game_system. Must be one of: {', '.join([e.name for e in GameSystemTypesEnum])}"

        if 'weapon_type' in data and data['weapon_type']:
            try:
                WeaponTypesEnum(data['weapon_type'])
            except ValueError:
                errors['weapon_type'] = f"Invalid weapon_type. Must be one of: {', '.join([e.name for e in WeaponTypesEnum])}"

        # Optional ID validations
        optional_id_fields = ['tournament_id', 'team_one_id', 'team_two_id']
        for field in optional_id_fields:
            if field in data and data[field] is not None:
                if not isinstance(data[field], int) or data[field] <= 0:
                    errors[field] = f"{field} must be a positive integer"

        return len(errors) == 0, errors if errors else None 