import django_filters as filters

from reviews.models import Title


class TitleFilter(filters.FilterSet):
    """Кастомный фильтр для возможности фильтрации по разным полям"""
    category = filters.CharFilter(field_name="category__slug")
    genre = filters.CharFilter(field_name="genre__slug")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Title
        fields = ["category", "genre", "name", "year"]
