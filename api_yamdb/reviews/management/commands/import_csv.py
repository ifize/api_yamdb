import csv

from django.core.management.base import BaseCommand

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
    User,
)

FILE_MODEL = {
    'category': Category,
    'genre': Genre,
    'titles': Title,
    'users': User,
    'review': Review,
    'comments': Comment,
}


class Command(BaseCommand):
    # вывод в консоль при python python manage.py import_csv --help
    help = 'Команда для импорта данных из .csv файла'

    def handle(self, *args, **options):
        """
        Функция импорта csv в базу данных проекта
        запуск производится командой python manage.py import_csv
        """
        # открываем в менеджере контекста для автоматического закрытия файла
        # аргумент newline - чтобы знаки абзаца случайно не попали в БД
        for file_name, model in FILE_MODEL.items():
            with open(
                    f'static/data/{file_name}.csv',
                    newline='',
                    encoding='utf-8'
            ) as csv_file:
                # DictReader =([('id', '1'), ('name', 'Фильм'), ('slug', 'movie')])
                datareader = csv.DictReader(csv_file, delimiter=',')
                model.objects.bulk_create(
                    [model(**row) for row in datareader])
            if file_name == 'category':
                break
        print('data import was successful')

