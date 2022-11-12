# author: Nasos Anagnostou
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# pytesseract and easyOCR engine used to parse timetags for each frame detected
# latest update 6/4/22


import pytesseract
import easyocr
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import glob
import re
import ntpath
import filepaths


# tesseract allocation
pytesseract.pytesseract.tesseract_cmd = r"E:\programs\tessaract\tesseract.exe"

# EasyOcr Reader initialisation
reader = easyocr.Reader(['en'], gpu=False)

# under minute format
under_minute_format = '(([1-5][0-9]|[0-9])\.[0-9])'

# creating method to sort image files in folder based in frame number low to high
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# tesseract ocr function
def tess_dir(dir_path, time_pattern, configure):
    # initialise vars
    counter_1 = 0
    counter_2 = 0
    timetags = []
    failrec = []

    # loop for every frame in the dir
    for filename in sorted(glob.glob(dir_path + '/*.png'), key=numericalSort):

        # get the filename not the whole path
        ftail = ntpath.split(filename)[1]

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # input frame in opencv and convert color
        im_cv2 = cv2.imread(filename)
        im_cv2 = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2RGB)

        # import frame to PIM
        pim = Image.fromarray(im_cv2)
        # pim = Image.open(filename)             #show image

        # 1. enhance image sharpness given a specific factor
        enhancer = ImageEnhance.Sharpness(pim)
        factor_sharp = 2
        pim_en = enhancer.enhance(factor_sharp)

        # 2. enhance image contrast given a specific factor
        enhancer_2 = ImageEnhance.Contrast(pim_en)
        factor_contr = 2  # 2.5 the best value for oem -0
        pim_en2 = enhancer.enhance(factor_contr)

        # CV input from PIL and Convert RGB to BGR
        img_pim = np.array(pim_en)
        img_pim = img_pim[:, :, ::-1].copy()

        # img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 3. Convert to Gray
        grimg = cv2.cvtColor(img_pim, cv2.COLOR_BGR2GRAY)

        # 3. thresholding image chose binary thresholding since it gives the best results( analusi kata to grapsimo )
        ret, thr_img = cv2.threshold(grimg, 120, 255, cv2.THRESH_BINARY)

        # 4. resize image x1.5 its original size
        (origW, origH) = pim.size
        big_img = cv2.resize(thr_img, (int(1.5 * origW), int(1.5 * origH)), interpolation=cv2.INTER_LINEAR)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # use pytesseract for OCR
        g = pytesseract.image_to_string(big_img, config=configure, lang="eng")
        # create a list of ocred strings
        gs = g.split()
        # print OCR results for every frame
        print("The frame has this elements: ", ftail, gs)

        # loop through every string parsed from ocr list
        counter_1 += 1
        success_flag = False
        for i, item in enumerate(gs):

            if not success_flag:

                if re.fullmatch(time_pattern, item):

                    # timetag parsing success inform
                    print("This is a match!", item)

                    # replace commas with dots to increase ocr accuracy
                    gs[i] = item.replace(',', '.')

                    # replace time tags when in under a minute to match play by play format
                    if re.fullmatch(under_minute_format, gs[i]):
                        third = gs[i].split('.')[0]
                        gs[i] = "0:" + third

                    # getting frame_id
                    z = re.findall('([0-9]+)', ftail)[0]
                    # creating a list with timetag ocred + frame that was found on
                    timetags.append([gs[i], z])

                    # update if found timetag in specific frame
                    success_flag = True
                    counter_2 += 1

        if not success_flag:
            # creating a list with frames that failed to give a timetag
            failrec.append(ftail)

    # calculating the succes_rate for all frames OCRed
    success_rate = (counter_2 / counter_1) * 100

    # Printing stuff related to ocr success
    print("\nYou found {} out of {} images successfully.".format(counter_2, counter_1))
    print("\n Success rate of:", success_rate, "%")
    print("\n These images failed :", failrec)
    print("\n Timetags exported are: ", timetags)

    return timetags, success_rate


# easyOcr ocr function
def easyOcr_dir(dir_path, time_pat):

    ttags = []
    counter_1 = 0
    counter_2 = 0

    # loop for every frame in the dir
    for filename in sorted(glob.glob(dir_path + '/*.png'),key=numericalSort):

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

def easyOcr_dir2(dir_path):

    ttags = []
    counter_1 = 0
    counter_2 = 0


    # loop for every frame in the dir
    for filename in sorted(glob.glob(dir_path + '/*.png'),key=numericalSort):
        counter_1 += 1
        ftail = ntpath.split(filename)[1]
        print("The frame : ", ftail)
        # get the results
        result = reader.readtext(filename)[1][1]

        if re.fullmatch(filepaths.time_pat2, result):

            if not re.fullmatch(under_minute_format, result):
                result = result.replace('.', ':').replace(',', ':').replace(';', ':')

            print("The frame : " + ftail + " Has this match :" + result)
            # replace commas with dots to increase ocr accuracy
            new_res = result.replace(',', '.')


            # replace time tags when in under a minute to match play by play format
            # dirty fix
            if re.fullmatch(filepaths.under_minute_format, new_res):
                third = new_res.split('.')[0]
                new_res = "0:" + third

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

