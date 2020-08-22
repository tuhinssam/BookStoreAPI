from fastapi import FastAPI, Body, Header, File
from models.user import User
from models.author import Author
from models.book import Book
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
app = FastAPI()

'''
Method: GET
basic get 
'''
@app.get('/')
async def hello_world():
    return {"Hello world fastapi!"}

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
@app.post('/user', status_code=HTTP_201_CREATED)
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
    #'embed = True' is used to take body in json format
    return {"name in body": name}

'''
method: POST
request: http://127.0.0.1:8000/user/author
body:
{   
	"user":
	{
	"id": 1,
	"name": "123",
    "password": "123456",
    "mail": "tuhinssa@gmail.com",
    "role": "admin"
	},
	"author":
	{
      "name": "author name1",
      "book": ["book1","book2"]
	}
}
'''
@app.post('/user/author')
async def post_user_and_author(user: User, author: Author):
    return {'user':user,'author':author}

'''
method: POST
request: http://127.0.0.1:8000/user/author/bookstore
body:
{   
	"user":
	{
	"id": 1,
	"name": "123",
    "password": "123456",
    "mail": "tuhinssa@gmail.com",
    "role": "admin"
	},
	"author":
	{
      "name": "author name1",
      "book": ["book1","book2"]
	},
	"bookstorename":"bookstore1"
}
'''
@app.post('/user/author/bookstore')
async def post_user_and_author_bookstore(user: User, author: Author, bookstorename: str = Body(..., embed=True)):
    '''
    body parameters which are not object should be decalred as Body(..., embed=True)
    '''
    return {'user':user,'author':author, 'bookstorename': bookstorename}

'''
Request with header
method: POST
request: http://127.0.0.1:8000/user/author/bookstore
header:
x-custom: dummayheader1
body:
{   
	"user":
	{
	"id": 1,
	"name": "123",
    "password": "123456",
    "mail": "tuhinssa@gmail.com",
    "role": "admin"
	},
	"author":
	{
      "name": "author name1",
      "book": ["book1","book2"]
	},
	"bookstorename":"bookstore1"
}
'''
@app.post('/userwithheader')
async def post_userwithheader(user: User, x_custom: str = Header(...)):
    '''
    default header can be created as x_custom: str = Header("default"), in this case head need not be createc with x-custom
    '''
    return {'user':user,'x_custom':x_custom}

'''
Return book object on Get Request
Method: GET
Request: http://127.0.0.1:8000/bookobj/isbn2
Response:
{
    "isbn": "isbn2",
    "author": {
        "name": "author1",
        "book": [
            "book1",
            "book2"
        ]
    }
}
'''
@app.get('/bookobj/{isbn}', response_model=Book, response_model_exclude=["name", "year"])
async def get_bookObj_with_isbn(isbn:str):
    author_dict = {
        "name": "author1",
        "book":["book1","book2"]
    }
    author1 = Author(**author_dict)
    book_dict = {
        "isbn": str(isbn),
        "name": "book1",
        "year":2019,
        "author": author1
    }
    book1 = Book(**book_dict)
    return book1

'''
Description: 
- Upload File using API. Use Body as Form Data and key as "profile_photo" and upload the file
- Get file size as a header
- set cookie
Method: POST
Request: http://127.0.0.1:8000/user/photo
Response:
{
    "File Size": 66704
}
'''
@app.post('/user/photo')
async def upload_user_photo(response: Response, profile_photo: bytes = File(...)):
    response.headers['x-file-size'] = str(len(profile_photo))
    response.set_cookie(key="cookie-api", value = "test-val")
    return {"File Size": len(profile_photo)}