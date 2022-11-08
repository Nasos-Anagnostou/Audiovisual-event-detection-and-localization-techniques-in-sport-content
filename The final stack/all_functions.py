# author: Nasos Anagnostou
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# pytesseract and easyOCR engine used to parse timetags for each frame detected
# latest update 7/11/22

# ALL THE IMPORTS NEEDED
import os
import filepaths
import pytesseract
import easyocr
import cv2
import numpy as np
import pandas as pd
import glob
import re
import ntpath
import time
import math
import imutils
from PIL import Image, ImageEnhance
from pandasgui import show
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from Obj_Det_AI import detect_custom_object

###################################################### PATHS ################################################
fpath = filepaths.f_path  # too many calls need small word

############################################# OCR FUNCTIONS #############################################
# creating method to sort image files in folder based in frame number low to high
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# tesseract ocr function
def tess_dir():

    # tesseract allocation
    pytesseract.pytesseract.tesseract_cmd = r"E:\programs\tessaract\tesseract.exe"
    # tesseract configure
    configure = r'--oem 0 --psm 6'

    # initialise vars
    counter_1 = 0
    counter_2 = 0
    timetags = []
    failrec = []

    # loop for every frame in the dir
    for filename in sorted(glob.glob(filepaths.ocr_path + '/*.png'), key=numericalSort):

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
def easyOcr_dir():

    # EasyOcr Reader initialisation
    reader = easyocr.Reader(['en'], gpu=False)
    ttags = []
    counter_1 = 0
    counter_2 = 0

    # loop for every frame in the dir
    for filename in sorted(glob.glob(filepaths.ocr_path + '/*.png'),key=numericalSort):

        ftail = ntpath.split(filename)[1]

        result = reader.readtext(filename)[1][1]
        print("The frame has this elements: ", ftail, result)

        # dirty fix
        if not re.fullmatch(filepaths.under_minute_format, result):
            result = result.replace('.', ':')

        counter_1 += 1
        if re.fullmatch(filepaths.time_pat, result):
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

############################################# OBJECT DETECTION FUNCTIONS ########################################
# Template matching
def match_scl(start_minute, end_minute):

    # remove the old temp images
    for f in os.listdir(filepaths.ocr_path):
        os.remove(os.path.join(filepaths.ocr_path, f))

    #start_minute, end_minute = float(28.5) , float(48.5)
    new_flag = False

    if not os.path.exists(fpath) & new_flag:
        print("\nCreating a clipped video of the '%s' match game video" % filepaths.vin_file[-10: -4])
        ffmpeg_extract_subclip(filepaths.vin_file, 60 * start_minute, 60 * end_minute, targetname=fpath)

    else:
        print("\nThe file '%s' is already here sir, lets proceed. " % fpath)

    # read first frame from input video
    cap = cv2.VideoCapture(fpath)

    # check if video stream is open
    if not cap.isOpened():
        print("Error opening video  file")

    # get framerate of the video and total frames
    myfps = cap.get(5)
    print("\nFrame rate of this video is: ", myfps)

    # Template image , edw mporw na valw to output tou automation
    template = cv2.imread(filepaths.im_file)  # load the template image
    gray_tem = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  # convert it to grayscale

    # loop through every frame read by input
    founds = []  # bookkeeping variable to keep track of the matched region
    ret = True
    first_time = True
    while ret:

        # read frame id
        frameid = cap.get(1)
        ret, frame = cap.read()
        # print('read a new frame:', ret)

        # obj detect with nn model
        #template_nn = detect_custom_object(frame)
        #template = cv2.imread(template_nn)  # load the template image

        # take 2 frames per every second, one each 500msec
        if ret & ((frameid % math.floor(myfps) == 0) | (frameid % math.floor(myfps) == math.ceil(myfps / 2))):

            # cv2.imwrite(pathOut + 'frame%d.jpg' % frameid, frame)

            # convert frame image to grayscale and then apply canny edge transformation
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image = cv2.Canny(gray, 50, 200)
            (iH, iW) = image.shape[:2]

            found = None
            # The mechanism to identify the scorebox in game -check if this is the first frame we detect the template image
            if first_time:

                # threshold n1 for the first_time
                threshold = 0.5
                for scale in np.linspace(0.4, 1, 20)[::-1]:         #image pyramid psaksou gia documentation

                    # resize the template according to the scale, and keep track of the ratio of the resizing
                    resized = imutils.resize(gray_tem, width=int(template.shape[1] * scale))
                    # if the resized template is bigger than the image, then break from the loop
                    if resized.shape[0] > iH or resized.shape[1] > iW:
                        break

                    # detect edges in the resized, grayscale template
                    # and apply template matching to find the template in the image
                    edged = cv2.Canny(resized, 50, 200)
                    # for full boxscore template use: ccoef normed / timebox use: ccoor normed
                    result = cv2.matchTemplate(image, edged, cv2.TM_CCORR_NORMED)
                    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                    # if we find a new maximum correlation value, then update the bookkeeping variable
                    if found is None or maxVal > found[0]:
                        found = (maxVal, maxLoc)
                        tH, tW = resized.shape[:2]

            else:
                # The generic template matching, repeat the same process as above
                edged = cv2.Canny(new_tem, 50, 200)
                result = cv2.matchTemplate(image, edged, cv2.TM_CCORR_NORMED)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                found = (maxVal, maxLoc)
                tH, tW = new_tem.shape[:2]

            # unpack the bookkeeping variable and compute the (x, y) coordinates of the bounding box based on the resized ratio
            (maxVal, maxLoc) = found
            founds.append(found)

            if maxVal >= threshold:
                # we just found the first mathcing image so we use it as the template from now on!
                first_time = False
                # threshold n2 is higher because we use the boxscore of the same game now
                threshold = 0.75

                (startX, startY) = (int(maxLoc[0]), int(maxLoc[1]))
                (endX, endY) = (int(maxLoc[0] + tW), int(maxLoc[1] + tH))

                # cropping the part we want to ocr
                crop_img = frame[startY:endY, startX:endX]
                new_tem = crop_img
                cv2.imwrite(filepaths.ocr_path + "frame_%d.png" % frameid, crop_img)
                # cv2.imshow("cropped", crop_img)
                # cv2.waitKey(0)
                print(found, frameid)

    # close capture
    cap.release()

    # quality control for max false positive - min true negative detected so we adjust threshold
    yef = []
    nof = []
    for f in founds:
        if (f[1] == (54, 609)) | (f[1] == (61, 608)):
            yef.append([f[0], f[1]])
        else:
            nof.append([f[0], f[1]])

    print("\nQuality Control:")
    try:
        print("Max false", max(nof))
    except:
        print(" No falses detected")
    try:
        print("Min true", min(yef))
    except:
        print(" No true detected")

    return myfps

