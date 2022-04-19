# OCR PREPROCESSING TEST
from filepaths import file_paths
import glob
import pytesseract
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import re
import ntpath

import easyocr
from matplotlib import pyplot as plt

dir_path = r"E:/Career files/Degree Thesis/Dataset/image processing/temp/"
reader = easyocr.Reader(['en'], gpu=False)


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# loop for every frame in the dir
for filename in sorted(glob.glob(dir_path + '/*.png'), key=numericalSort):
    result = reader.readtext(filename)
    print(result)


