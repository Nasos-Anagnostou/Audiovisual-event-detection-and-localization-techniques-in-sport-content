# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# main script calling functions
# latest update 18/6/21


from tess_fun import tess_dir
from csv_fun import csv_editor
from match_fun import match_scl
from filepaths import file_paths
from event_clip import clip_creator

import timeit
import pandas as pd
from pandasgui import show



#################################################################################################
# start the timer
start_time = timeit.default_timer()


# 1. initialise file paths with filepaths()
tess_path, csv_path, vinfile, imfile, trimfile, videoclip_1, fpath = file_paths()


# 2. get the matching frames with temp img with match_scl()
myfps = match_scl(fpath, imfile, tess_path, vinfile, 33.5, 34.5)


# 3. ocr the frames mathcing temp with  dir_tess()

# time pattern we want to recognise from scorebox
time_pat = '((1[012]|0[0-9]|[0-9]):([0-9][0-9]))|(([1-5][0-9]|[0-9])(\.|\,)[0-9])'   # maybe use a whitelist?
# tesseract configuration, see tess documentation for more 
conf = r'--oem 0 --psm 6'

ttags, succ_r, fldim  = tess_dir(tess_path, time_pat, conf)


# 4. Show user the events to choose what event wants to see by selecting sevent_id, using csv_trial()
myttag = csv_editor(csv_path)


# 5. match event_id timetag with ocr timetag and get the specific frame_id to create videoclip
# create the clip of the event user wants to see
clip_creator(myttag, ttags, myfps, fpath, videoclip_1)


# stop the timer print time of execution 
print("\nThe time difference is :", timeit.default_timer() - start_time)

################################################################################################


