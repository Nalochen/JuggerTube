from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import IsStringValidator, IsUrlValidator, LengthValidator


class CreateChannelInputFilter(InputFilter):
    """Input filter for channel creation endpoint"""

    def __init__(self):
        super().__init__()

        self.add(
            "name",
            required=True,
            validators=[
                IsStringValidator(),
                LengthValidator(max_length=100),
            ]
        )

        self.add(
            "channel_link",
            required=True,
            validators=[
                IsStringValidator(),
                IsUrlValidator(),
                LengthValidator(max_length=255),
            ]
        )
