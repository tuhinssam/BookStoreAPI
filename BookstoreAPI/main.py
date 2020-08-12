from fastapi import FastAPI
from models.user import User

app = FastAPI()

'''
Method: GET
basic get 
'''
@app.get('/')
async def hello_world():
    return {"Hello world fastapi!"}

'''
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
@app.post('/user')
async def post_user(user:User):
    return {"response-body":user}

'''
Method: GET
passing password as parameter in request url
Endpoint: http://127.0.0.1:8000/user?password=pass1
'''
@app.get('/user')
async def get_user_validation(password:str):
    return {"query parameter": password}