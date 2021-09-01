import click
import dotenv
from lab3_example import queries, scripts
from lab3_example.api import DBConn
from lab3_example.models import *
from lab3_example.models.base import Base


@click.group()
def cli():
    dotenv.load_dotenv()
    DBConn()


@cli.command()
def create_tables():
    Base.metadata.create_all(DBConn.engine)


@cli.command()
def drop_tables():
    Base.metadata.drop_all(DBConn.engine)


@cli.command()
@click.option('--department-id', '-d', type=click.INT)
def list_users(department_id):
    queries.list_users(department_id)


@cli.command()
def fill_db():
    scripts.fill_db()


if __name__ == '__main__':
    cli()
