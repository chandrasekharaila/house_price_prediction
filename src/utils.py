import os
import joblib
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

def save_obj(filepath,obj):
    try:
        dir_name = os.path.dirname(filepath)
        os.makedirs(dir_name,exist_ok=True)
        joblib.dump(obj,filepath)
    except Exception as e:
        raise CustomException(e,sys)

def load_obj(filepath):
    try:
        return joblib.load(filepath)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        logging.info("Started evaluating the models")

        report = {}

        for model_name, model in models.items():
            logging.info(f"started training {model_name}")

            model.fit(X_train,y_train)

            y_pred = model.predict(X_test)

            r2 = r2_score(y_test,y_pred)

            report[model_name] = {
                "model": model,
                "score": r2
            }

            logging.info("fcompleted training {model_name} with score {r2:.4f}")
        logging.info("Completed evaluating all models.")
        return report
    except Exception as e:
        raise CustomException(e,sys) 
        
    
