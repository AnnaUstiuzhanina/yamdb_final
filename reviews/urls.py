from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ReviewViewSet

app_name = 'reviews'

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
