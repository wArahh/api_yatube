from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from .views import PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls))
]