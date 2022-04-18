# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
#creating a videoclip of the event the user chose to see


import cv2
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def clip_creator(myttag, ttaglist, myfps, fpath, videoclip_1):

    for itime, fid in ttaglist:

        if myttag in itime:

            fr_id = float(fid)
            print("\nFound timestamp: {0} in frame_id: {1}".format(itime, fr_id))

            # Clip creation creating subclip with duration [mysec-4, mysec+2]  #vrisko to sec thelo [mysec-6, mysec+2] h [fr_id -(fps* 6), fr_id +(fps* 2)]
            mysec = fr_id / myfps
            ffmpeg_extract_subclip(fpath, mysec - 4, mysec + 2, targetname=videoclip_1)
            break

    # Play the video clip created
    cap = cv2.VideoCapture(videoclip_1)
    fps = int(cap.get(cv2.CAP_PROP_FPS))   # or cap.get(5)

    if not cap.isOpened():
        print("Error File Not Found")

    # setting playback for video clip created
    while cap.isOpened():
        ret,frame= cap.read()

        if ret:
            time.sleep(1/fps)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()