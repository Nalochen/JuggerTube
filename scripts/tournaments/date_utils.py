from datetime import datetime

def format_date(date_str):
    """Format date string to ISO format with time"""
    if not date_str:
        return None
    try:
        # First try to parse date with time (format: DD.MM.YYYY HH:mm Uhr)
        try:
            parsed_date = datetime.strptime(date_str.strip(), '%d.%m.%Y %H:%M Uhr')
            return parsed_date.strftime('%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            # If that fails, try just the date (format: DD.MM.YYYY)
            parsed_date = datetime.strptime(date_str.strip(), '%d.%m.%Y')
            # For dates without time, set to start of day
            return parsed_date.strftime('%Y-%m-%d 00:00:00.000000')
    except ValueError as e:
        print(f"Error parsing date '{date_str}': {e}")
        return None 