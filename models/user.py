from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from database.db import db
import uuid

class User(db.Model):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    name = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete")