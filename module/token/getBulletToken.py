import requests
import os
from dotenv import load_dotenv


def getBulletToken(xGameWebToken: str):
    load_dotenv()
    url = "https://api.lp1.av5ja.srv.nintendo.net/api/bullet_tokens"

    headers = {
        "Host": "api.lp1.av5ja.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja-JP",
        "X-Web-View-Ver": os.environ["WEB_VIEW_VER"],
        "X-GameWebToken": xGameWebToken,
    }

    data = requests.post(url=url, headers=headers)

    print(xGameWebToken)
    print(data)

    return data.json()
