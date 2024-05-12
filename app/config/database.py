from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
host = getenv("POSTGRES_HOST")
port = getenv("POSTGRES_PORT")
database = getenv("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{database}'  # Modify this line

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
