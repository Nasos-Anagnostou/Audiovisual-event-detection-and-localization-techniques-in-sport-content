







myfps = match_scl(filepaths.trim_vid_eu1, filepaths.cska_barc_vid, filepaths.ocr_eu1, filepaths.tmp_eu, 33.5,
                  34.5)  # NA DINW THN TEMP IMAGE EDW
with open("video_fps.txt", "w") as file:
    file.write(str(myfps))

# ocr the frames matching temp with easyOcr
ttags, succ_r = easyOcr_dir(
    filepaths.ocr_eu1)  # na ta kanw save kapou ta ttags         # TA TTAGS GIA KATHE MATCH ALLO FAKELO
with open(os.path.join(filepaths.timetags, "eur1.csv"), "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(ttags)