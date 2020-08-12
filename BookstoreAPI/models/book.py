from pydantic import BaseModel
import enum
from fastapi import Query
from models.author import Author

class User(BaseModel):
    isbn: int
    name: str
    author: Author
    year: str
