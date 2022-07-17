from fastapi import FastAPI
# from starlette.responses import Response
# from sqlalchemy.engine import Engine
from superbook2.db import models
from superbook2.db.database import engine
from superbook2.router import blog_get, user
from superbook2.router import blog_post
from superbook2.router import article
from superbook2.db import models

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/home", summary='this is th summary', response_description="this is response description")
async def root():
    """
    this is **description in the def**
    """
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)
