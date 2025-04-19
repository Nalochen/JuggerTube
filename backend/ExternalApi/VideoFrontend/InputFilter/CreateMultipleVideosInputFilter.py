from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import (
    InEnumValidator,
    IsStringValidator,
    RegexValidator,
    IsArrayValidator,
    ArrayLengthValidator,
)

class CreateMultipleVideosInputFilter(InputFilter):
    """The input filter for the create-multiple-videos route"""

    def __init__(self):
        """Initializes the CreateMultipleVideosInputFilter"""
        super().__init__()

        self.add(
            'videos',
            required=True,
            validators=[
                IsArrayValidator(),
                ArrayLengthValidator(min_length=1),
            ],
        )