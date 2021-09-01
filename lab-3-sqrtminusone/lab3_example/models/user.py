import sqlalchemy as sa
from sqlalchemy import orm

from .base import Base

__all__ = ['User']


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(256))

    department_id = sa.Column(
        sa.Integer,
        sa.ForeignKey(
            'department.id',
            ondelete='cascade',
            onupdate='cascade',
        ),
        nullable=False
    )

    belongs_to_department = orm.relationship(
        'Department', back_populates="has_users"
    )

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, department_id={self.department_id})'
