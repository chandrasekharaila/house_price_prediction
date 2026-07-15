from src.logger import logging
from src.exception import CustomException
from src.utils import load_obj
import sys
import os
import pandas as pd

class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts","model.pkl")
        self.preprocessor_path = os.path.join("artifacts","preprocessor.pkl")

    def predict(self,features):
        try:
            logging.info("started prediction pipeline")
            logging.info("loading preprocessor")
            preprocessor = load_obj(self.preprocessor_path)
            logging.info("loading model")
            model = load_obj(self.model_path)
            logging.info("transformed features")
            transformed_features = preprocessor.transform(features)
            logging.info("making prediction")
            prediction = model.predict(transformed_features)
            logging.info("prediction completed successfully")
            return prediction
            
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:

    def __init__(
        self,
        area: float,
        bedrooms: int,
        bathrooms: int,
        stories: int,
        parking: int,
        mainroad: str,
        guestroom: str,
        basement: str,
        hotwaterheating: str,
        airconditioning: str,
        prefarea: str,
        furnishingstatus: str
    ):

        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.stories = stories
        self.parking = parking

        self.mainroad = mainroad
        self.guestroom = guestroom
        self.basement = basement
        self.hotwaterheating = hotwaterheating
        self.airconditioning = airconditioning
        self.prefarea = prefarea
        self.furnishingstatus = furnishingstatus

    def get_data_as_dataframe(self):

        try:

            data = {
                "area": [self.area],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "stories": [self.stories],
                "parking": [self.parking],
                "mainroad": [self.mainroad],
                "guestroom": [self.guestroom],
                "basement": [self.basement],
                "hotwaterheating": [self.hotwaterheating],
                "airconditioning": [self.airconditioning],
                "prefarea": [self.prefarea],
                "furnishingstatus": [self.furnishingstatus],
            }

            df = pd.DataFrame(data)

            logging.info("Created prediction DataFrame.")

            return df

        except Exception as e:
            raise CustomException(e, sys)