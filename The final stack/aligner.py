# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# main script calling functions
# latest update 2/11/22

import os
import csv
import timeit
import filepaths
from ocr_fun import easyOcr_dir2, tess_dir2, easyOcr_dir3
from csv_fun import csv_editor
from all_functions import match_scl, tess_dir, easyOcr_dir, clip_creator, template_finder


################################################################################################

# 1. template finder with deep learning
#template_finder(filepaths.template_root, filepaths.trim_vid_eu3)


# 2. get the matching frames with temp img with match_scl()
#myfps = match_scl(filepaths.oly_pao_vid, filepaths.ocr_eu2, filepaths.tmp_eu, 'start', 'end')
# # store fps for later use
# with open(os.path.join(filepaths.timetags, 'nasos.txt'), "w") as wfile:
#     wfile.write(str(myfps))


# 3. ocr the frames matching temp with  dir_tess()
# tesseract configuration, see tesseract documentation for more
#conf = r'--oem 0 --psm 6'
# Tesseract
#ttags, succ_r = tess_dir2(filepaths.ocr_nba1)

#easyOcr3 gia ta wer
ttags, alltags = easyOcr_dir(filepaths.ocr_eu4)    # TA TTAGS GIA KATHE MATCH ALLO FAKELO
# store ttags list for frontend
with open(os.path.join(filepaths.timetags, "ref.csv"), "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(ttags)
with open(os.path.join(filepaths.timetags, "ttags.csv"), "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(alltags)

################################################### TEST ########################################################
#myfps = match_scl(filepaths.cska_bayern_vid, filepaths.ocr_eu2, filepaths.tmp_eu, 0, 99)
#myfps2 = match_scl(filepaths.oly_pao_vid, filepaths.ocr_eu3, filepaths.tmp_eu, 0, 101.5)
# start the timer
# start_time = timeit.default_timer()
#
# ttags, succ_r = easyOcr_dir(filepaths.ocr_eu1)
# # store ttags list for frontend
# with open(os.path.join(filepaths.timetags, "eur1.csv"), "w", newline='') as f:
#     wr = csv.writer(f)
#     wr.writerows(ttags)
#
# # stop the timer print time of execution
# print("\nThe time difference1 is :", timeit.default_timer() - start_time)

# start the timer
#start_time = timeit.default_timer()

#ttags, succ_r = easyOcr_dir(filepaths.ocr_eu1)
# store ttags list for frontend
# with open(os.path.join(filepaths.timetags, "eur2.csv"), "w", newline='') as f:
#     wr = csv.writer(f)
#     wr.writerows(ttags)

# stop the timer print time of execution
#print("\nThe time difference2 is :", timeit.default_timer() - start_time)
#
# # start the timer
# start_time = timeit.default_timer()
#
# ttags, succ_r = easyOcr_dir(filepaths.ocr_eu3)
# # store ttags list for frontend
# with open(os.path.join(filepaths.timetags, "eur3.csv"), "w", newline='') as f:
#     wr = csv.writer(f)
#     wr.writerows(ttags)
#
# # stop the timer print time of execution
# print("\nThe time difference3 is :", timeit.default_timer() - start_time)
################################################### TEST ########################################################


# 4. Show user the events to choose what event wants to see by selecting event_id, using csv_trial()
#myttag = csv_editor(filepaths.csv_path)

# 5. match event_id timetag with ocr timetag and get the specific frame_id to create videoclip
#clip_creator(myttag, ttags, myfps, filepaths.f_path, filepaths.clip_1)


################################################################################################

