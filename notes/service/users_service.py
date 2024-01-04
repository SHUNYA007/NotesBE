from ..database import SessionLocal, get_db
from .. import schema
from ..models import user_model 
from fastapi import Depends, HTTPException,status

def  create(req: schema.User ,  db: SessionLocal = Depends(get_db)):
    user = user_model.User(email = req.email, name = req.name,password = req.password,username = req.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:SessionLocal = Depends(get_db)):
    return db.query(user_model.User).all()

def get_user(id:int,db:SessionLocal = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == id).first()
    return user

def delete_user(id : int, db: SessionLocal = Depends(get_db)):
    db.query(user_model.User).filter(user_model.User.id == id).delete(synchronize_session = False)
    db.commit()
    return

def update_user(id:int,req: schema.User, db:SessionLocal = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == id)
    if user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id '{id}' doesn't exits")
    user.update(req.model_dump())
    db.commit()
    return 