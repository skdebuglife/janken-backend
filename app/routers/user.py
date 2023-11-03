from fastapi import APIRouter

from app import handle_errors
from app.models import UserModel, session
from app.routers.setting import AppRoutes
from app.schemas.requests import UserSaveIn
from app.schemas.responses import UserSaveOut

router = APIRouter(
    prefix=AppRoutes.Users.PREFIX,
    tags=[AppRoutes.Users.TAG],
)


@router.post(AppRoutes.Users.POST_URL, response_model=UserSaveOut)
@handle_errors
async def create_user(user: UserSaveIn):
    """
    create user
    """
    try:
        user = UserModel(**user.dict())
        user.save()
        session.commit()
        return UserSaveOut()
    except Exception:
        session.rollback()
    finally:
        session.close()
