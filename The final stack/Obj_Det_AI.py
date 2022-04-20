from imageai.Detection import ObjectDetection
import os
from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="Dataset folder")
trainer.setTrainConfig(object_names_array=["Timebox"], batch_size=4, num_experiments=10, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()


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