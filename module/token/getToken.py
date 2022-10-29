from retry import retry

from module.token.getAccessToken import getAccessToken
from module.token.getBulletToken import getBulletToken
from module.token.getIminkToken import getIminkToken
from module.token.getLoginAccessToken import getLoginAccessToken
from module.token.getWebServiceToken import getWebServiceToken


@retry()
def getToken() -> str:

    accessToken = getAccessToken()

    if accessToken == "The provided grant is invalid":
        return "InvalidAccessToken      "

    iminkToken1 = getIminkToken(token=accessToken, hashMethod=1)

    loginAccessToken = getLoginAccessToken(
        f=iminkToken1["f"],
        naIdToken=accessToken,
        timestamp=iminkToken1["timestamp"],
        requestId=iminkToken1["request_id"],
    )

    if loginAccessToken["status"] == 9427:
        return "Low-X-ProductVersion"

    iminkToken2 = getIminkToken(
        token=loginAccessToken["result"]["webApiServerCredential"]["accessToken"],
        hashMethod=2,
    )

    webServiceToken = getWebServiceToken(
        f=iminkToken2["f"],
        timestamp=iminkToken2["timestamp"],
        requestId=iminkToken2["request_id"],
        registrationToken=loginAccessToken["result"]["webApiServerCredential"][
            "accessToken"
        ],
    )

    if webServiceToken["status"] == 9427:
        return "LowProductVersion"

    bulletToken = getBulletToken(xGamewebtoken=webServiceToken["result"]["accessToken"])

    # print(bulletToken)

    return bulletToken["bulletToken"]


if __name__ == "__main__":
    getToken()
