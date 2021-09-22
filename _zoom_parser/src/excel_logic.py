from pydash import get
from xlsxwriter import Workbook

from configuration import output_file


def write_sheet(wb, ws, data, offset=0, header_map=None, with_colors=True):
    keys = list(data[0].keys())
    keys_translation = keys if not header_map else list(header_map.values())

    first_row = 0 + offset
    for header in keys_translation:
        col = keys_translation.index(header)
        ws.write(first_row, col, header)

    green = wb.add_format({'bg_color': '#00FF00'})
    yellow = wb.add_format({'bg_color': '#FFFF00'})
    red = wb.add_format({'bg_color': '#FF0000'})

    row = 1 + offset
    for row_data in data:

        color = None
        if get(row_data, 'visited_enough'):
            color = green
        if not get(row_data, 'visited_enough'):
            color = yellow
        if get(row_data, 'row_index') == '-':
            color = red

        for _key, _value in row_data.items():
            col = keys.index(_key)
            if not color or not with_colors:
                ws.write(row, col, str(_value))
            else :
                ws.write(row, col, str(_value), color)

        row += 1


header_map = {
    'user_name': 'ФИО',
    'group': 'Группа',
    'user_email': 'Почта',
    'match_with': 'Совпадение с',
    'row_index': 'Номера строк',
    'by_email': 'Совпадение по почте',
    'prob_1': 'Вероятн. 1',
    'prob_2': 'Вероятн. 2',
    'minutes': 'Длительность',
    'visited_enough': 'Балл'
}

header_map_unknown = {
    'name': 'Неопознанный',
    'email': 'Почта',
    'minutes': 'Длительность'
}

header_total = {
    'user_name': 'ФИО',
    'user_group': 'Группа',
    'count': 'Кол-во',
    'dates': 'Даты посещения',
}


def write_excel(total, found_users, unknown_users):
    wb = Workbook(output_file)

    ws = wb.add_worksheet('Посещение')
    write_sheet(wb, ws, total, header_map=header_total, with_colors=False)

    for key, value in found_users.items():

        ws = wb.add_worksheet(key)
        write_sheet(wb, ws, value, header_map=header_map)
        write_sheet(wb,
                    ws,
                    unknown_users[key],
                    offset=len(value) + 2,
                    header_map=header_map_unknown)

    wb.close()
