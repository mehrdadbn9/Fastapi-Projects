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


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        orm_mode = True
