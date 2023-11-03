import yaml
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.middleware.exception_middleware import ExceptionMiddleware
from app.models.setting import initialize_db, initialize_table
from app.routers import author_router, book_router, user_router

APP_TITLE = "janken-backend"
APP_VERSION = "1.0"
APP_DESCRIPTION = "This is a janken-backend"

app = FastAPI(title=APP_TITLE,
              version=APP_VERSION,
              description=APP_DESCRIPTION)

app.include_router(user_router)


if __name__ == "__main__":
    export_swagger()
