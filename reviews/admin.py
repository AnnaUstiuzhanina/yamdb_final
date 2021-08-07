from django.contrib import admin

from .models import Comment, Review


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'score', 'pub_date')
    search_fields = ('id', 'text', 'author')
    list_filter = ('id',)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'review', 'author', 'pub_date')
    search_fields = ('id', 'text', 'review', 'author',)
    list_filter = ('id',)
