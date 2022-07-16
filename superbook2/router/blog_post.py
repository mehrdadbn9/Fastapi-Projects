from enum import Enum
from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    body: str
    number_like: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None


@router.post('/new/{id}/blog/{blog_id}')
def create_blog(blog: BlogModel, id: int, version: int = 1,
                content: str = Body(..., max_length=50, min_length=10, regex='^[a-z\s]*$'),
                v: Optional[List[str]] = Query(['1', '2']),
                blog_id: int = Path(None, gt=6, le=8)):
    return {'data': blog, "id": id, 'content': content, "version": v}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_id: int = Query(None, title='this is id comment', description="some description",
                                           alias='commentId', deprecated=True)):
    return {'blog': blog, "id": id, "comment_id": comment_id}


def require_functionality():
    return 'this is required parameters'
