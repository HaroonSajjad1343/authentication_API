from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignUpView, UserLoginView, UserLogoutView, CurrentUserView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

# Router for User Management ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
