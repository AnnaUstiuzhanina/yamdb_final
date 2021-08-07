from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    """Правило на принадлежаность текущего пользователя к роли
    Администратора."""
    message = ('Только пользоваетль с ролью Администратор может '
               'просматривать данный материал')

    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser):
            user = get_user_model()
            return (request.user.role == user.Role.admin
                    or request.user.is_superuser)
        else:
            return False
