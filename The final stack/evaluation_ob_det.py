from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="Dataset folder")
trainer.evaluateModel(model_path="Dataset folder/models", json_path="Dataset folder/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
