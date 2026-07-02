from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app =  FastAPI()
app.include_router(note)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
# Templates directory
templates = Jinja2Templates(directory="templates")
