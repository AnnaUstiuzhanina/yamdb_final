from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsAuthorOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not isinstance(request.user, AnonymousUser):
            user = get_user_model()
            return ((obj.author == request.user)
                    or (request.user.role in [user.Role.admin,
                                              user.Role.moderator])
                    or request.user.is_superuser)
        else:
            return False
