from dynaconf import Dynaconf

__all__ = ['settings']

settings = Dynaconf(settings_files=['config.toml'])
