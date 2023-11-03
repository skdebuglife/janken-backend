from datetime import datetime

from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from app.models import UserModel, session


class UserFactory(SQLAlchemyModelFactory):
    class Meta:

        model = UserModel
        sqlalchemy_session = session

    name = Sequence(lambda n: f'name_{n}')
    password = Sequence(lambda n: f'password_{n}')
    e_mail = Sequence(lambda n: f'e_mail_{n}@sss.co.jp')
    created_at = datetime.now()
    updated_at = datetime.now()
