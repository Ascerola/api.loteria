import uvicorn
from fastapi import FastAPI

from api import register_routes
from config import APP_HOST, APP_PORT

app = FastAPI()
register_routes(app)

