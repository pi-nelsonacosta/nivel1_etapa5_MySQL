from fastapi import APIRouter, HTTPException, Depends, Path, status
from fastapi.responses import JSONResponse
from app.models.character import CharacterAddResponseModel, CharacterModel, CharacterResponseModel
from app.services.character import CharacterService
from app.services.auth import get_current_active_user
from app.models.user import User

router = APIRouter()

@router.get("/getAll", response_model=list[CharacterResponseModel], 
    summary="Get all characters", 
    description="Retrieve all characters from the database",
    responses={
        200: {"description": "Successful retrieval of all characters or empty list"},
        401: {"description": "Unauthorized User"}
    })
async def get_all_characters(current_user: User = Depends(get_current_active_user)):
    """
    This endpoint retrieves all characters from the database.

    - **current_user**: The current logged-in user
    """
    return await CharacterService.get_all_characters()

@router.get("/get/{id}", response_model=CharacterResponseModel, 
    summary="Get character by ID", 
    description="Retrieve a character by its ID",
    responses={
        200: {"description": "Successful retrieval of the character"},
        400: {"description": "Bad request: ID cannot be empty"},
        401: {"description": "Unauthorized User"},
        404: {"description": "Character not found"}
    })
async def retrieve_character(id: str = Path(..., description="The ID of the character to retrieve", min_length=1),
                                current_user: User = Depends(get_current_active_user)):
    """
    This endpoint retrieves a character by its ID.

    - **id**: The ID of the character to retrieve
    - **current_user**: The current logged-in user
    """
    if len(id.strip()) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID cannot be empty")

    character = await CharacterService.get_character_by_id(id)
    if character is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    return character

@router.post("/add", response_model=CharacterAddResponseModel, 
    summary="Add a new character", 
    description="Add a new character to the database",
    responses={
        201: {"description": "Character successfully added"},
        400: {"description": "Character already exists"},
        401: {"description": "Unauthorized user"},
        422: {"description": "Unprocessable Entity"}
    })
async def add_character(character: CharacterModel, current_user: User = Depends(get_current_active_user)):
    """
    This endpoint adds a new character to the database.

    - **character**: The character data to insert
    - **current_user**: The current logged-in user
    """
    # Check for null fields and validate types
    for field, value in character.dict().items():
        if value is None or (isinstance(value, str) and not value.strip()):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Field {field} cannot be empty")
    
    # Check if character already exists
    existing_character = await CharacterService.find_character_by_fields(character)
    if existing_character:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character already exists")

    # Add the new character to the database
    new_character = await CharacterService.add_character(character)
    
    # Return the newly created character with a 201 status code
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_character.dict())

@router.delete("/delete/{id}", response_model=dict, 
    summary="Delete character by ID", 
    description="Delete a character by its ID",
    responses={
        200: {"description": "Character successfully deleted"},
        400: {"description": "Character not found"},
        401: {"description": "Unauthorized User"},
        404: {"description": "ID cannot be empty"}
    })
async def delete_character(id: str = Path(..., description="The ID of the character to delete", min_length=1),
                                current_user: User = Depends(get_current_active_user)):
    """
    This endpoint deletes a character by its ID.

    - **id**: The ID of the character to delete
    - **current_user**: The current logged-in user
    """
    if len(id.strip()) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID cannot be empty")

    character = await CharacterService.get_character_by_id(id)
    if not character:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character does not exist")

    await CharacterService.delete_character(id)
    return {"message": "Character deleted successfully"}

