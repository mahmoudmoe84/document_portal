import os 
from dotenv import load_dotenv

#supporting imports
from utils.config_loader import load_config
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

#langchain imports
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

logger = CustomLogger().get_logger(__name__)

class ModelLoader:
    
    def __init__(self):
        pass
    
    def _validate_env_variables(self):
        pass
    
    def load_embeddings(self):
        pass 
    
    def load_llm(self):
        pass