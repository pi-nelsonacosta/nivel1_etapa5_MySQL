from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from bson import ObjectId
from bson.errors import InvalidId  # Asegúrate de que este sea el import correcto
from app.models.character import CharacterAddResponseModel, CharacterModel, CharacterResponseModel

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]

class CharacterService:
    @staticmethod
    async def get_all_characters():
        characters = await db.characters.find().to_list(1000)
        for character in characters:
            character["id"] = str(character["_id"])
        return [CharacterResponseModel(**character) for character in characters]

    @staticmethod
    async def get_character_by_id(character_id: str):
        try:
            character = await db.characters.find_one({"_id": ObjectId(character_id)})
            if not character:
                return None  # Return None if the character is not found

            # Convert MongoDB's _id to id
            character["id"] = str(character["_id"])
            del character["_id"]  # Remove _id from the response if it's not needed

        except InvalidId:
            return None  # Return None if the provided ID is invalid
        
        return character
    
    @staticmethod
    async def find_character_by_fields(character: CharacterModel):
        existing_character = await db.characters.find_one({
            "name": character.name,
            "height": character.height,
            "mass": character.mass,
            "hair_color": character.hair_color,
            "skin_color": character.skin_color,
            "eye_color": character.eye_color,
            "birth_year": character.birth_year
        })
        return existing_character

    @staticmethod
    async def add_character(character: CharacterModel):
        character_dict = character.dict()
        result = await db.characters.insert_one(character_dict)
        character_dict["id"] = str(result.inserted_id)
        return CharacterAddResponseModel(**character_dict)

    @staticmethod
    async def delete_character(character_id: str):
        await db.characters.delete_one({"_id": ObjectId(character_id)})

