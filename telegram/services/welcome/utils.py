import pytz
from datetime import datetime


async def get_time(time_zone: str) -> str:
    tz = pytz.timezone(time_zone)
    time: datetime = datetime.now(tz)
    return time.strftime("%H:%M:%S")
