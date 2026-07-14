from dataclasses import dataclass
import os
import numpy as np
from numpy.typing import NDArray
from src.utils import save_obj
from src.logger import logging
from src.exception import CustomException
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_models
import sys


@dataclass(frozen=True)
class ModelTrainerConfig:
    model_path: str = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_arr: NDArray, test_arr:NDArray):
        try:
            logging.info("started training the model")
            X_train = train_arr[:,:-1]
            y_train = train_arr[:,-1]
            X_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]
            logging.info("features and target split done")
            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(random_state = 42),
                "Random Forest": RandomForestRegressor(random_state = 42),
                "Gradient Boost": GradientBoostingRegressor(random_state = 42),
                "Xgboost": XGBRegressor(random_state = 42)
            }

            report = evaluate_models(X_train,y_train,X_test,y_test,models)

            logging.info("Model Performance")
            for model,result in report.items():
                logging.info(f"model-{model}: score-{result['score']:.4f}")

            best_model_name = max(report, key= lambda model_name: report[model_name]["score"])
            best_model = report[best_model_name]["model"]
            best_model_score = report[best_model_name]["score"]

            logging.info(f"best model - {best_model_name}, best model score - {best_model_score}")

            save_obj(self.model_trainer_config.model_path,best_model)

            
            return {
                "best_model_name": best_model_name,
                "best_model": best_model,
                "r2_score": best_model_score
            }

            
        except Exception as e:
            raise CustomException(e,sys)
