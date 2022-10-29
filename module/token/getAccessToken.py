import requests
import os
from dotenv import load_dotenv


def getAccessToken() -> str:
    load_dotenv()

    url = "https://accounts.nintendo.com/connect/1.0.0/api/token"

    headers = {
        "Host": "accounts.nintendo.com",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "Accept-Language": "ja-JP",
        "Accept-Encoding": "gzip, deflate, br",
    }

    params = {
        "client_id": os.environ["CLIENT_ID"],
        "session_token": os.environ["NINTENDO_SESSION_TOKEN"],
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer-session-token",
    }

    data = requests.post(url=url, headers=headers, json=params)

    if data.status_code == 400:
        return data.json()["error_description"]

    return data.json()["access_token"]
