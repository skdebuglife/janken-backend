from dataclasses import dataclass
from typing import Union

from pydantic import BaseModel

from app.errors.message import ErrorMessage


@dataclass
class InternalServerErrorOut(BaseModel):

    detail: str = ErrorMessage.INTERNAL_SERVER_ERROR


@dataclass
class InvalidRequestErrorOut(BaseModel):

    detail: str = ErrorMessage.INVALID_REQUEST


@dataclass
class DataBaseErrorOut(BaseModel):

    detail: str = ErrorMessage.DATABASE_ERROR


@dataclass
class DataBaseConnectionErrorOut(BaseModel):

    detail: str = ErrorMessage.DATABASE_CONNECTION_ERROR


@dataclass
class Root500ErrorClass(BaseModel):
    __root__: Union[InternalServerErrorOut, DataBaseErrorOut, DataBaseConnectionErrorOut]
