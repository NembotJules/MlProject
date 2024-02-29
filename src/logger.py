"""
Logger is for the purpose that any execution that probably happen we should be able to log all those 
informations, executions into some files so that we should be able to track errors.
    
"""

import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
) 


if __name__ == "__main__": 
    logging.info("Logging has started")
