from typing import Optional
from fastapi import FastAPI

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