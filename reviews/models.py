from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from title.models import Titles

User = get_user_model()


class Review(models.Model):
    text = models.TextField(verbose_name='Текст ревью')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор ревью',
    )
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Заголовок ревью',
    )
    score = models.PositiveSmallIntegerField(
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Оценка ревью',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации ревью',
    )

    def __str__(self):
        return self.text

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемое ревью',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления комментария',
    )

    def __str__(self):
        return self.text
