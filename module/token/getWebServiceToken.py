import requests
import os
from dotenv import load_dotenv
from pprint import pprint


def getWebServiceToken(
    f: str, registrationToken: str, timestamp: int, requestId: str, product: str
):
    load_dotenv()
    url = "https://api-lp1.znc.srv.nintendo.net/v2/Game/GetWebServiceToken"

    headers = {
        "Host": "api-lp1.znc.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja-JP",
        "Content-Type": "application/json",
        "X-ProductVersion": product,
        "X-Platform": "iOS",
        "Authorization": f"Bearer {registrationToken}",
    }

    params = {
        "parameter": {
            "f": f,
            "id": os.environ["USER_ID"],
            "registrationToken": registrationToken,
            "timestamp": timestamp,
            "requestId": requestId,
        },
        "requestId": requestId,
    }

    data = requests.post(url=url, headers=headers, json=params)

    return data.json()
