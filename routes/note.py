from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


# @note.post("/")
# def add_note(note: Note):
#     inserted_note = conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)

@note.post("/", response_class=HTMLResponse)
async def create_item(request: Request):
    pass