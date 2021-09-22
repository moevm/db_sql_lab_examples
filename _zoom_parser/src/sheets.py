import pandas as pd
import requests as requests
from io import BytesIO
from pydash import get


def sheet_id_to_url(sheet_id, name):
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={name}"


def get_sheet(sheet):
    url = sheet_id_to_url(get(sheet, 'sheet_id'), get(sheet, 'table_name'))
    r = requests.get(url)
    return pd.read_csv(BytesIO(r.content), encoding='utf-8')


def get_info_from_row(row, sheet):
    user_attendance_name = row[sheet['column_name']]
    user_attendance_email = row[sheet['column_email']]
    user_attendance_minutes = row[sheet['column_endurance']]
    return user_attendance_name, user_attendance_email, user_attendance_minutes
