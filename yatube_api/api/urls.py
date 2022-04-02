from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
# (?P=name)
# Matches the same text matched by a previously named capture group.
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('follow', FollowViewSet)

urlpatterns = [
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
