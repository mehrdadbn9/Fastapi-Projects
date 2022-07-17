from typing import List
from schema import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from superbook2.db.database import get_db
from superbook2.db import db_article

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# Get specific article
@router.get('/{id}')  # , response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return {
        'data': db_article.get_article(db, id)
    }
