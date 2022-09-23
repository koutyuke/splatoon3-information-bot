import requests
import sys
from os.path import dirname, abspath, basename, splitext

# sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from module.info.getInfo import getInfo
from glob import glob
from pprint import pprint


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


# if __name__ == "__main__":
#     print(
#         getBukiImage(
#             token="1_vwn2X6EufzBkzUhaDFvEvzSQ2fv2AbktZ6AfsB2v3LRRj2r_HdWUQcZplYOU-w2FN3-Poxb_dCq4ntp5qeyYaDxPOv7ctn-j1h0X7KHkx9C-3lBY7KeSuUqCY="
#         )
#     )
