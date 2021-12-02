from sqlalchemy import orm

__all__ = ['Base']

mapper_registry = orm.registry()
Base = mapper_registry.generate_base()
