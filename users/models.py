from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Реализация модели User с необходимыми дополнительными полями. """

    class Role(models.TextChoices):
        user = 'user', _('Пользователь')
        moderator = 'moderator', _('Модератор')
        admin = 'admin', _('Администратор')

    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name=_('Email адрес'),
        help_text=_('Email пользователя')
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.user,
        verbose_name=_('Роль пользователя'),
        help_text=_('Роль пользователя'),
    )
    bio = models.TextField(
        blank=True,
        verbose_name=_('Описание пользователя'),
        help_text=_('Описание пользователя'),
    )

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f'{self.email.replace(".", "")}'
        super().save(*args, **kwargs)
