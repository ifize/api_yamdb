import csv

from django.core.management.base import BaseCommand

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
)
from user.models import User

FILE_MODEL = {
    'category': Category,
    'genre': Genre,
    'titles': Title,
    'users': User,
    'review': Review,
    'comments': Comment,
    'user': User
}


class Command(BaseCommand):
    # вывод в консоль при python python manage.py import_csv --help
    help = 'Команда для импорта данных из .csv файла'

    def handle(self, *args, **options):
        """
        Функция импорта csv в базу данных проекта
        Запуск производится командой python manage.py import_csv
        Заполнить базу можно только один раз, при повторном заполнении
        появится ошибка UniqueConstraint
        Если нужно удалить БД используйте python manage.py flush
        Или просто удалите файл db.sqlite3
        """
        # открываем в менеджере контекста для автоматического закрытия файла
        # аргумент newline - чтобы знаки абзаца случайно не попали в БД
        for file_name, model in FILE_MODEL.items():
            with open(
                    f'static/data/{file_name}.csv',
                    newline='',
                    encoding='utf-8'
            ) as csv_file:
                # Ниже показано, как выглядит объект OrderedDict от DictReader
                # DictReader =([('id', '1'), ('name', 'Фильм'), ('slug', 'movie')])
                datareader = csv.DictReader(csv_file, delimiter=',')
                model.objects.bulk_create(
                    [model(**row) for row in datareader])
                '''
                Аналог кода:
                Category.objects.bulk_create([Category(id=i['id'],
                name=i['name'], slug=i['slug']) for i in datareader])
                '''
        print('Data import was successful')

