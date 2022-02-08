from typing import Optional
from pydantic import BaseModel

class user_model(BaseModel):
    #id: Optional[str]
    name: str
    surname:str
    #alive: bool
    #traits: Optional[list]
    season:Optional[int]
    age:Optional[int]
