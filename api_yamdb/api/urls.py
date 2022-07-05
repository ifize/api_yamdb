from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, ReviewViewSet, CategoryViewSet,
                    GenreViewSet, TitleViewSet)

router_v1 = DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
