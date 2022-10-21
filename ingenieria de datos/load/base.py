from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///newspaper.bd') # nuestro motor

Session = sessionmaker(bind=Engine)

Base = declarative_base() #clase base de la cual van a extender todos nuestros modelos
