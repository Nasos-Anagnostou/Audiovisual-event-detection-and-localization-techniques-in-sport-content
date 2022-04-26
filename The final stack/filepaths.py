# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# Create file paths - initialise each file path easy 

def file_paths():
    # working directory root
    root_path = r"C:\Users\Nasoptop\Desktop\Degree Thesis"

    # select the path extracted frames will be saved dimiourgia neou xorou kathe fora?
    tess_path = root_path + r"/Dataset/image processing/cropped_frames_2/"
    csv_path = root_path + r"/Dataset/play by play text/cska_barc.csv"

    # input template and full game video file
    vin_file = root_path + r"/Dataset/game videos/CSKA_BARCA.mp4"
    im_file = root_path + r"/Dataset/template images/eurtime.jpg"

    # trim X minutes from full match video and save it in the chosen dir
    trim_file = "trim_sample1.mp4"
    f_path = root_path + r"/Dataset/game videos/trimmed_videos/" + trim_file

    # chosen event video clip
    clip_1 = root_path + r"/Dataset/game videos/trimmed_videos/clip_1.mp4"

    return tess_path, csv_path, vin_file, im_file, trim_file, clip_1, f_path
