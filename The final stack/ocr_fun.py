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
def tess_dir2(ocr_path):
    # tesseract allocation
    pytesseract.pytesseract.tesseract_cmd = r"E:\programs\tessaract\tesseract.exe"
    # tesseract configure
    configure = r'--oem 0 --psm 6'

    # initialise vars
    counter_1 = 0
    counter_2 = 0
    timetags = []
    alltimetags = []
    failrec = []

    # loop for every frame in the dir
    for filename in sorted(glob.glob(ocr_path + '/*.png'), key=numericalSort):

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

                if re.fullmatch(filepaths.time_pat, item):

                    # timetag parsing success inform
                    print("This is a match!", item)

                    # replace commas with dots to increase ocr accuracy
                    gs[i] = item.replace(',', '.')

                    # replace time tags when in under a minute to match play by play format
                    if re.fullmatch(filepaths.under_minute_format, gs[i]):
                        third = gs[i].split('.')[0]

                        if len(third) == 2:
                            gs[i] = "0:" + third
                        else:
                            gs[i] = "0:0" + third

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
def easyOcr_dir3(ocr_path):

    alltimetags = []
    ttags = []
    failrec = []
    counter_1 = 0
    counter_2 = 0

    # loop for every frame in the dir
    for filename in sorted(glob.glob(ocr_path + '/*.png'), key=numericalSort):
        counter_1 += 1
        ftail = ntpath.split(filename)[1]
        # get the results

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        im_cv2 = cv2.imread(filename)
        pim = Image.fromarray(im_cv2)

        # 1. enhance image sharpness given a specific factor
        enhancer = ImageEnhance.Sharpness(pim)
        factor_sharp = 2
        pim_en = enhancer.enhance(factor_sharp)
        # CV input from PIL and Convert RGB to BGR
        img_pim = np.array(pim_en)
        img_pim = img_pim[:, :, ::-1].copy()

        # 3. Convert to Gray
        grimg = cv2.cvtColor(img_pim, cv2.COLOR_BGR2GRAY)

        # 3. thresholding image chose binary thresholding since it gives the best results( analusi kata to grapsimo )
        ret, thr_img = cv2.threshold(grimg, 120, 255, cv2.THRESH_BINARY)

        # 4. resize image x1.5 its original size
        (origW, origH) = pim.size
        big_img = cv2.resize(thr_img, (int(1.5 * origW), int(1.5 * origH)), interpolation=cv2.INTER_LINEAR)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # read the ocr items and check if the list is empty
        result = reader.readtext(big_img)
        if not result:
            continue

        quarter = result[0][1]
        result = result[1][1]
        alltimetags.append([result, quarter, ftail])
        print("The frame has these elements: ", ftail, result, quarter)

        if re.fullmatch(filepaths.time_pat2, result):

            if re.fullmatch('(\S*((1)|(1s|S|5))\S*)', quarter):
                quarter = "1st Quarter"

            elif re.fullmatch('(\S*(2|Z)\S*)|(\S*(ND)\S*)', quarter):
                quarter = "2nd Quarter"

            elif re.fullmatch('(\S*((J|J|3)|(RD|rd))\S*)', quarter):
                quarter = "3rd Quarter"

            elif re.fullmatch('(\S*((4TH|4|TH)|(AT|At))\S*)', quarter):
                quarter = "4th Quarter"

            # replace commas with dots to increase ocr accuracy
            result = result.replace(',', '.')

            # dirty fix
            if not re.fullmatch(filepaths.under_minute_format, result):
                result = result.replace('.', ':').replace(';', ':')

            else:
                # replace time tags when in under a minute to match play by play format
                third = result.split('.')[0]
                if len(third) == 2:
                    result = "0:" + third
                else:
                    result = "0:0" + third

            print("Its a match: ", result, quarter)
            # getting frame_id
            z = re.findall('([0-9]+)', ftail)[0]
            # creating a list with timetag ocred + frame that was found on
            ttags.append([result, quarter, z])
            counter_2 += 1

        else:
            failrec.append(ftail)

    # calculating the success_rate for all frames OCRed
    success_rate = (counter_2 / counter_1) * 100

    # Printing stuff related to ocr success
    print("\n These images failed :", failrec)
    print("\n Timetags exported are: ", ttags)
    print("\n You found {} out of {} images successfully.".format(counter_2, counter_1))
    print("\n Success rate of:", success_rate, "%")

    return ttags, alltimetags

