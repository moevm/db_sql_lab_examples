# Лабораторная работа №3

Использование ORM для работы с базыми данных на примере Django ORM.

Пример структуры исходного кода. 

## Запуск 

```shell
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

Запуск команды на заполнение данными 
```shell
python3 manage.py fill_db
```

Запуск команд ответов на вопросы лаборатоных
```shell
python3 manage.py select_all
python3 manage.py select_active_admins
python3 manage.py insert_me
```