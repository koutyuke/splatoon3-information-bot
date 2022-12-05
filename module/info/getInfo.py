import requests
from module.token.webViewVersion import WebViewViersion


def getInfo(token: str, sha256Hash: str):
    url = "https://api.lp1.av5ja.srv.nintendo.net/api/graphql"
    version = WebViewViersion()

    headers = {
        "Host": "api.lp1.av5ja.srv.nintendo.net",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-web-view-ver": version,
        "Authorization": f"Bearer {token}",
    }

    params = {
        "extensions": {
            "persistedQuery": {
                "sha256Hash": sha256Hash,
                "varsion": 1,
            }
        },
        "variables": {},
    }

    data = requests.post(url=url, headers=headers, json=params)

    return data.status_code, data.json()
