import re
from typing import Any

from flask_inputfilter.Filter import BaseFilter


class SanitizeStringFilter(BaseFilter):

    def apply(self, value: Any):

        if not isinstance(value, str):
            return value

        value = re.sub(r'<[^>]*?>', '', value)

        value = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        value = value.replace('"', '&quot;').replace("'", '&#x27;')

        return value.strip()
