from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# mysql+<drivername>://<username>:<password>@<server>:<port>/dbname

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" + USERNAME + ":" + PASSWORD + "@localhost:3306/" + DB_NAME

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()