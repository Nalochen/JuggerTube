import json
from typing import Any

from flask import Response as FlaskResponse, jsonify

from DataDomain.Model import CustomJSONEncoder


class Response(FlaskResponse):
    """Custom Response class that handles JSON serialization"""

    def __init__(self, response: Any = None, status=200, **kwargs):
        """Custom Response constructor"""

        if isinstance(response, FlaskResponse):
            super().__init__(
                response=response.response,
                status=response.status,
                headers=response.headers,
                **kwargs
            )
        else:
            super().__init__(
                response=jsonify(response).response,
                status=status,
                mimetype='application/json',
                **kwargs
            )
