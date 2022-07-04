import django_filters as filters

from reviews.models import Title


class TitleFilter(filters.FilterSet):
    """Кастомный фильтр для возможности фильтрации по разным полям"""
    # CharFilter для поиска по slug, а не по pk
    category = filters.CharFilter(field_name="category__slug")
    genre = filters.CharFilter(field_name="genre__slug")
    # в lookup_expr задаем тип фильтрации
    # icontains - вхождение независимо от регистра (Sql ILIKE)
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    # диапазон дат от минимальной к максимальной, где задается пока неясно

    class Meta:
        model = Title
        fields = ["category", "genre", "name", "year"]
