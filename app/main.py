from fastapi import FastAPI

from app.routers import user_router

APP_TITLE = "janken-backend"
APP_VERSION = "1.0"
APP_DESCRIPTION = "This is a janken-backend"

app = FastAPI(title=APP_TITLE,
              version=APP_VERSION,
              description=APP_DESCRIPTION)

app.include_router(user_router)
