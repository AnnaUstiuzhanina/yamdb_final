from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not isinstance(request.user, AnonymousUser):
            user = get_user_model()
            return (request.user.role == user.Role.admin
                    or request.user.is_superuser)
        else:
            return False
