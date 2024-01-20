from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
