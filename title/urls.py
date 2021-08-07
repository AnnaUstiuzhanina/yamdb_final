from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet

app_name = 'title'

router = DefaultRouter()

router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(router.urls)),
]
