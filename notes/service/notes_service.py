from ..database import SessionLocal, get_db
from .. import schema
from ..models import note_model 
from fastapi import Depends, HTTPException,status

def  create(req: schema.Note ,  db: SessionLocal = Depends(get_db)):
    note = note_model.Note(title = req.title, content = req.content,is_public = req.is_public,author_id = 1)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_all_notes(db:SessionLocal = Depends(get_db)):
    return db.query(note_model.Note).all()

def get_note(id:int,db:SessionLocal = Depends(get_db)):
    note = db.query(note_model.Note).filter(note_model.Note.id == id).first()
    return note

def delete_note(id : int, db: SessionLocal = Depends(get_db)):
    db.query(note_model.Note).filter(note_model.Note.id == id).delete(synchronize_session = False)
    db.commit()
    return

def update_note(id:int,req: schema.Note, db:SessionLocal = Depends(get_db)):
    note = db.query(note_model.Note).filter(note_model.Note.id == id)
    if note.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"note with id '{id}' doesn't exits")
    note.update(req.model_dump())
    db.commit()
    return 