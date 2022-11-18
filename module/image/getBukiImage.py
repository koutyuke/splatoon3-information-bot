import requests
from os.path import dirname, abspath, basename, splitext
from glob import glob
from module.info.getInfo import getInfo


def getBukiImage(token: str) -> list[str]:
    sha256Hash = "23c9b2b4ad878c2d91a68859be928dea"
    dirpath = dirname(abspath(__file__))
    files = glob(f"{dirpath}/buki/*") + glob(f"{dirpath}/buki/.*")
    nowBukiImageList = [splitext(basename(image))[0] for image in files]

    postResponse = getInfo(token=token, sha256Hash=sha256Hash)["data"]["weaponRecords"][
        "nodes"
    ]

    for bukiData in postResponse:
        if not bukiData["name"] in nowBukiImageList:
            bukiName = bukiData["name"]
            imagedata = requests.get(bukiData["image"]["url"]).content
            with open(f"{dirpath}/buki/{bukiName}.jpg", "wb") as f:
                f.write(imagedata)

    files = glob(f"{dirpath}/buki/*") + glob(f"{dirpath}/buki/.*")
    nowBukiImageList = [splitext(basename(image))[0] for image in files]

    return nowBukiImageList
