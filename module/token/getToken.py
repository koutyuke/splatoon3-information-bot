from retry import retry

from module.token.getAccessToken import getAccessToken
from module.token.getBulletToken import getBulletToken
from module.token.getIminkToken import getIminkToken
from module.token.getLoginAccessToken import getLoginAccessToken
from module.token.getWebServiceToken import getWebServiceToken
from module.token.productVersion import ProductVarsion


@retry(tries=1)
def getToken() -> str:

    accessToken = getAccessToken()
    product = ProductVarsion()

    if not product:
        return "No-Product-Varsion"

    if accessToken == "The provided grant is invalid":
        return "Invalid-AccessToken"

    iminkToken1 = getIminkToken(token=accessToken, hashMethod=1)

    loginAccessToken = getLoginAccessToken(
        f=iminkToken1["f"],
        naIdToken=accessToken,
        timestamp=iminkToken1["timestamp"],
        requestId=iminkToken1["request_id"],
        product=product,
    )

    if loginAccessToken["status"] == 9427:
        return "Low-Product-Version"

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
        product=product,
    )

    if webServiceToken["status"] == 9427:
        return "Low-Product-Version"

    bulletToken = getBulletToken(xGameWebToken=webServiceToken["result"]["accessToken"])

    # print(bulletToken)

    return bulletToken["bulletToken"]


if __name__ == "__main__":
    getToken()
