from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    # below class convert data of database to require(above) format
    class Config:
        orm_mode = True
