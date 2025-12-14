import sys 
import traceback 
import os 

#adding parent directory to sys.path for imports
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_directory not in sys.path:
    sys.path.insert(0,parent_directory)

from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger(__file__)

class DocumentPortalException(Exception):
    """custom exception for document portal"""
    
    def __init__(self,error_message:str,error_details:sys):
       _,_,exe_tb = error_details.exc_info()
       self.file_name =exe_tb.tb_frame.f_code.co_filename
       self.line_number = exe_tb.tb_lineno
       self.error_message = str(error_message)
       self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))
    
    
    def __str__(self):
        return f"""
            Error in [{self.file_name}] at line number [{self.line_number}]
            Message : {self.error_message}
            Traceback : 
            {self.traceback_str}
        """
         

if __name__ == "__main__":
    try:
        a = 1/0
        print(a)
    except Exception as e:
        app_exc = DocumentPortalException(e,sys)
        logger.error(app_exc)
        raise app_exc