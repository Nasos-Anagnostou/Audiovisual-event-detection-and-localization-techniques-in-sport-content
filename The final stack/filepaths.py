# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# Create file paths - initialise each file path easy 

def file_paths():
    # working directory root
    root_path = r"E:\Career files\Degree Thesis"

    # select the path extracted frames will be saved dimiourgia neou xorou kathe fora?
    ocr_path = root_path + r"/2. Dataset/Images Dataset/cropped_frames_2/"

    roi_path = root_path + r"/2. Dataset/Object_Det_files/"
    csv_path = root_path + r"/2. Dataset/play by play text/cska_barc.csv"

    # input template and full game video file
    vin_file = root_path + r"/2. Dataset/game videos/CSKA_BARCA.mp4"
    im_file = root_path + r"/2. Dataset/template images/eurtime.jpg"

    # trim X minutes from full match video and save it in the chosen dir
    trim_file = "trim_sample1.mp4"
    f_path = root_path + r"/2. Dataset/game videos/trimmed_videos/" + trim_file

    # chosen event video clip
    clip_1 = root_path + r"/2. Dataset/game videos/trimmed_videos/clip_1.mp4"

    return ocr_path, roi_path, csv_path, vin_file, im_file, trim_file, clip_1, f_path
