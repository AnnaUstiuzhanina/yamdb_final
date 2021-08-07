from django.contrib import admin

from .models import Categories, Genres, Titles


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name', )
    list_filter = ('id', )


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name', )
    list_filter = ('id', )


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'description', 'category',)
    search_fields = ('name', )
    list_filter = ('id', )
