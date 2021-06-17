from fastapi import APIRouter, Depends, status, Response, HTTPException
from starlette.routing import Router
from .. import schema, database, models, hashing
from sqlalchemy.orm import Session
from ..repistory import user

from typing import List
get_db = database.get_db

router = APIRouter(
    prefix = "/user",
    tags = ["User"]
)

@router.post('/', response_model = schema.showUser)
def create_user(request:schema.User, db:Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model = schema.showUser)
def get_user(id:int, db:Session =Depends(get_db)):
    return user.get_user(id, db)
 