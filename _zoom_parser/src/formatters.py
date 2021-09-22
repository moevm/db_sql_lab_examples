import re
from fuzzywuzzy import fuzz
from transliterate import translit
from pydash import map_, order_by


def parse_name(name, with_midname=False):
    # В транслит
    name = translit(name, 'ru')
    # Нижний регистр
    name = name.lower()
    # Убрать номер группы
    name = re.sub(r'\d', '', name)
    # Нижнее подчеркивание = пробел
    name = name.replace('_', ' ')
    # Убрать дополнительную информацию из скобок
    name = re.sub(r'\(.*\)', '', name)
    # Убрать лишние пробелы
    name = name.strip()

    s = name.split(' ')

    def rejoin(s, index):
        return ' '.join(s[index:])

    if not with_midname:
        return s[0], rejoin(s, 1)
    else:
        return s[0], s[1], rejoin(s, 2)


def parse_email(email):
    return email.strip() if isinstance(email, str) else ''


def similarity_coefficient(str1, str2):
    return fuzz.ratio(str1, str2)


def pretty_name(name):
    return ' '.join(map_(name, lambda s: s.capitalize()))


def format_date(date):
    return date.strftime('%Y.%m.%d')


def sort_dict(v, order):
    for key, value in v.items():
        v[key] = order_by(value, order)
