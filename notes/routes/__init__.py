from fastapi import APIRouter
from importlib import import_module

router = APIRouter()

from .notes_route import router as notes_router
from .user_route import router as users_router

router.include_router(notes_router)
router.include_router(users_router)