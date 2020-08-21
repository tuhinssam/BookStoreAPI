from fastapi import FastAPI, Body
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

'''
Method: GET
http://127.0.0.1:8000/book/isbn1
'''
@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"isbn of the book": isbn}

'''
Method: GET
http://127.0.0.1:8000/author/2/book?order=order1&category=category1
'''
@app.get("/author/{id}/book")
async def get_author_books(id: int, category: str, order: str= 'asc'):
    return {"Query Changable parameter": order + category + str(id)}

'''
Method: Patch
http://127.0.0.1:8000/author/name
body:
{
  "name":"tuhin"
}
'''
@app.patch('/author/name')
async def patch_author_name(name: str = Body(..., embed = True)):
    return {"name in body": name}