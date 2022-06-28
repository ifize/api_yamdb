from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "slug",)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name", "slug",)


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериалайзер для запроса GET"""
    # переопределение поля, чтобы получать не id, а объекты
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    # переопределение поля, тк оне не задано в модели
    rating = serializers.IntegerField()
    # переопределение типа поля, чтобы оно было необязательным
    description = serializers.CharField(required=False)

    class Meta:
        model = Title
        fields = (
            "id", "name", "year", "rating",  "description", "genre", "category"
        )


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериалайзер для запросов POST, PATCH, DELETE"""
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )

    class Meta:
        model = Title
        fields = (
            "id", "name", "year", "rating", "description", "genre", "category"
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
