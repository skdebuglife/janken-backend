from pydantic import BaseModel, Field


class UserSaveIn(BaseModel):
    """

    Attributes
    ----------
    name : str
        user name
    password : str
        user password
    e_mail : str
        user e_mail
    """

    name : str = Field(title='name', min_length=1, max_length=255)
    password : str = Field(title='password', min_length=8, max_length=255)
    e_mail : str = Field(title='e_mail', min_length=1, max_length=255)

    class Config:
        schema_extra = {
            'example': {
                'name': 'test',
                'password': 'test',
                'e_mail': 'sample1111@gss.com'
            }
        }
