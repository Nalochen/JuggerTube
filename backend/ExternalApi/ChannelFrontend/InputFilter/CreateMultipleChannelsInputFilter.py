from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import (
    IsArrayValidator,
    ArrayLengthValidator
)


class CreateMultipleChannelsInputFilter(InputFilter):
    """Input filter for creating multiple channels"""

    def __init__(self):
        """Initializes the CreateMultipleChannelsInputFilter"""
        super().__init__()

        self.add(
            'channels',
            required=True,
            validators=[
                IsArrayValidator(),
                ArrayLengthValidator(min_length=1),
            ],
        )