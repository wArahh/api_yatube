from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupDetail, GroupList, PostViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
    path('api/v1/groups/', GroupList.as_view()),
    path('api/v1/groups/<int:pk>/', GroupDetail.as_view()),
]
