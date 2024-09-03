from pydantic import BaseModel
from typing import Optional

class EyeColor(BaseModel):
    id: Optional[str] = None
    color: str
