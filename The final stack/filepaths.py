# author: Nasos Anagnostou
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# Create file paths - initialise each file path easy
# ocr needed time pattern and under minute format
time_pat = '((1[012]|0[0-9]|[0-9]):([0-9][0-9]))|(([1-5][0-9]|[0-9])(\.|\,)[0-9])'
under_minute_format = '(([1-5][0-9]|[0-9])\.[0-9])'
# working directory root
root_path = r"E:\Career files\Degree Thesis"  # move to aligner
# select the path extracted frames will be saved
ocr_path = root_path + r"/2. Dataset/Images Dataset/cropped_frames_2/"  # dimiourgia neou xorou kathe fora? - move to aligner
roi_path = root_path + r"/2. Dataset/Object_Det_files/"  # move to aligner
csv_path = root_path + r"/2. Dataset/play by play text/cska_barc.csv"  # USER INPUT
# input template and full game video file
vin_file = root_path + r"/2. Dataset/game videos/CSKA_BARCA.mp4"  # USER INPUT
im_file = root_path + r"/2. Dataset/template images/eurtime.jpg"  # USER INPUT
# trim X minutes from full match video and save it in the chosen dir
trim_file = "trim_sample1.mp4"  # move to aligner
f_path = root_path + r"/2. Dataset/game videos/trimmed_videos/" + trim_file  # move to aligner
# chosen event video clip
clip_1 = root_path + r"/2. Dataset/game videos/trimmed_videos/clip_1.mp4"  # move to clip_creator
##check
