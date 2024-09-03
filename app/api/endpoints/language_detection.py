from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/lng_detect/chatgpt/")
async def chatgpt_response(request: TextRequest):
    # Configuración de la API
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    
    if not api_key or not endpoint:
        raise HTTPException(status_code=500, detail="API key or endpoint not set in environment variables")

    endpoint += "/openai/deployments/ChatNelsonChallengeV5/chat/completions?api-version=2024-02-15-preview"

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }

    # Payload para la solicitud
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are an AI assistant that helps people find information."
            },
            {
                "role": "user",
                "content": request.text
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    # Enviar solicitud
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Levantará una excepción si hay un error HTTP
        response_data = response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to make the request. Error: {e}")

    # Extraer y devolver solo el "content" del mensaje
    try:
        message_content = response_data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=500, detail="Unexpected response format from OpenAI")

    return {"message_content": message_content}
