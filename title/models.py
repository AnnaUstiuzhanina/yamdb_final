from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное название категории',
    )


class Genres(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное название жанра',
    )


class Titles(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название произведения',
    )
    year = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        verbose_name='Год публикации',
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genres,
        related_name='titles',
        blank=True,
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория',
    )
