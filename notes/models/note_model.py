from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text
from ..database import Base
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__ =   "note"

    id = Column(Integer, primary_key=True,index= True)
    title = Column(String(length=255))
    content = Column(Text)
    is_public = Column(Boolean,default=False)
    author_id  = Column(Integer, ForeignKey("user.id"))

    author = relationship('User', back_populates="notes")
    