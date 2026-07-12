from src.logger import logging
from src.exception import CustomException
import sys

try:
    a = 10 / 0
except Exception as e:
    logging.error(CustomException(e, sys))