from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
  # only get published blogs
    if published:
      return {"data": f'{limit} published blogs from the list'}
    else:
      return {"data": f'{limit} blogs from the list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1','2'}}

class Blog(BaseModel):
  title: str
  body: str
  published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog is created {blog.title}'}