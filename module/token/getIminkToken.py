import requests


def getIminkToken(token: str, hashMethod: int):

    url = "https://api.imink.app/f"
    headers = {
        "Host": "api.imink.app",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "discord-information-bot",
    }
    params = {"token": token, "hash_method": hashMethod}

    data = requests.post(url=url, headers=headers, json=params)

    return data.json()
