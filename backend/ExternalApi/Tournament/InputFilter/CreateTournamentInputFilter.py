from functools import wraps
import re
from typing import Optional

from flask import request, jsonify

from DataDomain.Model import Response
from ExternalApi.Tournament.Validator.CreateTournamentValidator import CreateTournamentValidator


class CreateTournamentInputFilter:
    """Input filter for tournament creation endpoint"""

    @staticmethod
    def _sanitize_string(value: Optional[str]) -> Optional[str]:
        """Sanitize string input to prevent XSS"""
        if value is None:
            return None
        # Remove any HTML tags
        value = re.sub(r'<[^>]*?>', '', value)
        # Convert special characters to HTML entities
        value = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        value = value.replace('"', '&quot;').replace("'", '&#x27;')
        return value.strip()

    @staticmethod
    def _is_valid_url(url: str) -> bool:
        """Validate URL format"""
        if not url:
            return True
        
        # URL pattern
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return bool(url_pattern.match(url))

    @staticmethod
    def validate():
        """
        Decorator to validate tournament creation input data
        """
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                # Check content type
                if not request.is_json:
                    return Response(
                        response=jsonify({
                            "message": "Invalid content type. Expected application/json",
                            "errors": {"content_type": "Must be application/json"}
                        }),
                        status=400
                    )

                try:
                    data = request.get_json()
                except Exception as e:
                    return Response(
                        response=jsonify({
                            "message": "Invalid JSON format",
                            "errors": {
                                "json": "Could not parse JSON data",
                                "details": str(e)
                            }
                        }),
                        status=400
                    )

                if not data:
                    return Response(
                        response=jsonify({
                            "message": "Empty request body",
                            "errors": {"body": "Request body cannot be empty"}
                        }),
                        status=400
                    )

                # Sanitize string inputs
                for field in ['name', 'city', 'address', 'jtrLink']:
                    if field in data:
                        data[field] = CreateTournamentInputFilter._sanitize_string(data[field])

                # Validate URL format for jtrLink
                if 'jtrLink' in data and data['jtrLink']:
                    if not CreateTournamentInputFilter._is_valid_url(data['jtrLink']):
                        return Response(
                            response=jsonify({
                                "message": "Invalid input data",
                                "errors": {
                                    "jtrLink": "Invalid URL format"
                                }
                            }),
                            status=400
                        )

                # Validate input data
                is_valid, errors = CreateTournamentValidator.validate(data)
                if not is_valid:
                    return Response(
                        response=jsonify({
                            "message": "Invalid input data",
                            "errors": errors
                        }),
                        status=400
                    )

                # Store sanitized data in request context
                request.validated_data = data
                return f(*args, **kwargs)

            return decorated_function
        return decorator 