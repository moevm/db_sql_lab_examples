import sqlalchemy as sa
from sqlalchemy import orm

from .base import Base

__all__ = ['Book']


class Book(Base):
    __tablename__ = 'book'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(256), nullable=False)
    shelf_id = sa.Column(sa.Integer(), sa.ForeignKey('shelf.id'), nullable=True)

    shelf = orm.relationship('Shelf', back_populates='books')

    def __repr__(self):
        return f'<Book id={self.id} name={self.name}>'
