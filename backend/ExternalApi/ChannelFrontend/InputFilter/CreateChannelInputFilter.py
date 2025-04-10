from functools import wraps

from flask import request

from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Validator.CreateChannelValidator import CreateChannelValidator


class CreateChannelInputFilter:
    """Input filter for channel creation endpoint"""

    @staticmethod
    def validate():
        """
        Decorator to validate channel creation input data
        
        Returns:
            callable: Decorated function
        """
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                # Validate request data
                is_valid, errors = CreateChannelValidator.validate(request.get_json())
                
                if not is_valid:
                    return Response(
                        response={"errors": errors},
                        status=400
                    )
                
                # Store validated data
                request.validated_data = request.get_json()
                
                return f(*args, **kwargs)
            return decorated_function
        return decorator 