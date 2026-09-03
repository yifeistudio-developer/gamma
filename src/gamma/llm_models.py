from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
import os

load_dotenv()  # Load environment variables from .env file
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_api_base = os.getenv('OPENAI_BASE_URL')
modle_name = os.getenv('OPENAI_MODEL_NAME')

def get_llm():
    return ChatOpenAI(openai_api_key=openai_api_key, 
                      base_url=openai_api_base,
                      model_name=modle_name)

