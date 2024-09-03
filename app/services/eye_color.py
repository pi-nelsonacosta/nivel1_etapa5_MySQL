from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from bson import ObjectId
from bson.errors import InvalidId
from app.models.eye_color import EyeColor

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]

class EyeColorService:
    @staticmethod
    async def create_eye_color(color: str):
        eye_color = {"color": color}
        result = await db.eye_colors.insert_one(eye_color)
        eye_color["id"] = str(result.inserted_id)
        return EyeColor(**eye_color)

    @staticmethod
    async def get_eye_color_by_id(eye_color_id: str):
        try:
            eye_color = await db.eye_colors.find_one({"_id": ObjectId(eye_color_id)})
            if eye_color:
                eye_color["id"] = str(eye_color["_id"])
                return EyeColor(**eye_color)
            return None
        except InvalidId:
            return None

    @staticmethod
    async def get_all_eye_colors():
        eye_colors = await db.eye_colors.find().to_list(1000)
        for eye_color in eye_colors:
            eye_color["id"] = str(eye_color["_id"])
        return [EyeColor(**ec) for ec in eye_colors]

