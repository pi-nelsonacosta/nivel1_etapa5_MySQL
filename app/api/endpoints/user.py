from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.models.user import User, UserCreate, UserInDB
from app.services.auth import (authenticate_user, create_access_token, get_password_hash, get_current_active_user)
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

router = APIRouter()

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]

@router.post("/register", response_model=User, 
             summary="Register a new user", 
             description="Register a new user with email and password", responses={
             201: {"description": "User created"},
             400: {"description": "User already exists"}                        
            })
async def register(user_in: UserCreate):
    """
    This endpoint registers a new user.
    """
    user = await db.users.find_one({"email": user_in.email})
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    hashed_password = get_password_hash(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    await db.users.insert_one(user_in_db.dict())
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=user_in_db.dict())

@router.post("/token", response_model=dict, 
             summary="Get access token", 
             description="Authenticate user and get an access token",
             responses={
            200: {"description": "Token Generated"},
            401: {"description": "Unauthorized User"}
       
    })
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This endpoint authenticates the user and provides an access token.
    """
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=User, summary="Get current user", description="Get details of the current authenticated user")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    This endpoint retrieves the current authenticated user's information.
    """
    return current_user

