from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection.Custom import DetectionModelTrainer
import os


# 1. Train a pre-trained YOLOV3 model with our Data-Set
def train_pretrained_model(dataset_dir):
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory= dataset_dir)
    trainer.setTrainConfig(object_names_array=["Timebox"], batch_size=4, num_experiments=10,
                           train_from_pretrained_model="pretrained-yolov3.h5")
    trainer.trainModel()


# 2. Evaluate the models generated by training
def evaluate_models():
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory="Dataset folder")
    trainer.evaluateModel(model_path="Dataset folder/models", json_path="Dataset folder/json/detection_config.json",
                          iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)


# 3. Detection of object with the best model
def detect_custom_object():
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("hololens-ex-60--loss-2.76.h5")
    detector.setJsonPath("detection_config.json")
    detector.loadModel()
    detections, extracted_images = detector.detectObjectsFromImage(input_image="ela.jpg",
                                                                   output_image_path="ela-detected.jpg",
                                                                   extract_detected_objects=True)
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
