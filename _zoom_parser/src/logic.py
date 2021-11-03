from pydash import map_, find, get, pick

from configuration import similarity_threshold
from src.formatters import parse_name, similarity_coefficient, pretty_name, sort_dict
from src.sheets import get_info_from_row


def identify_user(sheet, found_users, date, user_name, user_email, user_group):
    found_user = False
    # По каждой строке таблицы посещаемости
    for row_index, row in sheet['sheet'].iterrows():
        user_attendance_name, user_attendance_email, user_attendance_minutes = get_info_from_row(
            row, sheet)

        possible_name = parse_name(user_attendance_name)

        # Варианты сопоставления
        variants_name = [
            f'{possible_name[1]} {possible_name[0]}',
            f'{possible_name[0]} {possible_name[1]}'
        ]
        name_format = f'{user_name[0]} {user_name[1]}'

        s1 = similarity_coefficient(name_format, variants_name[0])
        s2 = similarity_coefficient(name_format, variants_name[1])

        # Если нет совпадения по ФИО или почте - следующая строка
        if not (s1 > similarity_threshold or s2 > similarity_threshold
                or user_email == user_attendance_email):
            continue

        # Студент найден
        found_user = True

        # Учитываем случай, если студент зашел с 2+ аккаунтов - обновление данных
        duplicate = find(found_users[date],
                         lambda x: x['user_email'] == user_email)
        if duplicate:
            duplicate['minutes'].append(user_attendance_minutes)
            duplicate['row_index'].append(row_index)
            duplicate['match_with'].append(user_attendance_name)
            duplicate['visited_enough'] = sum(map_(duplicate['minutes'],
                                                   int)) >= sheet['min_time']
            continue

        # Сохраняем пользователя
        visited_enough = user_attendance_minutes >= sheet['min_time']
        found_users[date].append({
            'user_name': pretty_name(user_name),
            'group': user_group,
            'user_email': user_email,
            'match_with': [user_attendance_name],
            'row_index': [row_index],
            'by_email': user_email == user_attendance_email,
            'prob_1': s1,
            'prob_2': s2,
            'minutes': [user_attendance_minutes],
            'visited_enough': visited_enough,
        })
    return found_user


def add_not_visited(user_not_visited, date, user_name, user_email, user_group):
    user_not_visited[date].append({
        'user_name': pretty_name(user_name),
        'group': user_group,
        'user_email': user_email,
        'match_with': '-',
        'row_index': '-',
        'by_email': False,
        'prob_1': 0,
        'prob_2': 0,
        'minutes': 0,
        'visited_enough': False,
    })


def count_total(found_users):
    results = []
    for date, users in found_users.items():
        for user in users:
            found = find(results,
                         lambda u: u['user_name'] == user['user_name'])
            counter = 1 if user['visited_enough'] else 0

            if found:
                found['count'] += counter
                if counter:
                    found['dates'].append(date)
            else:
                results.append({
                    'user_name': user['user_name'],
                    'user_group': user['group'],
                    'count': counter,
                    'dates': [date] if counter else []
                })
    sort_dict({'_': results}, ['group', 'user_name'])
    return results


def preprocess_results(v):
    # Из-за заголовков индексы едут
    for key, value in v.items():
        for el in value:
            if isinstance(get(el, 'row_index'), list):
                el['row_index'] = map_(el['row_index'], lambda i: i + 2)
