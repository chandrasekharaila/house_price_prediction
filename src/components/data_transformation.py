from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.utils import save_obj
from src.exception import CustomException
import pandas as pd
import numpy as np
import os
import sys

@dataclass(frozen=True)
class DataTransformationConfig:
    preprocessor_path: str = os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_preprocessor_object(self) -> ColumnTransformer:

        logging.info("started creating preprocessor object")
        numerical_transformer = Pipeline(
            steps=[
                ("numerical_imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
            ]
        )

        categorical_transformer = Pipeline(
            steps=[
                ("categorical_imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore"))
            ]
        )

        num_cols = ["area","bedrooms","bathrooms","stories","parking"]
        cat_cols = ["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]

        preprocessor = ColumnTransformer(
            transformers=[
                ("numerical_preprocessor", numerical_transformer, num_cols),
                ("catgorical_preprocessor", categorical_transformer, cat_cols)
            ]
        )

        logging.info("completed creating preprocessor object")

        return preprocessor
    

    def initiate_data_transformation(self, train_data_path:str, test_data_path:str):
        try:
            logging.info("Started data transformation")
            train_data = pd.read_csv(train_data_path)
            logging.info("Loaded train data")
            test_data = pd.read_csv(test_data_path)
            logging.info("Loaded test data")

            train_x = train_data.drop("price",axis=1)
            train_y = train_data["price"]
            logging.info("X and y split done for train data")

            test_x = test_data.drop("price",axis=1)
            test_y = test_data["price"]
            logging.info("X and y split done for test data")

            preprocessor = self.get_data_preprocessor_object()

            transformed_train_X = preprocessor.fit_transform(train_x)
            transformed_test_X = preprocessor.transform(test_x)
            logging.info("data transformation done")

            save_obj(self.data_transformation_config.preprocessor_path,preprocessor)
            logging.info("saved the preprocessor")

            train_arr = np.c_[transformed_train_X,train_y]
            test_arr = np.c_[transformed_test_X,test_y]

            return (train_arr,test_arr,self.data_transformation_config.preprocessor_path)
        except Exception as e:
            raise CustomException(e,sys)


        