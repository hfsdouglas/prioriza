from sqlalchemy import Column, Integer, String, UUID, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.db import db

class Tasks(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer(), primary_key=True, autoincrement="auto", nullable=False)
    task = Column(String(350), nullable=False)
    user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="tasks")