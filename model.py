from langchain_ollama import OllamaLLM
from config import OLLAMA_MODEL_NAME

model = OllamaLLM(model=OLLAMA_MODEL_NAME)
