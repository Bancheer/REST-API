from pydantic import BaseModel
from typing import Optional
from datetime import date

class User(BaseModel):
    name: str
    last_name: str
    email: Optional[str]
    phone: int
    birthday: Optional[date]
    extra_data: Optional[str] = None