def easyOcr_dir2(ocr_path):

    ttags = []
    failrec = []
    counter_1 = 0
    counter_2 = 0

    # loop for every frame in the dir
    for filename in sorted(glob.glob(ocr_path + '/*.png'), key=numericalSort):
        counter_1 += 1
        ftail = ntpath.split(filename)[1]
        # get the results

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        im_cv2 = cv2.imread(filename)
        pim = Image.fromarray(im_cv2)

        # 1. enhance image sharpness given a specific factor
        enhancer = ImageEnhance.Sharpness(pim)
        factor_sharp = 2
        pim_en = enhancer.enhance(factor_sharp)
        # CV input from PIL and Convert RGB to BGR
        img_pim = np.array(pim_en)
        img_pim = img_pim[:, :, ::-1].copy()

        # 3. Convert to Gray
        grimg = cv2.cvtColor(img_pim, cv2.COLOR_BGR2GRAY)

        # 3. thresholding image chose binary thresholding since it gives the best results( analusi kata to grapsimo )
        ret, thr_img = cv2.threshold(grimg, 120, 255, cv2.THRESH_BINARY)
        cv2.imshow("",thr_img)
        cv2.waitKey(0)
        # 4. resize image x1.5 its original size
        (origW, origH) = pim.size
        big_img = cv2.resize(thr_img, (int(1.3 * origW), int(1.3 * origH)), interpolation=cv2.INTER_LINEAR)
        cv2.imshow("", big_img)
        cv2.waitKey(0)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ALL THIS IS THE PREPROCESSING PIPELINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # read the ocr items and check if the list is empty
        result = reader.readtext(big_img)
        if not result:
            continue

        quarter = result[0][1]
        result = result[1][1]
        print("The frame has these elements: ", ftail, result, quarter)

        if re.fullmatch(filepaths.time_pat, result):

            if re.fullmatch('(\S*((1)|(1s|S|5))\S*)', quarter):
                quarter = "1st Quarter"

            elif re.fullmatch('(\S*(2|Z)\S*)|(\S*(ND)\S*)', quarter):
                quarter = "2nd Quarter"

            elif re.fullmatch('(\S*((J|J|3)|(RD|rd))\S*)', quarter):
                quarter = "3rd Quarter"

            elif re.fullmatch('(\S*((4TH|4|TH)|(AT|At))\S*)', quarter):
                quarter = "4th Quarter"

            # replace commas with dots to increase ocr accuracy
            result = result.replace(',', '.')

            # dirty fix
            if not re.fullmatch(filepaths.under_minute_format, result):
                result = result.replace('.', ':').replace(';', ':')

            else:
                # replace time tags when in under a minute to match play by play format
                third = result.split('.')[0]
                if len(third) == 2:
                    result = "0:" + third
                else:
                    result = "0:0" + third

            print("Its a match: ", result, quarter)
            # getting frame_id
            z = re.findall('([0-9]+)', ftail)[0]
            # creating a list with timetag ocred + frame that was found on
            ttags.append([result, quarter, z])
            counter_2 += 1

        else:
            failrec.append(ftail)

    # calculating the success_rate for all frames OCRed
    success_rate = (counter_2 / counter_1) * 100

    # Printing stuff related to ocr success
    print("\n These images failed :", failrec)
    print("\n Timetags exported are: ", ttags)
    print("\n You found {} out of {} images successfully.".format(counter_2, counter_1))
    print("\n Success rate of:", success_rate, "%")

    return ttags, success_rate

