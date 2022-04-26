from imageai.Detection import ObjectDetection
import os
# execution_path = os.getcwd()
#
# detector = ObjectDetection()
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
# detector.loadModel()
# detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "ela.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"),extract_detected_objects=True)    # add this to get the image ,extract_detected_objects=True
#
#
# for eachObject in detections:
#     print(eachObject["name"] , " : " , eachObject["percentage_probability"] )