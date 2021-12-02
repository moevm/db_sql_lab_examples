from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy import orm

from prac_12.config import settings


__all__ = ['DBConn']


class DBConn:
    engine = None
    Session = None

    def __init__(self):
        DBConn.engine = DBConn.get_engine()
        DBConn.Session = orm.sessionmaker()
        DBConn.Session.configure(bind=DBConn.engine)

    @staticmethod
    def get_engine():
        url = 'mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4'.format(
            settings.database.user, settings.database.password,
            settings.database.host, settings.database.database
        )
        return sa.create_engine(url, echo=True, future=True)

    @staticmethod
    @contextmanager
    def get_session(**kwargs):
        session = DBConn.Session(**kwargs)
        yield session
        session.close()