############################################# CSV EDITING FUNCTIONS #############################################
# csv file editor obsolete since the frontend is developed
def csv_editor (filename):

	# root path of csv files
	mypath = r"E:/Career files/Degree Thesis/2. Dataset/play by play text"

	# read csv file and create dataframe
	df = pd.read_csv(filename) #,index_col ="event_id")
	rows,cols  = df.shape

	#rename columns
	df.columns = ['Quarter', 'Clock time', 'Score', 'Event']

	#Create event_ids and place them as first column
	event_ids = list(range(1,rows+1))
	df.insert(loc=0, column='Event_Id', value=event_ids)
	print(df.columns)

	# display to user the events of play by play text to choose which event to watch
	show(df)

	# ask user to choose which event_id he wants to watch
	myevid = int(input("Give me the event_id you want to watch:"))  # EDW THELEI ENAN ELEGXO TIMIS
	# future use of the quarter for now not in use
	myquart = "2nd Quarter"

	# create a filter for the specific event id, quarter(not used currently)
	filt_1 = (df['Event_Id'] == myevid)
	filt_2 = (df['Quarter'] == myquart)

	# apply filter to get timetag, quarter(not used
	myttag = df.loc[filt_1, 'Clock time']
	myevent = df.loc[filt_2]  # , 'Clock time']

	# convert timetag,quarter to string
	myevent = myevent.to_string(index=False).strip()
	myttag = myttag.to_string(index=False).strip()

	df.to_csv(mypath+"/sample1.csv", index=False)

	return myttag

############################################# VIDEO EDITING FUNCTIONS ############################################
# create the Highlight video clip
def clip_creator(myttag, ttaglist, myfps):

    # videolcip init
    videoclip = 0
    # flag to check if the video created
    vflag = False
    for itime, fid in ttaglist:

        if myttag in itime:
            fr_id = float(fid)
            print("\nFound timestamp: {0} in frame_id: {1}".format(itime, fr_id))

            # Clip creation creating subclip with duration [mysec-4, mysec+2]  #vrisko to sec thelo [mysec-6, mysec+2] h [fr_id -(fps* 6), fr_id +(fps* 2)]
            mysec = fr_id / myfps
            ffmpeg_extract_subclip(fpath, mysec - 5, mysec + 1, targetname=filepaths.clip_1)
            videoclip = filepaths.clip_1
            vflag = True
            break

        if os.path.exists(filepaths.clip_1):
            os.remove(filepaths.clip_1)
            print("Deleting the old file")
        else:
            continue

    # # Play the video clip created
    # cap = cv2.VideoCapture(videoclip_1)
    # fps = int(cap.get(cv2.CAP_PROP_FPS))   # or cap.get(5)
    #
    # if not cap.isOpened():
    #     print("Error File Not Found")
    #
    # # setting playback for video clip created
    # while cap.isOpened():
    #     ret,frame= cap.read()
    #
    #     if ret:
    #         time.sleep(1/fps)
    #         cv2.imshow('frame', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     else:
    #         break
    #
    # # close capture
    # cap.release()
    # cv2.destroyAllWindows()
    return vflag, videoclip