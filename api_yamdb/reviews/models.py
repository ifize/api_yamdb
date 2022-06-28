from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator)
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    LIST = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Недопустимый символ.'
            )
        ],
        verbose_name='Имя пользователя',
    )
    first_name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Фамилия',
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта',
    )
    role = models.CharField(
        max_length=254,
        choices=LIST,
        default=USER,
        verbose_name='Роль',
    )
    bio = models.TextField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='Биография',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            ),
        ]


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("Slug категории", max_length=100, unique=True)

    class Meta:
        # поля в админке
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title[:79]


class Genre(models.Model):
    name = models.CharField("Название жанра", max_length=100)
    slug = models.SlugField("Slug жанра", max_length=100, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title[:79]


class Title(models.Model):
    name = models.CharField("Название произведения", max_length=100)
    year = models.IntegerField("Год выпуска",)
    # если поле пустое - NULL; необязательное поле
    description = models.TextField("Описание", null=True, blank=True)
    # related_name - для использования Genre.title а не Genre.title_set
    # для обратного отношения
    genre = models.ManyToManyField(
        Genre, related_name="titles", verbose_name="Жанр"
    )
    category = models.ForeignKey(
        Category,
        # on_delete - обязательное поле, при удалении объекта категории
        # произведение остаётся
        # для genre on_delete е указываем, так как оно необязательно для
        # ManyToManyField
        on_delete=models.SET_NULL,
        null=True,
        related_name="titles",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.title[:79]


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.SET_NULL,
        related_name='reviews', blank=True, null=True
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text[:100]

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
