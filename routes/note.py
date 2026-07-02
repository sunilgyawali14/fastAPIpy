from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntity,notesEntity

note = APIRouter()

# Templates directory
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newdocs = []

    for doc in docs:
        newdocs.append({
            "id": str(doc["_id"]),   # Convert ObjectId to string
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],
        })

    return templates.TemplateResponse("index.html",{"request": request,"newdocs": newdocs})
@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    formDict["important"] = True if formDict.get("important") == "on" else False

    conn.notes.notes.insert_one(formDict)

    return {
        "success": True
    }

