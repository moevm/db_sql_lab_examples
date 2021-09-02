import os
from contextlib import contextmanager
from typing import Any, cast

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ['DBConn']


class DBConn:
    engine = None
    session: Any = None

    def __init__(self):
        DBConn.engine = create_engine(os.environ['URI'], future=True, echo=True)
        DBConn.session = sessionmaker(DBConn.engine)

    @staticmethod
    @contextmanager
    def get_session(**kwargs):
        """
        with DBConn.get_session() as session:
            # do stuff
        """
        session = DBConn.session(**kwargs)
        yield session
        session.close()
