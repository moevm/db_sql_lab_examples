# Лабораторная работа 5

> Тестирование БД на безопасность

Задачи:
- Сделать простой web-сервер для выполнения запросов из ЛР3, например с [express.js](https://expressjs.com/). Не обязательно делать авторизацию и т.п., хватит одного эдпоинта на каждый запрос, с параметрами запроса как query parameters.
- Намеренно сделайте несколько (2-3) запроса, подверженных SQL-инъекциям
- Проверьте Ваше API с помощью [sqlmap](https://sqlmap.org/) (или чего-то аналогичного), передав эндпоинты в качестве целей атаки. Посмотрите, какие уязвимости он нашёл (и не нашёл), опишите пути к исправлению.
- +2 балла, если напишете эндпоинт с уязвимостью, которая не находится sqlmap-ом.
