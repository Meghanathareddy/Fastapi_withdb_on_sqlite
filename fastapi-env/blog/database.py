from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = 'sqlite:///./blog.db'

engine = create_engine( sqlalchemy_database_url, connect_args = {"check_same_thread": False})

sessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False )
Base = declarative_base()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()