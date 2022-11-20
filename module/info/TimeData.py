import re
import datetime
from zoneinfo import ZoneInfo


def createTimeData(startTimeStr: str, endTimeStr: str) -> str:
    startTimeNum = list(map(int, re.findall(r"\d+", startTimeStr)))
    endTimeNum = list(map(int, re.findall(r"\d+", endTimeStr)))

    startTime = datetime.datetime(
        int(startTimeNum[0]),
        int(startTimeNum[1]),
        int(startTimeNum[2]),
        int(startTimeNum[3]),
        0,
        0,
        0,
        tzinfo=datetime.timezone.utc,
    ).astimezone(ZoneInfo("Asia/Tokyo"))

    endTime = datetime.datetime(
        int(endTimeNum[0]),
        int(endTimeNum[1]),
        int(endTimeNum[2]),
        int(endTimeNum[3]),
        0,
        0,
        0,
        tzinfo=datetime.timezone.utc,
    ).astimezone(ZoneInfo("Asia/Tokyo"))
    time = f"{startTime.month}/{startTime.day} {startTime.hour}:00 - {endTime.month}/{endTime.day} {endTime.hour}:00"

    return time
