import requests
from os.path import dirname, abspath, basename, splitext, split
from module.info.getInfo import getInfo
from glob import glob
from pprint import pprint


def getStageImage(token: str) -> list[str]:
    sha256Hash = "56c46bdbdfa4519eaf7845ce9f3cd67a"
    dirpath = dirname(abspath(__file__))
    files = glob(f"{dirpath}/stage/*")
    nowStageImageList = [splitext(basename(image))[0] for image in files]

    postResponse = getInfo(token=token, sha256Hash=sha256Hash)["data"]["stageRecords"][
        "nodes"
    ]

    for stageData in postResponse:
        if not stageData["name"] in nowStageImageList:
            stageName = stageData["name"]
            imageData = requests.get(stageData["image"]["url"]).content
            with open(f"{dirpath}/stage/{stageName}.jpg", "wb") as f:
                f.write(imageData)
    files = glob(f"{dirpath}/stage/*")
    nowStageImageList = [splitext(basename(image))[0] for image in files]

    return nowStageImageList


# if __name__ == "__main__":
#     getStageImage(
#         token="vKhcSJMsKhnwyUFbgMpag2et3VW03U1Ht7KEoaV-MsYU-CDHOI-zY_jS2T4-e-Y2y85lqKG7SHxVOaNS4eKgXPK7Bc2ytYw5ItMp8ibpEJSuOb9zMGyRCbgSZ7Y="
#     )
