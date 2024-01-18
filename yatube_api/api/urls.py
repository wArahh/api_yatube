from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, GroupList, GroupDetail

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
    path('api/v1/groups/' , GroupList.as_view()),
    path('api/v1/groups/<int:pk>/', GroupDetail.as_view()),
]