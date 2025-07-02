import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Check available models
models = genai.list_models()

for model in models:
    print(model.name, " | Supported methods:", model.supported_generation_methods)
