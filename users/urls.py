from rest_framework import routers
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateModelView, CustomTokenObtainPairView

router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('auth/token/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserCreateModelView.as_view(), name='users')
]

