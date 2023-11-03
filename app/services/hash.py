from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"])


class Hash():
    """
    Hash manager
    """

    @classmethod
    def bcrypt(cls, password: str) -> str:
        """
        bcrypt password

        Parameters
        ----------
        password : str
            password
        """
        return pwd_cxt.hash(password)

    @classmethod
    def verify(cls, plain_password: str, hashed_password: str) -> bool:
        """
        verify password
        """
        return pwd_cxt.verify(plain_password, hashed_password)
