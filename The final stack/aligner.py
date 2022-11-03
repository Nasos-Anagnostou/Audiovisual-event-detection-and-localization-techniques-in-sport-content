# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# main script calling functions
# latest update 2/11/22
import csv
import timeit
import filepaths
from csv_fun import csv_editor
from all_functions import match_scl, tess_dir, easyOcr_dir, clip_creator

#from pages import Game_Highlights


################################################################################################
# start the timer
start_time = timeit.default_timer()

# 1. initialise file paths with filepaths()
#ocr_path, roi_path, csv_path, vinfile, imfile, trimfile, videoclip_1, fpath = file_paths()

# 2. get the matching frames with temp img with match_scl()
#myfps = match_scl(filepaths.f_path, filepaths.im_file, filepaths.ocr_path, filepaths.vin_file, 33.5, 34.5)

# 3. ocr the frames matching temp with  dir_tess()

# time pattern we want to recognise from scorebox
time_pat = '((1[012]|0[0-9]|[0-9]):([0-9][0-9]))|(([1-5][0-9]|[0-9])(\.|\,)[0-9])'   # maybe use a whitelist?

# tesseract configuration, see tesseract documentation for more
#conf = r'--oem 0 --psm 6'
# Tesseract
#ttags, succ_r = tess_dir(filepaths.ocr_path, time_pat, conf)

#easyOcr
ttags, succ_r = easyOcr_dir(filepaths.ocr_path, time_pat)    # na ta kanw save kapou ta ttags

# store ttags list for frontend
with open("out.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(ttags)

# 4. Show user the events to choose what event wants to see by selecting event_id, using csv_trial()
#myttag = csv_editor(filepaths.csv_path)

# 5. match event_id timetag with ocr timetag and get the specific frame_id to create videoclip
#clip_creator(myttag, ttags, myfps, filepaths.f_path, filepaths.clip_1)

# stop the timer print time of execution
print("\nThe time difference is :", timeit.default_timer() - start_time)

################################################################################################

