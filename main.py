from fastapi import FastAPI
# from starlette.responses import Response
from superbook2.router import blog_get
from superbook2.router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/home", summary='this is th summary', response_description="this is response description")
async def root():
    """
    this is **description in the def**
    """
    return {"message": "Hello World"}
