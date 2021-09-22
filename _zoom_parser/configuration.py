from datetime import datetime

# Исходная таблица со студентами
users = {
    'sheet_id': '1WdaaGINwqaOvzUKYT-5l9ZkDSKuUSsz78eVizJQUrSw',
    'table_name': 'Оценки',
    'column_name': 'ФИО',
    'column_group': 'Группа',
    'column_email': 'Email'
}

# Указать откуда брать данные, за какую пару, сколько минимум минут
sheets = [{
    'sheet_id': '1xU4akJt6QbTG2FYsrBgYYRTRTrqGRc9IRtdoN-SKQx4',
    'table_name': "09.09.2021",
    'date': datetime(2021, 9, 9),
    'min_time': 45,
    'column_name': 'ФИО',
    'column_endurance': 'Длительность',
    'column_email': 'Почта'
}, {
    'sheet_id': '1xU4akJt6QbTG2FYsrBgYYRTRTrqGRc9IRtdoN-SKQx4',
    'table_name': "16.09.2021",
    'date': datetime(2021, 9, 16),
    'min_time': 75,
    'column_name': 'ФИО',
    'column_endurance': 'Длительность',
    'column_email': 'Почта'
}]

output_file = 'Подсчет посещения.xlsx'
similarity_threshold = 85
