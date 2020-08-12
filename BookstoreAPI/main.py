from fastapi import FastAPI
from models.user import User

app = FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello world fastapi!"}
@app.post('/user')
async def post_user(user:User):
    return {"response-body":user}
