from lab3_example.api import DBConn
from lab3_example.models import User
from sqlalchemy import select

__all__ = ['list_users']


def list_users(department_id):
    with DBConn.get_session() as session:
        users = session.execute(select(User).where(User.department_id==department_id))
        for user in users:
            print(user)
