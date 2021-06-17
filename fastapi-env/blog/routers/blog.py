from fastapi import APIRouter, Depends, status, Response, HTTPException
from starlette.routing import Router
from .. import schema, database, models
from sqlalchemy.orm import Session
from typing import List
from ..repistory import blog
get_db = database.get_db

router = APIRouter(
    prefix = "/blog",
    tags = ["Blogs"]
)
@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schema.Blog, db:Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/', response_model = List[schema.showBlog])
def all(db:Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT )
def destroy(id, db:Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED )
def update(id, request:schema.Blog, db:Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code = 200, response_model = schema.showBlog)
def show(id, db:Session = Depends(get_db)):
   return blog.show(id, db)
