from flask_inputfilter import InputFilter
from flask_inputfilter.Enum import RegexEnum
from flask_inputfilter.Filter import (
    StringTrimFilter,
    ToIntegerFilter,
    ToNullFilter,
)
from flask_inputfilter.Validator import (
    InEnumValidator,
    IsIntegerValidator,
    IsStringValidator,
    RegexValidator,
)

from DataDomain.Database.Enum import (
    GameSystemTypesEnum,
    VideoCategoriesEnum,
    WeaponTypesEnum,
)


class CreateVideoInputFilter(InputFilter):
    """The input filter for the create-video route"""

    def __init__(self):
        """Initializes the CreateVideoInputFilter"""

        super().__init__()

        self.add(
            'name',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'category',
            required=True,
            filters=[ToNullFilter()],
            validators=[
                InEnumValidator(
                    VideoCategoriesEnum
                )
            ]
        )

        self.add(
            'videoLink',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'uploadDate',
            required=True,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Anmeldedatum muss im iso format sein.'
                )
            ]
        )

        self.add(
            'channelLink',
            required=True,
            filters=[StringTrimFilter(), ToNullFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'comment',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'dateOfRecording',
            required=False,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Aufnahmedatum muss im iso format sein.'
                )
            ]
        )

        self.add(
            'topic',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'guests',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'weaponType',
            required=False,
            validators=[
                InEnumValidator(WeaponTypesEnum)
            ]
        )

        self.add(
            'gameSystem',
            required=False,
            validators=[
                InEnumValidator(GameSystemTypesEnum)
            ]
        )

        # Tournament object validation
        self.add(
            'tournament.id',
            required=False,
            filters=[ToIntegerFilter()],
            validators=[IsIntegerValidator()]
        )

        self.add(
            'tournament.name',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'tournament.city',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'tournament.startDate',
            required=False,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Turnier-Startdatum muss im iso format sein.'
                )
            ]
        )

        self.add(
            'tournament.endDate',
            required=False,
            validators=[
                RegexValidator(
                    RegexEnum.ISO_DATE.value,
                    'Das Turnier-Enddatum muss im iso format sein.'
                )
            ]
        )

        # Team One object validation
        self.add(
            'teamOne.id',
            required=False,
            filters=[ToIntegerFilter()],
            validators=[IsIntegerValidator()]
        )

        self.add(
            'teamOne.teamName',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'teamOne.city',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        # Team Two object validation
        self.add(
            'teamTwo.id',
            required=False,
            filters=[ToIntegerFilter()],
            validators=[IsIntegerValidator()]
        )

        self.add(
            'teamTwo.teamName',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )

        self.add(
            'teamTwo.city',
            required=False,
            filters=[StringTrimFilter()],
            validators=[IsStringValidator()]
        )
