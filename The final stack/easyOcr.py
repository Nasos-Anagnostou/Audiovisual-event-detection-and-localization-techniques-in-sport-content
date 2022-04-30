# OCR PREPROCESSING TEST
from filepaths import file_paths
import glob
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import re
import ntpath
import easyocr
from matplotlib import pyplot as plt

# EasyOcr Reader initialisation
reader = easyocr.Reader(['en'], gpu=False)
# under minute format
under_minute_format = '(([1-5][0-9]|[0-9])\.[0-9])'

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def easyOcr_dir(dir_path, time_pat):
    ttags = []
    counter_1 = 0
    counter_2 = 0

    # loop for every frame in the dir
    for filename in sorted(glob.glob(dir_path + '/*.png'), key=numericalSort):

        ftail = ntpath.split(filename)[1]

        result = reader.readtext(filename)[1][1]
        print("The frame has this elements: ", ftail, result)

        # dirty fix
        if not re.fullmatch(under_minute_format, result):
            result = result.replace('.', ':')

        counter_1 += 1
        if re.fullmatch(time_pat, result):
            # timetag parsing success inform
            print("This is a match!", result)

            new_res = result.replace(',', '.')

            z = re.findall('([0-9]+)', ftail)[0]
            ttags.append([new_res, z])
            counter_2 += 1

    # calculating the succes_rate for all frames OCRed
    success_rate = (counter_2 / counter_1) * 100

    # Printing stuff related to ocr success
    print("\nYou found {} out of {} images successfully.".format(counter_2, counter_1))
    print("\n Success rate of:", success_rate, "%")
    print("\n Timetags exported are: ", ttags)

    return ttags, success_rate
