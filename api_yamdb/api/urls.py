from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet, retrieve_token, sign_up
from .views import (CommentViewSet, ReviewViewSet, CategoryViewSet,
                    GenreViewSet, TitleViewSet)

router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')
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

v1_auth_patterns = [
    path('signup/', sign_up, name='sign_up'),
    path('token/', retrieve_token, name='retrieve_token'),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(v1_auth_patterns)),
]
