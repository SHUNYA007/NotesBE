from ..database import Base

from .note_model import Note
from .user_model import User


def create_all_models(engine):
    Base.metadata.create_all(bind=engine)