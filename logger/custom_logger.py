import logging 
import os 
from datetime import datetime


class CustomLogger:
    
    def __init__(self):
        
        #create logging directory
        logger_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(logger_dir,"logs")
        os.makedirs(log_dir,exist_ok=True)
        
        #create log file name that is date and time stamped
        log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log" 
        log_file_path = os.path.join(log_dir,log_file)
        
        #logging configuration 
        logging.basicConfig(
            filename=log_file_path,
            format = "[%(asctime)s] %(levelname)s %(name)s (line:%(lineno)d) %(message)s",
            level=logging.INFO,
        )
        
    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("logger initialized")