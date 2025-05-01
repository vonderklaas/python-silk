from datetime import datetime, timezone
from dateutil.parser import isoparse

def safe_parse_date(date_str: str) -> datetime:
    try:
        return isoparse(date_str).astimezone(timezone.utc)
    except Exception:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
