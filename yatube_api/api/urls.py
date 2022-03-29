from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .routers import CustomFollowRouter
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_django = SimpleRouter()
router_django.register('posts', PostViewSet)
router_django.register('groups', GroupViewSet)
# (?P=name)
# Matches the same text matched by a previously named capture group.
router_django.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_custom = CustomFollowRouter()
router_custom.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    # JWT-эндпоинты, для управления JWT-токенами:
    path('', include('djoser.urls.jwt')),
    path('', include(router_custom.urls)),
    path('', include(router_django.urls)),
]
