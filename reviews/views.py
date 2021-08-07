from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from title.models import Titles

from .models import Comment, Review
from .permissions import IsAuthorOrModeratorOrReadOnly
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrModeratorOrReadOnly]

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        return serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        queryset = title.reviews.all().order_by('pub_date')
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsAuthorOrModeratorOrReadOnly]

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        queryset = review.comments.all().order_by('pub_date')
        return queryset
