import requests


def getBulletToken(xGamewebtoken: str):
    url = "https://api.lp1.av5ja.srv.nintendo.net/api/bullet_tokens"

    headers = {
        "Host": "api.lp1.av5ja.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja-JP",
        "X-Web-View-Ver": "1.0.0-42f70e51",
        "X-GameWebToken": xGamewebtoken,
    }

    data = requests.post(url=url, headers=headers)

    return data.json()
