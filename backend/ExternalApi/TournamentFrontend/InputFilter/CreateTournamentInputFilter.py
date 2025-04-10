from flask_inputfilter import InputFilter
from flask_inputfilter.Condition import TemporalOrderCondition
from flask_inputfilter.Validator import (
    IsStringValidator,
    IsUrlValidator,
    LengthValidator,
)

from ExternalApi.VideoFrontend.Filter import SanitizeStringFilter


class CreateTournamentInputFilter(InputFilter):
    """Input filter for tournament creation endpoint"""

    def __init__(self):
        super().__init__()

        self.add(
            'name',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
                LengthValidator(max_length=100)
            ]
        )

        self.add(
            'city',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
                LengthValidator(max_length=50)
            ]
        )

        self.add(
            'address',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
                LengthValidator(max_length=255)
            ]
        )

        self.add(
            'jtrLink',
            validators=[
                IsStringValidator(),
                IsUrlValidator(),
                LengthValidator(max_length=255),
            ]
        )

        self.add(
            'startDate',
            required=True,
            validators=[
                # IsDateTimeValidator() Existiert noch nicht, füge ich in der lib hinzu
            ]
        )

        self.add(
            'endDate',
            required=True,
            validators=[
                # IsDateTimeValidator() Existiert noch nicht, füge ich in der lib hinzu
            ]
        )

        self.addCondition(TemporalOrderCondition('startDate', 'endDate'))
