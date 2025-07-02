from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load the API key from .env
load_dotenv()
genai_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=genai_api_key)

# Initialize the model
model = genai.GenerativeModel('models/gemini-2.5-pro')


# Initialize FastAPI
app = FastAPI()

# Allow CORS (connect frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class ChatRequest(BaseModel):
    message: str

# Endpoint for chatbot
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = model.generate_content(req.message)
        reply = response.text
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
