import requests
import os
from dotenv import load_dotenv


def getLoginAccessToken(f: str, naIdToken: str, timestamp: int, requestId: str):
    load_dotenv()

    url = "https://api-lp1.znc.srv.nintendo.net/v3/Account/Login"

    headers = {
        "Host": "api-lp1.znc.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "X-ProductVersion": "2.2.0",
        "Accept-Language": "ja-JP",
        "X-Platform": "iOS",
    }

    params = {
        "parameter": {
            "f": f,
            "language": "ja-JP",
            "naCountry": "JP",
            "naBirthday": os.environ["USER_BIRTHDAY"],
            "naIdToken": naIdToken,
            "timestamp": timestamp,
            "requestId": requestId,
        },
        "requestId": requestId,
    }

    data = requests.post(url=url, headers=headers, json=params)

    return data.json()
