# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# Template matching processing using a scalable template image for a robust application
# latest update 5/4/22

import numpy as np
import math
import imutils
import cv2
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def match_scl(fpath, temp_img, tess_path, vinfile, start_minute, end_minute):

    #start_minute, end_minute = float(28.5) , float(48.5)
    new_flag = False

    if not os.path.exists(fpath) & new_flag:
        print("\nCreating a clipped video of the '%s' match game video" % vinfile[-10: -4])
        ffmpeg_extract_subclip(vinfile, 60 * start_minute, 60 * end_minute, targetname=fpath)

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
    template = cv2.imread(temp_img)  # load the template image
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

                print(found, frameid)

                (startX, startY) = (int(maxLoc[0]), int(maxLoc[1]))
                (endX, endY) = (int(maxLoc[0] + tW), int(maxLoc[1] + tH))

                # draw a bounding box around the detected result and display the image
                # cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)
                # cv2.imshow("Image", img)
                # cv2.waitKey(0)

                # cropping the part we want to ocr
                crop_img = frame[startY:endY, startX:endX]
                new_tem = crop_img
                cv2.imwrite(tess_path + "frame_%d.png" % frameid, crop_img)
                # cv2.imshow("cropped", crop_img)
                # cv2.waitKey(0)

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
