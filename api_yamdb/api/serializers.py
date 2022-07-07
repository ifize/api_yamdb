from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериалайзер для запроса GET"""
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False,)

    class Meta:
        model = Title
        fields = (
            "id", "name", "year", "rating", "description", "genre", "category"
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
        fields = ("id", "name", "year", "description", "genre", "category")


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        request = self.context['request']
        title_id = self.context.get('view').kwargs.get('title_id')
        if request.stream.method == 'POST':
            if Review.objects.filter(
                title=title_id,
                author=request.user
            ).exists():
                raise serializers.ValidationError(
                    'Можно оставить только один отзыв!'
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
