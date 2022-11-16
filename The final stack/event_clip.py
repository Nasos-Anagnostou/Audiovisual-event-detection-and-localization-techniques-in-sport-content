# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
#creating a videoclip of the event the user chose to see

import os
import filepaths
import cv2
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def clip_creator(trim_vid, myttag, ttaglist, myfps):
    if os.path.exists(filepaths.clip_1):
        os.remove(filepaths.clip_1)
        print("Deleting the old file")

    # videolcip init
    videoclip = 0
    # flag to check if the video created
    vflag = False
    for item in ttaglist:

        if myttag[0] in item[0] and myttag[1] in item[1]:
            fr_id = float(item[2])
            print("\nFound timestamp: {0} in frame_id: {1}".format(item[0], fr_id))

            # Clip creation creating subclip with duration [mysec-4, mysec+2]  #vrisko to sec thelo [mysec-6, mysec+2] h [fr_id -(fps* 6), fr_id +(fps* 2)]
            mysec = fr_id / myfps
            ffmpeg_extract_subclip(trim_vid, mysec - 4, mysec + 1, targetname=filepaths.clip_1)
            videoclip = filepaths.clip_1
            vflag = True
            break

        elif myttag[0] in item[0] and myttag[1] not in item[2]:
            print("\nWe dont have the quarter")



    return vflag, videoclip
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