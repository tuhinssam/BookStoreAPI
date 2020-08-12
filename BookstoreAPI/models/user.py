from pydantic import BaseModel
import enum

class Role(str, enum.Enum):
    admin: str = 'admin'
    personel: str = 'personel'

class User(BaseModel):
    id: int
    name: str
    password: str
    mail: str
    role: Role