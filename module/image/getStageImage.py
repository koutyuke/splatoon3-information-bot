import requests
import sys
from os.path import dirname, abspath, basename, splitext, split

# sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from module.info.getInfo import getInfo
from glob import glob
from pprint import pprint


def getStageImage(token: str):
    sha256Hash = ""
