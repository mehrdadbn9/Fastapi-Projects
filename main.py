from fastapi import FastAPI, HTTPException
# from starlette.responses import Response
# from sqlalchemy.engine import Engine
from fastapi.responses import PlainTextResponse
from exception import StoryException
from superbook2.database import engine
from superbook2.router import blog_get, user
from superbook2.router import blog_post
from superbook2.router import article
from superbook2.db import models
from fastapi import Request
from fastapi.responses import JSONResponse

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


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={'detail': exc.name})


@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: StoryException):
    return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)
