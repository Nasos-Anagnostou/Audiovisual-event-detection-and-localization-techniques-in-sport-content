from imageai.Detection.Custom import DetectionModelTrainer
from imageai.Detection.Custom import CustomObjectDetection

# # 1. Evaluation models
# trainer = DetectionModelTrainer()
# trainer.setModelTypeAsYOLOv3()
# trainer.setDataDirectory(data_directory="Dataset folder")
# trainer.evaluateModel(model_path="Dataset folder/models", json_path="Dataset folder/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)


# 2. Detection
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("Dataset folder/models\detection_model-ex-005--loss-0021.688.h5")
detector.setJsonPath("Dataset folder/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="ela.jpg", output_image_path="ela-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
