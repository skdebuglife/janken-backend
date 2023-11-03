from app.services.hash import Hash


class TestHash():

    def test_bcrypt(self) -> None:
        """
        test_bcrypt
        """
        password = 'test'
        hashed_password = Hash.bcrypt(password)

        assert hashed_password != password
        assert isinstance(hashed_password, str)
        assert len(hashed_password) > 0

    def test_verify(self) -> None:
        """
        test_verify
        """
        password = 'test'
        hashed_password = Hash.bcrypt(password)

        assert Hash.verify(password, hashed_password) is True
        assert Hash.verify('test2', hashed_password) is False
