from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer, String

from app.models.setting import BaseModel, Engine, session
from app.services.hash import Hash


class UserModel(BaseModel):
    """
    UserModel
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), unique=True, nullable=False, comment='user name')
    password = Column(String(256), nullable=False, comment='user password')
    e_mail = Column(String(256), unique=True, nullable=False, comment='user e_mail')
    is_enabled = Column(Boolean, default=True, comment='is enabled')

    def __init__(self,
                 name: str,
                 password: str,
                 e_mail: str,
                 is_enabled: bool = True,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:

        self.name = name
        self.password = Hash.bcrypt(password)
        self.e_mail = e_mail
        self.is_enabled = is_enabled
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"<UserModel(name={self.name}, is_enabled={self.is_enabled})>"

    def save(self) -> None:
        """
        save
        """
        session.add(self)
        session.flush()


if __name__ == "__main__":
    BaseModel.metadata.create_all(bind=Engine)
