import os
import joblib
import sys
from src.exception import CustomException

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