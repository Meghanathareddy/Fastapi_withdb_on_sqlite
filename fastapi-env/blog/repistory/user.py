from sqlalchemy.orm.session import Session
from .. import schema, database, models, hashing
from .. import models, schema, database
from fastapi import Depends, status, Response, HTTPException


def create_user(request:schema.User, db:Session ):
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int, db:Session):
    user =  db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} is not available")
       # response.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail':f"Blog with id {id} is not available"}
    return user