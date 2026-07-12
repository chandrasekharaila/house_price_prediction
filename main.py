from src.utils import save_obj, load_obj
import os
from src.logger import logging
from src.exception import CustomException
import sys

artifacts_folder = os.path.join(os.getcwd(),"artifacts")
os.makedirs(artifacts_folder,exist_ok=True)

sample_obj = "model: xgboost"

# try:
#     filepath = os.path.join(artifacts_folder,"sample_file.pkl")
#     save_obj(filepath,sample_obj)
#     logging.info("obj saved successfully")
# except Exception as e:
#     logging.info("failed to save obj")
#     logging.error(CustomException(e,sys))


try:
    filepath = os.path.join(artifacts_folder,"sample_file.pkl")
    obj1 = load_obj(filepath)
except Exception as e:
    logging.info("failed to load obj")
    logging.error(CustomException(e,sys))
