from pydash import get, map_, find

from configuration import sheets, users
from src.formatters import format_date, parse_name, parse_email, sort_dict
from src.logic import identify_user, add_not_visited, preprocess_results, count_total
from src.sheets import get_sheet, get_info_from_row
from src.excel_logic import write_excel


def main():
    # Скачивание всех таблиц
    sheet_dfs = map_(sheets, lambda x: {**x, **{'sheet': get_sheet(x)}})

    # Скачивание таблицы пользователя
    users_df = get_sheet(users)

    # Пользователи, которых не смогли определить
    unknown_users = {}
    # Студенты, которые не посетили пару
    user_not_visited = {}
    # Опознанные студенты
    found_users = {}

    # По каждой таблица посещаемости
    for sheet in sheet_dfs:
        date = format_date(sheet['date'])

        found_users[date] = []
        unknown_users[date] = []
        user_not_visited[date] = []

        for _, user in users_df.iterrows():
            user_name_raw = user[get(users, 'column_name')]
            if not user_name_raw or not isinstance(user_name_raw, str):
                break

            # Получаем ФИО, группу студента
            user_name = parse_name(user_name_raw, with_midname=True)
            user_group = int(user[get(users, 'column_group')])
            user_email = parse_email(user[get(users, 'column_email')])

            # Ищем пользователя и сохраняем информацию
            found_user = identify_user(sheet, found_users, date, user_name,
                                       user_email, user_group)

            if not found_user:
                add_not_visited(user_not_visited, date, user_name, user_email,
                                user_group)

    # Повторно проходим, чтобы просмотреть не сопоставленные строки
    for sheet in sheet_dfs:
        date = format_date(sheet['date'])

        unknown_users[date] = []

        for row_index, row in sheet['sheet'].iterrows():
            found = find(found_users[date],
                         lambda x: row_index in x['row_index'])
            if not found:

                user_attendance_name, user_attendance_email, user_attendance_minutes = get_info_from_row(
                    row, sheet)

                unknown_users[date].append({
                    'name': user_attendance_name,
                    'minutes': user_attendance_minutes,
                    'email': user_attendance_email,
                })

    # Объединяем списки
    for key, value in user_not_visited.items():
        found_users[key] += value

    sort_dict(found_users, ['group', 'user_name'])
    sort_dict(unknown_users, ['name'])

    preprocess_results(found_users)

    total = count_total(found_users)

    write_excel(total, found_users, unknown_users)
