from fastapi import APIRouter, Depends, status, HTTPException
from ..database import SessionLocal, get_db
from .. import schema
from ..service import notes_service

router = APIRouter(
    prefix="/note",
    tags=["Notes"]
    )



@router.post("/",status_code=status.HTTP_201_CREATED)
def create_note(req: schema.Note, db: SessionLocal = Depends(get_db)):
    note =  notes_service.create(req,db)
    return note

@router.get("/")
def get_all_notes(db:SessionLocal = Depends(get_db)):
    notes = notes_service.get_all_notes(db)
    return notes

@router.get("/{id}",status_code= status.HTTP_200_OK)
def get_note(id:int,db:SessionLocal = Depends(get_db)):
    note = notes_service.get_note(id,db)
    if note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Note with id `{id}` doesn't exists")
    return note



@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_note(id : int, db: SessionLocal = Depends(get_db)):
    notes_service.delete_note(id,db)
    return "deleted!!"

@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update_note(id:int,req: schema.Note, db:SessionLocal = Depends(get_db)):
    notes_service.update_note(id,req,db)
    return 'updated!!!'



