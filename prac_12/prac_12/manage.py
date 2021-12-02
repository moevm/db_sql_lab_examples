from pprint import pprint

import click
import sqlalchemy as sa

from prac_12.config import DBConn, settings
from prac_12.models import Base

__all__ = ['cli']


@click.group()
def cli():
    DBConn()


@cli.command(help='Say hello')
def say_hello():
    print('hello')


@cli.command()
def print_config():
    pprint(dict(settings))


@cli.command()
def test_db():
    with DBConn.engine.connect() as conn:
        result = conn.execute(sa.text('select 2 + 3'))
        print(result.all())


@cli.command()
def create_models():
    Base.metadata.create_all(DBConn.engine)
