from fastapi import FastAPI
from app.api.endpoints import character, user, docs

app = FastAPI(
    title="Characters API",
    description="""
    API documentation to handle Characters in MongoDB

    General objective
    It is required to develop an API that allows you to interact with test data and make GET, POST and DELETE requests.
    
    The API should provide the following functionalities:
    - Registration and Authentication are required to operate the API (This is added as an additional challenge requirement)
    - As an API user I can consult all the saved characters.
    - As an API user I can consult the data of a character searched for by the id field.
    - As an API user I can insert a new character.
    - As an API user I can delete a character searched for by the id field.
    """,
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

