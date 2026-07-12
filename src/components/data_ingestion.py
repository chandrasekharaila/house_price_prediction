from dataclasses import dataclass
from src.logger import logging
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import os
import sys
import pandas as pd

@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw1.csv")
    train_data_path: str = os.path.join("artifacts","train1.csv")
    test_data_path: str = os.path.join("artifacts","test1.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self, datasetpath: str):
        try:
            logging.info("data ingestion started")
            df = pd.read_csv(datasetpath)
            logging.info("dataset loaded")
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("raw dataset saved")

            train_data, test_data = train_test_split(df,test_size=0.2,random_state=42)
            logging.info("train test split is done")
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info("train csv saved")
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("test csv saved")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)






