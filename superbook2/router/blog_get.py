from enum import Enum
from typing import Optional
from fastapi import APIRouter, status, Response, Depends

from superbook2.router.blog_post import require_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogType(str, Enum):
    short = 'short'
    long = 'long'

# @app.get("/blog/{type}")
# async def get_blog(type: BlogType):
#     return {"message": f"this is {type}"}


@router.get('/blog/all', description='this is description in the parentheses')
#query params
async def get_blogs(page=1, page_Size: Optional[int] = None, req_parameter: dict = Depends(require_functionality)):
    return {'message': f"all page_size {page_Size} and currently you are in the page {page}", 'req_param': req_parameter}


@router.get("/{id}", status_code=status.HTTP_200_OK, tags=['single_page'])
async def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"this blog with {id}"}
