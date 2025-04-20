from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import (
    IsArrayValidator,
    ArrayLengthValidator
)

class CreateMultipleTournamentsInputFilter(InputFilter):
    """The input filter for the create-multiple-tournaments route"""

    def __init__(self):
        """Initializes the CreateMultipleTournamentsInputFilter"""
        super().__init__()

        self.add(
            'tournaments',
            required=True,
            validators=[
                IsArrayValidator(),
                ArrayLengthValidator(min_length=1),
            ],
        )