1) aligner = main script calling functions

2) filepaths = Create file paths - initialise each file path/name easy 

3) match_fun = Template matching processing using a scalable template image for a robust application 

4) tess_fun = pytesseract OCR engine used to parse timetags for each frame detected 

5) csv_fun = script for csv file preprocessing adding event_id column and changing column names

6) event_clip =  creating a videoclip of the event the user chose to see

7) easyOcr = easyOcr OCR engine used to parse timetags for each frame detected

8) Obj_Det_AI  = ROI localization using a a pre-trained YOLOV3 model to generate a custom model for the timebox