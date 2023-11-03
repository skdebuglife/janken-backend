from pydantic import BaseModel, Field


class UserSaveOut(BaseModel):

    message: str = Field(title='message', default='success')

    class Config:
        schema_extra = {
            'example': {
                'message': 'success'
            }
        }
