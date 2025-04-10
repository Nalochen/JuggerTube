from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import IsStringValidator, LengthValidator


class CreateTeamInputFilter(InputFilter):
    """Input filter for team creation endpoint"""

    def __init__(self):
        super().__init__()

        self.add(
            "name",
            required=True,
            validators=[
                IsStringValidator(),
                LengthValidator(max=100)
            ]
        )

        self.add(
            "country",
            required=True,
            validators=[
                IsStringValidator(),
                LengthValidator(min=2, max=2)
            ]
        )

        self.add(
            "city",
            required=True,
            validators=[
                IsStringValidator(),
                LengthValidator(max=50)
            ]
        )
