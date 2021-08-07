from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthUserView, RegistrationUserView, UsersView

app_name = "users"

router = DefaultRouter()
router.register('users', UsersView)

urlpatterns = [
    path('v1/auth/email', RegistrationUserView.as_view()),
    path('v1/auth/token', AuthUserView.as_view()),
    path('v1/', include(router.urls)),
]
