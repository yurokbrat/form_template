import re
from datetime import datetime
from typing import Any


def validate_field_type(value: Any) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return "date"
    except ValueError:
        pass
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return "date"
    except ValueError:
        pass
    if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return "phone"
    if re.match(r"^\S+@\S+\.\S+$", value):
        return "email"
    return "text"
