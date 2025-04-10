from flask_inputfilter import InputFilter
from flask_inputfilter.Validator import (
    InEnumValidator,
    IsIntegerValidator,
    IsStringValidator,
    IsUrlValidator,
    LengthValidator,
)

from DataDomain.Database.Enum import (
    GameSystemTypesEnum,
    VideoCategoriesEnum,
    WeaponTypesEnum,
)
from ExternalApi.VideoFrontend.Filter import SanitizeStringFilter


class CreateVideoInputFilter(InputFilter):
    """Input filter for video creation endpoint"""

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
            'topic',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
            ]
        )

        self.add(
            'guests',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
            ]
        )

        self.add(
            'comment',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                IsStringValidator(),
            ]
        )

        self.add(
            'video_link',
            required=True,
            validators=[
                IsStringValidator(),
                IsUrlValidator(),
                LengthValidator(max_length=255),
            ]
        )

        self.add(
            'channel_id',
            required=True,
            validators=[
                IsIntegerValidator()
            ]
        )

        self.add(
            'category',
            required=True,
            filters=[
                SanitizeStringFilter()
            ],
            validators=[
                InEnumValidator(VideoCategoriesEnum)
            ]
        )

        self.add(
            'upload_date',
            required=True,
            validators=[
                # IsDateTimeValidator() Existiert noch nicht, füge ich in der lib hinzu
            ]
        )

        self.add(
            'date_of_recording',
            required=True,
            validators=[
                # IsDateTimeValidator() Existiert noch nicht, füge ich in der lib hinzu
            ]
        )

        self.add(
            'game_system',
            required=True,
            validators=[
                InEnumValidator(GameSystemTypesEnum)
            ]
        )

        self.add(
            'weapon_type',
            required=True,
            validators=[
                InEnumValidator(WeaponTypesEnum)
            ]
        )

        self.add(
            'tournament_id',
            validators=[
                IsIntegerValidator()
            ]
        )

        self.add(
            'team_one_id',
            validators=[
                IsIntegerValidator()
            ]
        )

        self.add(
            'team_two_id',
            validators=[
                IsIntegerValidator()
            ]
        )
