import requests
import os
from dotenv import load_dotenv


def getBulletToken(xGamewebtoken: str):
    load_dotenv()
    url = "https://api.lp1.av5ja.srv.nintendo.net/api/bullet_tokens"

    headers = {
        "Host": "api.lp1.av5ja.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja-JP",
        "X-Web-View-Ver": os.environ["WEB_VIEW_VER"],
        "X-GameWebToken": xGamewebtoken,
    }

    data = requests.post(url=url, headers=headers)

    print(xGamewebtoken)
    print(data)

    return data.json()
