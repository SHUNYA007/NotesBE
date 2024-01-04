from fastapi import FastAPI
from typing import Optional
from notes.schema import Note

app = FastAPI()


@app.get("/")
async def read_root():
    return {"data":{"hello":"world"}}

@app.get("/note")
async def get_all_notes(sort:Optional[int] = None,limit = 10):
    return {"data":{"data":"list of all notes, limit:"+ str(limit)}}

@app.get("/note/{id}")
async def get_note(id:int):
    return {"data":id}


@app.post("/note")
async def create_post(note : Note):
    return {"data":note}
