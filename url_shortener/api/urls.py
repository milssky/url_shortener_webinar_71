from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

 


router = SimpleRouter()
router.register('urls', UrlViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
