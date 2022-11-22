import cv2
import numpy as np
from PIL import Image


def createScheduleImage(data: object):
    for rule in ["regular", "open", "challenge", "x", "league"]:
        for i in range(3):
            type = "now" if i == 0 else "next" if i == 1 else "nextnext"
            imageArr = data[rule][i]["stage"]

            pilImg1 = Image.open(f"module/image/stage/{imageArr[0]}.jpg")
            img1 = np.array(pilImg1)
            if img1.ndim == 3:
                img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
            img1 = cv2.resize(img1, dsize=(400, 200))

            pilImg2 = Image.open(f"module/image/stage/{imageArr[1]}.jpg")
            img2 = np.array(pilImg2)
            if img2.ndim == 3:
                img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
            img2 = cv2.resize(img2, dsize=(400, 200))

            afterImage = cv2.hconcat([img1, img2])
            cv2.imwrite(f"module/image/schedule/{rule}/{type}.jpg", afterImage)
