from fastapi import status

from app.errors.message import ErrorMessage


class AppError(Exception):
    """App Base Exception
    """

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = 'Error Message'


class InternalServerError(AppError):

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = ErrorMessage.INTERNAL_SERVER_ERROR


class InvalidRequestError(AppError):

    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = ErrorMessage.INVALID_REQUEST


class DataBaseError(AppError):

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = ErrorMessage.DATABASE_ERROR


class DataBaseConnectionError(AppError):

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = ErrorMessage.DATABASE_CONNECTION_ERROR
