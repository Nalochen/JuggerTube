from flask_inputfilter import InputFilter
from flask_inputfilter.Enum import RegexEnum
from flask_inputfilter.Filter import (
    StringTrimFilter,
    ToNullFilter,
)
from flask_inputfilter.Validator import (
    IsStringValidator,
    RegexValidator,
    IsArrayValidator,
    ArrayLengthValidator
)

class CreateTournamentInputFilter(InputFilter):
    """The input filter for the create-tournament route"""

    def __init__(self):
        """Initializes the CreateTournamentInputFilter"""

        super().__init__()

        self.add(
            'name',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'city',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'startDate',
            required=True,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Startdatum muss im iso format sein.'
                )
            ]
        )

        self.add(
            'endDate',
            required=False,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Enddatum muss im iso format sein.'
                )
            ]
        )

        self.add(
            'jtrLink',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
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