import sqlalchemy as sa
from sqlalchemy import orm

from .base import Base

__all__ = ['Shelf']


class Shelf(Base):
    __tablename__ = 'shelf'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    room = sa.Column(sa.Integer(), nullable=False)
    name = sa.Column(sa.String(256), nullable=False)

    books = orm.relationship('Book', back_populates='shelf')

    def __repr__(self):
        return f'<Shelf id={self.id} name={self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "room": self.room,
            "name": self.name
        }
