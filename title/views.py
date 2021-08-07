from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .filters import TitleFilter
from .models import Categories, Genres, Titles
from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer)


class CategoriesViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Categories.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
    permission_classes = (IsAdminOrReadOnly, )


class GenresViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Genres.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
    permission_classes = (IsAdminOrReadOnly, )


class TitlesViewSet(ModelViewSet):
    queryset = Titles.objects.get_queryset().order_by('id')
    filterset_fields = ('genre', 'category', 'year', 'name')
    filterset_class = TitleFilter
    permission_classes = (IsAdminOrReadOnly, )

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleReadSerializer
        return TitleWriteSerializer
