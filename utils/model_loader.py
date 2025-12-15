import os 
import sys
from dotenv import load_dotenv


#supporting imports
from utils.config_loader import load_config
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

#langchain imports
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
log = CustomLogger().get_logger(__name__)

class ModelLoader:
    """Class to load language models and embeddings based on configuration."""
    
    def __init__(self):
        load_dotenv()
        self._validate_env_variables()
        self.config = load_config()
        log.info("ModelLoader initialized with configuration.")
    
    def _validate_env_variables(self):
        """
        validate required environment variables are set.
        ensure API keys for OpenAI are available.
        """
        required_vars = ['OPENAI_API_KEY']
        self.api_keys = {key:os.getenv(key) for key in required_vars}
        missing = [k for k, v in self.api_keys.items() if not v]
        if missing:
            log.error(f"Missing required environment variables: {missing}")
            raise DocumentPortalException(f"Missing required environment variables: {missing}", sys)
        log.info("All required environment variables are set.")
        
        
    def load_embeddings(self):
        """load embeddings based on configuration.""" 
        try:
            log.info("Loading embeddings model.")
            embeddings = self.config['embedding_model']['model_name']
            return OpenAIEmbeddings(model=embeddings, openai_api_key=self.api_keys['OPENAI_API_KEY'])
        
        except Exception as e:
            log.error(f"Error Loading Embedding Model: {e}")
            raise DocumentPortalException("Failed ot load embedding model",sys)
        
        
    def load_llm(self):
        """load llm based on configuration."""
        try:
            log.info("Loading language model.")
            llm_config = self.config["llm"]['gpt4o_mini']
            api_key = self.api_keys['OPENAI_API_KEY']
            if api_key is None:
                log.error("OpenAI API key is not set.")
                raise DocumentPortalException("OpenAI API key is not set.", sys)
            model_name = llm_config.get('model_name', 'gpt-4o-mini')
            temperature = llm_config.get('temperature', 0)
            max_tokens = llm_config.get('max_output_tokens', 2048)
            log.info(f"LLM Config - Model: {model_name}, Temperature: {temperature}, Max Tokens: {max_tokens}")        
            llm = ChatOpenAI(
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
                openai_api_key=api_key)
            return llm
        except Exception as e:
            log.error(f"Error loading LLM: {e}")
            raise DocumentPortalException("Failed to load LLM", sys)

if __name__ =="__main__":
    model_loader = ModelLoader()
    llm = model_loader.load_llm()
    embeddings = model_loader.load_embeddings()
    # result = llm.invoke("Hello, world!")
    # print("===================")
    # print(result.content)