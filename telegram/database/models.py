from alchemynger.sqlalchemy import Column, Integer

from .manager import manager

class User(manager.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    def __repr__(self) -> str:
        return f"User({self.id})"
    