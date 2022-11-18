import requests
import sys
from os.path import dirname, abspath, basename, splitext, split
from module.info.getInfo import getInfo
from glob import glob
from pprint import pprint


def getStageImage(token: str):
    sha256Hash = ""
