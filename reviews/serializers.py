from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from title.models import Titles

from .models import Comment, Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=(serializers.CurrentUserDefault())
    )

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = self.context['request'].parser_context['kwargs'].get(
                'title_id')
            author = self.context['request'].user
            title = get_object_or_404(Titles, id=title_id)
            if title.reviews.filter(author=author).exists():
                raise serializers.ValidationError(
                    'Отзыв на это произведение уже существует')
        return data

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = ('id', 'text', 'review_id', 'author', 'pub_date')
        model = Comment
