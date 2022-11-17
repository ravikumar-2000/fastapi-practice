import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


'''
    pip install mysqlclient
    pip install sqlalchemy
    connection string => mysql://username:password@server:port/database_name
'''


def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


MYSQL_USERNAME = os.getenv('MYSQLUSERNAME')
MYSQL_PASSWORD = os.getenv('MYSQLPASSWORD')
DB_NAME = 'fastapi-db'
HOST = '127.0.0.1'
PORT = 3306


engine = create_engine(
    f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{HOST}:{PORT}/{DB_NAME}")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
