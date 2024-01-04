from fastapi import APIRouter, Depends, status, HTTPException
from ..database import SessionLocal, get_db
from .. import schema
from ..service import users_service

router = APIRouter(
    prefix="/user",
    tags=["Users"]
    )



@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(req: schema.User, db: SessionLocal = Depends(get_db)):
    user =  users_service.create(req,db)
    return user

@router.get("/")
def get_all_users(db:SessionLocal = Depends(get_db)):
    users = users_service.get_all_users(db)
    return users

@router.get("/{id}",status_code= status.HTTP_200_OK)
def get_user(id:int,db:SessionLocal = Depends(get_db)):
    user = users_service.get_user(id,db)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"user with id `{id}` doesn't exists")
    return user



@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_user(id : int, db: SessionLocal = Depends(get_db)):
    users_service.delete_user(id,db)
    return "deleted!!"

@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update_user(id:int,req: schema.User, db:SessionLocal = Depends(get_db)):
    users_service.update_user(id,req,db)
    return 'updated!!!'



