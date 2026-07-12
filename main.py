from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException

try:
    ingestion = DataIngestion()

    train_path, test_path = ingestion.initiate_data_ingestion(
        "notebook/housing.csv"
    )

    print(train_path)
    print(test_path)

except CustomException as e:
    logging.error(e)