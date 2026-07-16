from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging
import sys


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self,dataset_path):
        try:
            logging.info("training pipeline started")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion(dataset_path)
            logging.info("data ingestion completed")
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_path,test_path)
            logging.info("data transformation completed")
            model_trainer = ModelTrainer()
            final_model_report = model_trainer.initiate_model_training(train_arr,test_arr)
            logging.info("model training completed")
            logging.info("training pipeline completed")
            return final_model_report
        except Exception as e:
            raise CustomException(e,sys)


