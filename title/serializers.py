from django.db.models import Avg
from rest_framework import serializers

from .models import Categories, Genres, Titles


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Categories
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Genres
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        res = obj.reviews.filter(score__isnull=False).aggregate(Avg('score'))
        return res['score__avg']

    class Meta:
        fields = '__all__'
        model = Titles


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genres.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Titles
