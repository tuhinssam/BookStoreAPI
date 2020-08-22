from fastapi import FastAPI, Body, Header, File
from models.user import User
from models.author import Author
from models.book import Book
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response

app_v2 = FastAPI(openapi_prefix="/v2")

'''
Method: GET
basic get 
'''
@app_v2.get('/')
async def hello_world():
    return {"Hello world fastapi from v2!"}

'''
Create post and use custom status code 201
Method: POST
Body:
{   
	"id": 1,
	"name": "123",
    "password": "123456",
    "mail": "tuhinssa@gmail.com",
    "role": "admin"
}
endpoint: http://127.0.0.1:8000/user
'''
@app_v2.post('/user', status_code=HTTP_201_CREATED)
async def post_user(user:User):
    return {"response-body-from-apiv2":user}