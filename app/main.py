from fastapi import FastAPI
from app.api.endpoints import character, user, docs, language_detection, eye_color
from app.services.eye_color_initializer import initialize_eye_colors
from dotenv import load_dotenv
import os


load_dotenv()  # Esto cargará las variables de entorno desde el archivo .env

# Inicializa la aplicación FastAPI
app = FastAPI(
    title="Characters API",
    description="API documentation to handle Characters in MongoDB",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "character",
            "description": "Operations with characters"
        },
        {
            "name": "user",
            "description": "Operations with users"
        },
        {
            "name": "documentation",
            "description": "API documentation"
        }
    ]
)

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(character.router, prefix="/character", tags=["character"])
app.include_router(docs.router, prefix="/docs", tags=["documentation"])
app.include_router(language_detection.router, tags=["language detection"])
app.include_router(eye_color.router, tags=["eye colors"])

