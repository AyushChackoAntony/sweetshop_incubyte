from fastapi import FastAPI
from backend.routers import auth
from backend import models
from backend.database import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth.router, prefix="/api/auth")