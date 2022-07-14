from enum import Enum
from typing import Optional
from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/')
def create_blog():
    pass
