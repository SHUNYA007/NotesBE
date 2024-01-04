from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from ..database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,index= True)
    name = Column(String(length=255))
    username = Column(String(length = 255))
    email  = Column(String(length=255))
    password = Column(String(length=255))
    is_actice = Column(Boolean,default=True)

    notes = relationship("Note", back_populates="author")


