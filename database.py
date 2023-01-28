from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()
password = os.getenv('password')

engine = create_engine("postgresql://postgres:{}@localhost/pizza_delivery".format(password), echo=True)


Base = declarative_base()

Session = sessionmaker()