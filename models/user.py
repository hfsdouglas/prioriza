from sqlalchemy import Column, String, UUID
from database.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, default=db.func.uuid_generate_v4())
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    name = Column(String(100), nullable=False)