from pydantic import BaseModel, Field, validator

class CharacterModel(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int
    eye_color: str  # O ObjectId, dependiendo de cómo lo manejes

    @validator('*')
    def no_empty_fields(cls, v):
        if v is None or (isinstance(v, str) and not v.strip()):
            raise ValueError('Field cannot be empty')
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "Luke Skywalker",
                "height": 172,
                "mass": 77,
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": 1998,
            }
        }

class CharacterResponseModel(BaseModel):
    id: str
    name: str
    height: int
    mass: int
    birth_year: int
    eye_color: str

    class Config:
        schema_extra = {
            "example": {
                "id": "60d0fe4f5311236168a109ca",
                "name": "Luke Skywalker",
                "height": 172,
                "mass": 77,
                "birth_year": 1998,
                "eye_color": "blue"
            }
        }

from pydantic import BaseModel

class CharacterAddResponseModel(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int
    id: str  # Este campo se incluirá al final

    class Config:
        schema_extra = {
            "example": {
                "name": "string",
                "height": 0,
                "mass": 0,
                "hair_color": "string",
                "skin_color": "gfdgdfgdfgdfgfdgfdgdfg",
                "eye_color": "string",
                "birth_year": 0,
                "id": "60d0fe4f5311236168a109ca"  # Ejemplo de ID generado por la base de datos
            }
        }
