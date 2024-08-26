from fastapi import FastAPI
from frontend.app import frontend_app  
from app.api.endpoints import character, user, docs

# Inicializa la aplicación FastAPI
backend_app = FastAPI(
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

# Montar la aplicación FastHTML en FastAPI
backend_app.mount("/frontend", frontend_app)

backend_app.include_router(user.router, prefix="/user", tags=["user"])
backend_app.include_router(character.router, prefix="/character", tags=["character"])
backend_app.include_router(docs.router, prefix="/docs", tags=["documentation"])

# Este es el objeto de aplicación que Uvicorn debe utilizar
app = backend_app
