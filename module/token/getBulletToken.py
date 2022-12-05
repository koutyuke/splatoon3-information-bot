import requests
from module.token.webViewVersion import WebViewViersion


def getBulletToken(xGameWebToken: str):
    url = "https://api.lp1.av5ja.srv.nintendo.net/api/bullet_tokens"
    version = WebViewViersion()

    headers = {
        "Host": "api.lp1.av5ja.srv.nintendo.net",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja-JP",
        "X-Web-View-Ver": version,
        "X-GameWebToken": xGameWebToken,
    }

    data = requests.post(url=url, headers=headers)

    print(xGameWebToken)
    print(data)

    return data.json()
