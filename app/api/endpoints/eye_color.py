from fastapi import APIRouter, HTTPException
from app.services.eye_color import EyeColorService
from app.models.eye_color import EyeColor

router = APIRouter()

@router.post("/eye_colors/", response_model=EyeColor)
async def create_eye_color(color: str):
    eye_color = await EyeColorService.create_eye_color(color)
    return eye_color

@router.get("/eye_colors/{eye_color_id}", response_model=EyeColor)
async def get_eye_color(eye_color_id: str):
    eye_color = await EyeColorService.get_eye_color_by_id(eye_color_id)
    if not eye_color:
        raise HTTPException(status_code=404, detail="Eye color not found")
    return eye_color

@router.get("/eye_colors/", response_model=list[EyeColor])
async def get_all_eye_colors():
    return await EyeColorService.get_all_eye_colors()
