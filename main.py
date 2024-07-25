from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# get 방식으로 루트 호출되면 Hello World(@키워드는 메서드 방식을 의미...?)
@app.get("/")
def printHello():
    return "Hello FastAPI"

@app.get("/json")
def printJson():
    return {
        "Number": 12345,
    }

class Post(BaseModel):
	title: str
	content: str


@app.post("/posts")
def createContent(post: Post):
    title = post.title
    content = post.content

    print(f'title : {title}, content : {content}')
