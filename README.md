# Учебный проект: API Yamdb
RestAPI для сервиса Yamdb - базы данных книг, музыки, фильмов.
## About
RestAPI для сервиса Yamdb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий (Category) может быть расширен администратором.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка.
Произведению может быть присвоен жанр (Genre) из списка предустановленны.
Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и
ставят произведению оценку в диапазоне от одного до десяти (целое число);
из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число).
На одно произведение пользователь может оставить только один отзыв.
## Как запустить проект:
- Склонировать репозиторий и перейти в папку проекта через командную строку:
```
git@github.com/ifize/api_yamdb
```
```
cd api_yamdb/
```
- Создать и активировать вируальное окружение (если вы работаете не в Pycharm):
```
python -m venv venv
```
```
source venv/Scripts/activate
```
- Установить зависимости
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Создать миграции:
```
python manage.py migrate
```
- Загрузить данные из .csv файла (api_yamdb/api_yamdb/static/data/) в БД с помощью management command:
```
python manage.py import_csv
```
- Запустить проект:
```
python manage.py runserver
```
## Примеры эндпоинтов
- Создать пользователя        http://127.0.0.1:8000/api/v1/auth/signup/
```
{ "email": "string", "username": "string" }
```
- Получить Jwt Token      http://127.0.0.1:8000/api/v1/auth/token/
```
{ "username": "string", "confirmation_code": "string" }
```
- Категории      http://127.0.0.1:8000/api/v1/categories/
- Жанры         http://127.0.0.1:8000/api/v1/genres/
- Произведения         http://127.0.0.1:8000/api/v1/titles/
- Отзывы        http://127.0.0.1:8000/api/v1/titles/1/reviews/
- Комментарии       http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/
- Пользователи          http://127.0.0.1:8000/api/v1/users/

## Команда разработчиков:
[Илья Воронков](https://github.com/ifize) | [Ильшат](https://github.com/ilshat2) | [Матвей Строков](https://github.com/Flock1993) |



![](https://img.shields.io/pypi/pyversions/p5?logo=python&logoColor=yellow&style=for-the-badge)
![](https://img.shields.io/badge/Django-2.2.16-blue)
![](https://img.shields.io/badge/DRF-3.12.4-lightblue)