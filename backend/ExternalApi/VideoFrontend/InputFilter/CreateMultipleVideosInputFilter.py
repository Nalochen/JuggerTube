from flask_inputfilter import InputFilter
from flask_inputfilter.validators import (
    ArrayLengthValidator,
    IsArrayValidator,
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
